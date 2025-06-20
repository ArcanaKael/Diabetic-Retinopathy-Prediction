# Import libraries
import pandas as pd
import numpy as np
import streamlit as st
import pickle
import tensorflow as tf
import cv2
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
from tensorflow.keras.models import load_model

# Load model and define main app
def run():
    st.title("🔎 Diabetic Retinopathy Detection")
    st.markdown(
        """
        Upload a retina image below, and the model will classify whether the image shows signs of
        **Diabetic Retinopathy (DR)** or is **Normal (No_DR)**.
        """
    )
    
    st.divider()
    file = st.file_uploader("📤 Upload Retina Image (JPG or PNG)", type=["jpg", "png"])

    # Load pre-trained model
    model = load_model('./src/model_sequential.hdf5')
    target_size = (224, 224)

    # Prediction function
    def import_and_predict(image_data, model):
        image = load_img(image_data, target_size=(220, 220))
        img_array = img_to_array(image)
        img_array = tf.expand_dims(img_array, 0)  # Create a batch
        img_array = img_array / 255.0  # Normalize

        predictions = model.predict(img_array)
        idx = np.where(predictions >= 0.6, 1, 0).item()
        jenis = ['DR', 'No_DR']
        result = f"🧠 **Prediction Result:** {jenis[idx]}"
        return result

    # Display uploaded image and prediction
    if file is None:
        st.info("Please upload a retina image to proceed.")
    else:
        result = import_and_predict(file, model)
        st.success(result)  # Menampilkan hasil di atas gambar
        st.image(file, caption="🖼️ Uploaded Retina Image")

# Run the app
if __name__ == "__main__":
    run()