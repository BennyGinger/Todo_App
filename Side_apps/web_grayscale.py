# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image
    
st.subheader("Color to Grayscale Converter")

with st.expander("Upload image"):
    image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")
    
if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

if image:
    img = Image.open(image)
    gray_img = img.convert('L')
    st.image(gray_img)