import streamlit as st
import os
import tempfile

#setting temprary file
os.environ["QRDET_CACHE_DIR"] = tempfile.gettempdir()

# from pyzbar.pyzbar import decode
from qreader import QReader
from PIL import Image

print("QRDET_CACHE_DIR:", os.getenv("QRDET_CACHE_DIR"))

# Title of the app
st.title("QR Code Scanner - Upload or Camera")

# Option to either upload an image or take a picture
option = st.radio("Choose an option", ("Upload an image", "Take a picture from camera"))

# Layout to display options
col1, col2 = st.columns([3, 3])  # Larger width for the camera input

# QReader Object
qr_reader = QReader()

if option == "Upload an image":
    # File uploader for the QR code image
    uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        # Load and display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded QR Code", use_column_width=True)

        # Decode the QR code using pyzbar
        # decoded_data = decode(image)
        decoded_data = qr_reader.detect_and_decode(image=image)
        
        if decoded_data:
            for obj in decoded_data:
                qr_data = obj.data.decode('utf-8')
                # qr_data = obj
                st.success(f"Decoded Data: {qr_data}")
        else:
            st.warning("No QR Code detected.")

elif option == "Take a picture from camera":
    # with col2:  # Use col2 (larger column) for the camera
        # Camera input widget
    camera_image = st.camera_input("Capture a QR Code")

    if camera_image:
        # Load and display the captured image
        image = Image.open(camera_image)
        st.image(image, caption="Captured QR Code")

        # Decode the QR code using pyzbar
        # decoded_data = decode(image)
        decoded_data = qr_reader.detect_and_decode(image=image)
        
        if decoded_data:
            for obj in decoded_data:
                qr_data = obj.data.decode('utf-8')
                # qr_data = obj
                st.success(f"Decoded Data: {qr_data}")
        else:
            st.warning("No QR Code detected.")





# import streamlit as st
# from pyzbar.pyzbar import decode
# from PIL import Image

# # Title of the app
# st.title("QR Code Scanner - Upload or Camera")

# # Option to either upload an image or take a picture
# option = st.radio("Choose an option", ("Upload an image", "Take a picture from camera"))

# # Layout to display options
# col1, col2 = st.columns([3, 7])  # Larger width for the camera input

# if option == "Upload an image":
#     # File uploader for the QR code image
#     uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])
    
#     if uploaded_file:
#         # Load and display the uploaded image
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded QR Code", use_column_width=True)

#         # Decode the QR code using pyzbar
#         decoded_data = decode(image)
        
#         if decoded_data:
#             for obj in decoded_data:
#                 qr_data = obj.data.decode('utf-8')
#                 st.success(f"Decoded Data: {qr_data}")
#         else:
#             st.warning("No QR Code detected.")
            

# elif option == "Take a picture from camera":
#     with col2:  # Use col2 (larger column) for the camera
#         # Camera input widget
#         # Inject custom CSS for larger camera window
        
#         st.markdown("""
#             <style>
#                 .stCamera { 
#                     width: 100% !important;
#                     height: 500px !important; /* Adjust height */
#                 }
#             </style>
#         """, unsafe_allow_html=True)
        
#         camera_image = st.camera_input("Capture a QR Code")

#         if camera_image:
#             # Load and display the captured image
#             image = Image.open(camera_image)
#             st.image(image, caption="Captured QR Code", use_column_width=True)

#             # Decode the QR code using pyzbar
#             decoded_data = decode(image)
            
#             if decoded_data:
#                 for obj in decoded_data:
#                     qr_data = obj.data.decode('utf-8')
#                     st.success(f"Decoded Data: {qr_data}")
#             else:
#                 st.warning("No QR Code detected.")



# import streamlit as st
# from pyzbar.pyzbar import decode
# from PIL import Image
# import streamlit.components.v1 as components

# # Custom component to control camera input behavior (front/rear camera selection)
# components.html("""
#     <script>
#         const constraints = {
#             video: {
#                 facingMode: "environment"  // 'environment' for rear camera on mobile
#             }
#         };

#         const videoElement = document.querySelector('video');
#         if (videoElement) {
#             navigator.mediaDevices.getUserMedia(constraints)
#                 .then((stream) => {
#                     videoElement.srcObject = stream;
#                 })
#                 .catch((err) => {
#                     console.error("Error accessing the camera:", err);
#                 });
#         }
#     </script>
# """, height=0)

# # Title of the app
# st.title("QR Code Scanner - Upload or Camera")

# # Option to either upload an image or take a picture
# option = st.radio("Choose an option", ("Upload an image", "Take a picture from camera"))

# if option == "Upload an image":
#     # File uploader for the QR code image
#     uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])
    
#     if uploaded_file:
#         # Load and display the uploaded image
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded QR Code", use_column_width=True)

#         # Decode the QR code using pyzbar
#         decoded_data = decode(image)
        
#         if decoded_data:
#             for obj in decoded_data:
#                 qr_data = obj.data.decode('utf-8')
#                 st.success(f"Decoded Data: {qr_data}")
#         else:
#             st.warning("No QR Code detected.")

# elif option == "Take a picture from camera":
#     # Camera input widget (default camera behavior)
#     camera_image = st.camera_input("Capture a QR Code")

#     if camera_image:
#         # Load and display the captured image
#         image = Image.open(camera_image)
        
#         # Resize the image to make it larger if necessary
#         image = image.resize((image.width * 2, image.height * 2))  # Scale up by 2x (adjust as needed)
        
#         st.image(image, caption="Captured QR Code", use_column_width=True)

#         # Decode the QR code using pyzbar
#         decoded_data = decode(image)
        
#         if decoded_data:
#             for obj in decoded_data:
#                 qr_data = obj.data.decode('utf-8')
#                 st.success(f"Decoded Data: {qr_data}")
#         else:
#             st.warning("No QR Code detected.")
