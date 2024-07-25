#-------------------#
#      Imports      #
#-------------------#

from pathlib import Path
import streamlit as st
from site_utils import Jokes

#-------------------#
#       Setup       #
#-------------------#

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"

### Page Configuration
st.set_page_config(page_title="What the elephant?!", page_icon="🐘")

### Apply Custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#-------------------#
#   Session State   #
#-------------------#
if 'jokes' not in st.session_state:
    st.session_state['jokes'] = Jokes()
    st.session_state['jokes'].load_jokes( THIS_DIR / "the_elephant_joke.txt" )

if 'curr_joke' not in st.session_state:
    st.session_state['curr_joke'] = 0

#-------------------#
#   Page Elements   #
#-------------------#

# Display Header
st.title(f"Elephant Jokes 🐘", anchor=False)

st.markdown("#")

col1, col2, col3 = st.columns(3)

joke_text_placeholder = st.empty()

joke_text_placeholder.header(st.session_state['jokes'].questions[st.session_state['curr_joke']], anchor=False)

if col1.button("Back", use_container_width=True):
    if st.session_state['curr_joke'] > 0:
        st.session_state['curr_joke'] -= 1
        joke_text_placeholder.header(st.session_state['jokes'].questions[st.session_state['curr_joke']], anchor=False)

if col2.button("Reveal Answer", type="primary", use_container_width=True):
    joke_text_placeholder.header(st.session_state['jokes'].answers[st.session_state['curr_joke']], anchor=False)

if col3.button("Next", use_container_width=True):
    if st.session_state['curr_joke'] == len(st.session_state['jokes'].questions) - 1:
        st.session_state['curr_joke'] = 0
    else:
        st.session_state['curr_joke'] += 1
    joke_text_placeholder.header(st.session_state['jokes'].questions[st.session_state['curr_joke']], anchor=False)

#st.session_state