import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras import models

model = models.load_model('CNN_best_model.keras')


def load_image(image_file):
    img = Image.open(image_file)
    return img


st.title("Bird Species Classification")

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])


if image_file is not None:
    st.image(load_image(image_file), width=250)
    image = Image.open(image_file)
    image = image.resize((224, 224))
    image_arr = np.array(image.convert('RGB'))
    image_arr.shape = (1, 224, 224, 3)
    result = model.predict(image_arr)
    ind = np.argmax(result)
    classes = ['AMERICAN GOLDFINCH', 'BARN OWL', 'CARMINE BEE-EATER', 'DOWNY WOODPECKER', 'EMPEROR PENGUIN', 'FLAMINGO']
    print(ind)
    st.header(classes[ind])
