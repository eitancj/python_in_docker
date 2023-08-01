### Investment Growth Calculator ###
# simple web application to practice building python-app images with Docker #
# https://app.pluralsight.com/guides/dockerfile-for-python-web-projects #
# latest tested Python version: 3.11.4


import streamlit as st
from PIL import Image
import os

origDir = os.getenv('PWD')

# title
st.title(":snake: Python App in a Docker Image :whale:")
st.header("\nCalculate Growth Percentage")


initial = st.number_input("Initial Investment in US$",step=100)
yr = st.number_input("Growth Period in Years",step=1)
growth = st.number_input("Growth Rate in %", step=0.50)
final_val = 0
current_val = initial
for year in range(int(yr)):
   current_val += (growth * current_val / 100)
   final_val = current_val

# perform cashflow projections for the next 5 years
st.write(f'{initial}$, after {int(yr)} years and at a fixed growth rate \
         of {growth}%, becomes:')
st.write(f':money_with_wings: **:green[{final_val:,.2f}]** :money_with_wings:')

# Hide 'made with Streamlit' footer 
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True) #https://github.com/streamlit/streamlit/issues/892

# print random gummy bears
jpgFile = os.path.join(origDir,'aux/gummy_bears.jpg')
try:
    bears = Image.open(jpgFile)
except IOError:
    raise "\nFailed to process jpg image"

print ("")
st.image(bears, caption='random gummy bears')
