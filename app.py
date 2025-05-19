import streamlit as st
import os
import tempfile
import cv2
import numpy as np

# from pyzbar.pyzbar import decode
import my_qrdet
from PIL import Image

# Title of the app
st.title("QR Code Scanner - Upload or Camera")

# Option to either upload an image or take a picture
option = st.radio("Choose an option", ("Upload an image", "Take a picture from camera"))

# Layout to display options
# col1, col2 = st.columns([3, 3])  # Larger width for the camera input

# QReader Object
qreader = my_qrdet.QReader()

if option == "Upload an image":
    # File uploader for the QR code image
    uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        # Load and display the uploaded image
        # image = Image.open(uploaded_file)
        image_raw = Image.open(uploaded_file)
        image = my_qrdet._prepare_input(source = image_raw)
        image = np.array(image) # Image is in BGR
        # st.image(image, caption="Uploaded QR Code", use_container_width=True)

        # Decode the QR code using pyzbar
        # decoded_data = decode(image)
        # decoded_data = qreader.detect_and_decode(image=image)
        decoded_data, detections = qreader.detect_and_decode(image=image, return_detections = True)

        for i in range(len(detections)):
            bbox = detections[i]['bbox_xyxy']
            cxcy = detections[i]['cxcy']
            wh = detections[i]['wh']
            polygon_xy = detections[i]['polygon_xy']
            confidence = detections[i]['confidence']
            
            # Draw the center of the bounding box
            cv2.circle(image, (int(cxcy[0]), int(cxcy[1])), 5, (0, 0, 255), -1)
            # Put Text for identification

            # Draw the polygon
            # cv2.polylines(image, [np.int32(polygon_xy)], isClosed=True, color=(255, 0, 255), thickness=2) 
            # Draw the bounding box
            if decoded_data[i]:
                cv2.rectangle(image, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2)
            else:
                cv2.rectangle(image, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (255, 0, 0), 2)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        st.image(image, caption="Uploaded QR Code", use_container_width=True)
        
        if decoded_data:
            # if you want to use st.success
            # all_data = "\n".join(f"{i}. str({qr_data.replace("$", "\\$")})" for i, qr_data in enumerate(decoded_data, start=1))
            # st.success(f"Decoded Data:\n{all_data}")
            st.write("Decoded Data:")
            for i, qr_data in enumerate(decoded_data, start=1):
                if qr_data:
                    qr_data.replace("$", "\\$")
                    st.success(f"{i}: {qr_data}")
            # all_data = "\n".join(f"{i}. {qr_data.replace("$", "\\$")}" for i, qr_data in enumerate(decoded_data, start=1))
            # st.success(f"Decoded Data:\n{all_data}")
            # # st.write(f"Decoded Data:\n{all_data}")

        
        else:
            st.warning("No QR Code detected.")

elif option == "Take a picture from camera":
    # with col2:  # Use col2 (larger column) for the camera
        # Camera input widget
    camera_image = st.camera_input("Capture a QR Code")
    
    if camera_image:
        # Load and display the uploaded image
        # image = Image.open(uploaded_file)
        image_raw = Image.open(uploaded_file)
        image = my_qrdet._prepare_input(source = image_raw)
        image = np.array(image) # Image is in BGR
        # st.image(image, caption="Uploaded QR Code", use_container_width=True)

        # Decode the QR code using pyzbar
        # decoded_data = decode(image)
        # decoded_data = qreader.detect_and_decode(image=image)
        decoded_data, detections = qreader.detect_and_decode(image=image, return_detections = True)

        for i in range(len(detections)):
            bbox = detections[i]['bbox_xyxy']
            cxcy = detections[i]['cxcy']
            wh = detections[i]['wh']
            polygon_xy = detections[i]['polygon_xy']
            confidence = detections[i]['confidence']
            
            # Draw the center of the bounding box
            cv2.circle(image, (int(cxcy[0]), int(cxcy[1])), 5, (0, 0, 255), -1)
            # Put Text for identification

            # Draw the polygon
            # cv2.polylines(image, [np.int32(polygon_xy)], isClosed=True, color=(255, 0, 255), thickness=2) 
            # Draw the bounding box
            if decoded_data[i]:
                cv2.rectangle(image, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2)
            else:
                cv2.rectangle(image, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (255, 0, 0), 2)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        st.image(image, caption="Uploaded QR Code", use_container_width=True)
        
        if decoded_data:
            # if you want to use st.success
            # all_data = "\n".join(f"{i}. str({qr_data.replace("$", "\\$")})" for i, qr_data in enumerate(decoded_data, start=1))
            # st.success(f"Decoded Data:\n{all_data}")
            st.write("Decoded Data:")
            for i, qr_data in enumerate(decoded_data, start=1):
                if qr_data:
                    qr_data.replace("$", "\\$")
                    st.success(f"{i}: {qr_data}")
            # all_data = "\n".join(f"{i}. {qr_data.replace("$", "\\$")}" for i, qr_data in enumerate(decoded_data, start=1))
            # st.success(f"Decoded Data:\n{all_data}")
            # # st.write(f"Decoded Data:\n{all_data}")

        
        else:
            st.warning("No QR Code detected.")

        # # Load and display the captured image
        # image = Image.open(camera_image)
        # image = my_qrdet._prepare_input(source = image)
        # st.image(image, caption="Captured QR Code")
    
        # # Decode the QR code using pyzbar
        # # decoded_data = decode(image)
        # decoded_data = qreader.detect_and_decode(image=image)
        
        # if decoded_data:
        #     # if you want to use st.success
        #     # all_data = "\n".join(f"{i}. str({qr_data.replace("$", "\\$")})" for i, qr_data in enumerate(decoded_data, start=1))
        #     # st.success(f"Decoded Data:\n{all_data}")
        #     for i, qr_data in enumerate(decoded_data, start=1):
        #         if qr_data:
        #             st.markdown(f"Decoded Data {i}: :gray[{qr_data}]")
        #     # all_data = "\n".join(f"{i}. {qr_data.replace("$", "\\$")}" for i, qr_data in enumerate(decoded_data, start=1))
        #     # st.success(f"Decoded Data:\n{all_data}")
        #     # # st.write(f"Decoded Data:\n{all_data}")
        # else:
        #     st.warning("No QR Code detected.")


