import streamlit as st
import os
import tempfile
import cv2

# from pyzbar.pyzbar import decode
import my_qrdet
from PIL import Image

# Title of the app
st.title("QR Code Scanner - Upload or Camera")

# Option to either upload an image or take a picture
option = st.radio("Choose an option", ("Upload an image", "Take a picture from camera"))

# Layout to display options
col1, col2 = st.columns([10, 3])  # Larger width for the camera input

# QReader Object
qreader = my_qrdet.QReader()

if option == "Upload an image":
    # File uploader for the QR code image
    uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        # Load and display the uploaded image
        image = Image.open(uploaded_file)
        image = my_qrdet._prepare_input(source = image)
        st.image(image, caption="Uploaded QR Code", use_container_width=True)

        # Decode the QR code using pyzbar
        # decoded_data = decode(image)
        decoded_data = qreader.detect_and_decode(image=image)
        
        if decoded_data:
            # for qr_data in decoded_data:
                # qr_data = obj.data.decode('utf-8')
                # qr_data = obj
                # st.success(f"Decoded Data: {qr_data}")
            # st.success(f"Decoded Data: {decoded_data}")
            # st.success(f"Decoded Data:\n", (qr_data, "\n") for qr_data in decoded_data)
            all_data = "\n".join(f"{i}. :white[st.text({qr_data})]" for i, qr_data in enumerate(decoded_data, start=1))
            st.write(f"Decoded Data:\n{all_data}")

        
        else:
            st.warning("No QR Code detected.")

elif option == "Take a picture from camera":
    # with col2:  # Use col2 (larger column) for the camera
        # Camera input widget
    camera_image = st.camera_input("Capture a QR Code")
    
    if camera_image:
        # Load and display the captured image
        image = Image.open(camera_image)
        image = my_qrdet._prepare_input(source = image)
        st.image(image, caption="Captured QR Code")
    
        # Decode the QR code using pyzbar
        # decoded_data = decode(image)
        decoded_data = qreader.detect_and_decode(image=image)
        
        if decoded_data:
            for qr_data in decoded_data:
            #     qr_data = obj.data.decode('utf-8')
                # qr_data = obj
                st.success(f"Decoded Data: {qr_data}")
            # st.success(f"Decoded Data: {decoded_data}")
        else:
            st.warning("No QR Code detected.")


