import streamlit as st
from qreader import QReader
from PIL import Image

st.title("QR Code Scanner using qreader")

# File uploader for the QR code image
uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded QR Code", use_column_width=True)
    
    # Use QReader to decode the QR code
    try:
        qr_reader = QReader()
        qr_data = qr_reader.decode(uploaded_file)
        if qr_data:
            st.success(f"Decoded Data: {qr_data}")
        else:
            st.warning("No QR code detected in the uploaded image.")
    except Exception as e:
        st.error(f"Error decoding QR code: {e}")
