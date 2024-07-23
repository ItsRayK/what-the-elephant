#-------------------#
#      Imports      #
#-------------------#

from pathlib import Path
import streamlit as st

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


#-------------------#
#   Page Elements   #
#-------------------#

# Display Header
st.header(f"Elephant Jokes", anchor=False)

# About Text
st.markdown('''
            ### What the heck even is this?!
            Just me playing with Streamlit stuff.
''')