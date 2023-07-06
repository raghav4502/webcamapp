import streamlit as st
from PIL import Image

with st.expander("Open Camera"):#prompts the user to start camera or not
    img = st.camera_input("Take A Photo")#starts camera

if img:
    image = Image.open(img)#creates img instance
    greyimg = image.convert("L")#convert img to grayscale
    st.image(greyimg)#render img on the website
