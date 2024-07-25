class Jokes:

    def __init__(self):
        self.questions = []
        self.answers = []

    def load_jokes(self, file_path):

        with open(file_path, "r") as jokes:
            lines = [line.rstrip() for line in jokes]

            for line in lines:
                if ">" in line:
                    self.questions.append(line.lstrip(">"))
                elif "<" in line:
                    self.answers.append(line.lstrip("<"))