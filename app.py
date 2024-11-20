import streamlit as st
import qrcode
import qreader from QReader
# from PIL import Image
import cv2
import numpy as np


st.title("QR Code Generator & Scanner")

menu = st.sidebar.selectbox("Menu", ["Generate QR Code", "Scan QR Code"])

if menu == "Generate QR Code":
    st.header("Generate QR Code")
    input_text = st.text_input("Enter text/URL for the QR Code:")
    if st.button("Generate"):
        if input_text:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
            qr.add_data(input_text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            st.image(img, caption="Your QR Code", use_column_width=True)
            img.save("generated_qr.png")
            with open("generated_qr.png", "rb") as file:
                st.download_button(label="Download QR Code", data=file, file_name="QRCode.png", mime="image/png")
        else:
            st.warning("Please enter some text or a URL.")

elif menu == "Scan QR Code":
    st.header("Scan QR Code")
    uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded QR Code", use_column_width=True)
        opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        # detector = cv2.QRCodeDetector()
        data = QReader.detect_and_decode(image=opencv_image)
        # data, _, _ = detector.detectAndDecode(opencv_image)
        if data:
            st.success(f"Decoded Data: {data}")
        else:
            st.error("Could not decode the QR Code.")
