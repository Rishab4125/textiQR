import streamlit as st
from qreader import QReader
from PIL import Image

st.title("QR Code Scanner App")
st.subheader("Scan QR Codes with ease!")

# Sidebar information
st.sidebar.title("How to Use")
st.sidebar.write("""
1. Upload an image containing a QR Code.
2. The app will scan and display the QR Code's content.
3. If the QR Code cannot be detected, try a clearer image.
""")

# QR Code Scanner
st.header("Upload a QR Code Image")
uploaded_file = st.file_uploader("Choose a QR Code image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    try:
        # Load the image using PIL
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded QR Code", use_column_width=True)

        # Decode QR Code using QReader
        qr_reader = QReader()
        qr_data = qr_reader.decode(uploaded_file)

        # Display the result
        if qr_data:
            st.success("QR Code Detected!")
            st.write("Decoded Content:")
            st.code(qr_data)
        else:
            st.warning("No QR Code detected in the uploaded image.")
    except Exception as e:
        st.error(f"An error occurred while scanning the QR Code: {e}")
