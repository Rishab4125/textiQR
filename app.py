import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image

st.title("QR Code Scanner")

# File uploader for the QR code image
uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Load and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded QR Code", use_column_width=True)

    # Decode the QR code using pyzbar
    decoded_data = decode(image)
    
    if decoded_data:
        for obj in decoded_data:
            qr_data = obj.data.decode('utf-8')
            st.success(f"Decoded Data: {qr_data}")
    else:
        st.warning("No QR Code detected.")
