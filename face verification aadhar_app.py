import streamlit as st
import cv2
import numpy as np

st.title("FAadhaar Verification App")

# Aadhaar number input
aadhaar_number = st.text_input("Enter Aadhaar Number")

# Upload photo
uploaded_file = st.file_uploader("Upload Aadhaar Photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, channels="BGR", caption="Uploaded Aadhaar Photo")

    # Face detection using OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        st.success(f"✅ Face detected for Aadhaar: {aadhaar_number}")
    else:
        st.error("❌ No face detected. Please upload a valid Aadhaar photo.")
