###    Python App in Docker Image     ###
# Practice containerizing a python app  #
# using Docker with this simple web app #
#             EitanCJ 2023              #
#             Python 3.11.4             #
###    --------------------------     ###


# Modules
import streamlit as st
from PIL import Image
import os

# Title
st.title(":snake: Python App in a Docker Image :whale:")
st.header("\nCalculate Growth Percentage")

# Vars
origDir = os.getenv('PWD')
initial = st.number_input("Initial Investment in US Dollars",step=100)
yr = st.number_input("Growth Period in Years",step=1)
growth = st.number_input("Growth Rate in %", step=0.50)
final_val = 0
current_val = initial

## Main ## 

# Calculate growth
for year in range(int(yr)):
   current_val += (growth * current_val / 100)
   final_val = current_val

# Predict capital growth based on user input
st.write(f'${initial}, after {int(yr)} years and at a fixed growth rate \
         of {growth}%, becomes:')
st.write(f':money_with_wings: **:green[{final_val:,.2f}]** :money_with_wings:')

# Hide 'made with Streamlit' footer 
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)  # https://github.com/streamlit/streamlit/issues/892

# Display random gummy bears image
jpgFile = os.path.join(origDir,'aux/gummy_bears.jpg')
try:
    bears = Image.open(jpgFile)
except IOError:
    raise "\nFailed to process jpg image"

print ("")
st.image(bears, caption='random gummy bears')
