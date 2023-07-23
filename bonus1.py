import streamlit as st
from PIL import Image

with st.expander("Start The camera"):
    cameraImage = st.camera_input("Camera")

if cameraImage:
    # image Taken
    img = Image.open(cameraImage)
    # Image Converted into grey Color
    greycolor = img.convert("L")
    # Render the grey Images
    st.image(greycolor)
