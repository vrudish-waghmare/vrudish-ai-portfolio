# Importing libraries
import tensorflow as tf
import numpy as np
import tf_keras as keras
from PIL import Image
import os
import requests
import streamlit as st

# class names
class_names = ["apple_pie","baklava","baby_back_ribs","beef_carpaccio","beef_tartare","beet_salad","beignets","bibimbap","bread_pudding","breakfast_burrito","bruschetta","caesar_salad","cannoli","caprese_salad","carrot_cake","ceviche","cheesecake","cheese_plate","chicken_curry","chicken_quesadilla","chicken_wings","chocolate_cake","chocolate_mousse","churros","clam_chowder","club_sandwich","crab_cakes","creme_brulee","croque_madame","cup_cakes","deviled_eggs","donuts","dumplings","edamame","eggs_benedict","escargots","falafel","filet_mignon","fish_and_chips","foie_gras","french_fries","french_onion_soup","french_toast","fried_calamari","fried_rice","frozen_yogurt","garlic_bread","gnocchi","greek_salad","grilled_cheese_sandwich","grilled_salmon","guacamole","gyoza","hamburger","hot_and_sour_soup","hot_dog","huevos_rancheros","hummus","ice_cream","lasagna","lobster_bisque","lobster_roll_sandwich","macaroni_and_cheese","macarons","miso_soup","mussels","nachos","omelette","onion_rings","oysters","pad_thai","paella","pancakes","panna_cotta","peking_duck","pho","pizza","pork_chop","poutine","prime_rib","pulled_pork_sandwich","ramen","ravioli","red_velvet_cake","risotto","samosa","sashimi","scallops","seaweed_salad","shrimp_and_grits","spaghetti_bolognese","spaghetti_carbonara","spring_rolls","steak","strawberry_shortcake","sushi","tacos","takoyaki","tiramisu","tuna_tartare","waffles"]

# Hugging Face URL
MODEL_URL = "https://huggingface.co/vrudish-waghmare/food-vision-big-model/resolve/main/food_vision_big_model.keras"
MODEL_PATH = "models/food_vision_big_model.keras"

# Download model (only if not exists)
def download_model():
    if not os.path.exists(MODEL_PATH):
        os.makedirs("models", exist_ok=True)
        with open(MODEL_PATH, "wb") as f:
            response = requests.get(MODEL_URL)
            f.write(response.content)

# Cache the model
@st.cache_resource
def load_model():
    download_model()
    model = keras.models.load_model(MODEL_PATH)
    return model

# Load model
model = load_model()

# Preprocessing function
def preprocess_image(uploaded_file, img_shape=224):
    """
        Reads in an image from filename, turns it into a tensor and reshapes into
        (224, 224, 3).

        Parameters
        ----------
        filename (str): string filename of target image
        img_shape (int): size to resize target image to, default 224
    """
    # Save uploaded file temporarily
    temp_path = "temp.jpg"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Step 2: Read using TensorFlow
    image = tf.io.read_file(temp_path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [img_shape, img_shape])
    image = tf.expand_dims(image, axis=0)

    # Optional: remove temp file
    os.remove(temp_path)

    return image



def predict_image(uploaded_file):
    """
       Reads in an image and preprocess it using load_and_preprocess_image method and return the prediction probabilities

       Parameters
       ----------
       filename (str): string filename of target image
    """
    processed_image = preprocess_image(uploaded_file)
    pred_probs = model.predict(processed_image)

    predicted_class = class_names[pred_probs.argmax()]
    confidence = np.max(pred_probs)

    return predicted_class, confidence




st.title("🍔 Food Vision Big")

uploaded_file = st.file_uploader("Upload Food Image", type=["jpg", "png", "jpeg"])

if uploaded_file:

    st.image(uploaded_file, caption="Uploaded Image", width=700)

    predicted_class, confidence = predict_image(uploaded_file)
 
    st.success(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}")