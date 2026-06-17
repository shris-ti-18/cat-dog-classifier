# import streamlit as st
# import tensorflow as tf
# import numpy as np
# from PIL import Image

# model = tf.keras.models.load_model("cat_dog_classifier.keras")

# st.title("🐱 Cat vs Dog Classifier")

# uploaded_file = st.file_uploader(
#     "Upload a cat or dog image",
#     type=["jpg", "jpeg", "png"]
# )

# if uploaded_file:
#     img = Image.open(uploaded_file).convert("RGB")

#     st.image(img, caption="Uploaded Image", width= 350)

#     img = img.resize((128,128))
#     img = np.array(img) / 255.0
#     img = np.expand_dims(img, axis=0)

#     pred = model.predict(img)[0][0]

#     if pred > 0.5:
#         st.success(f"🐶 Dog ({pred*100:.2f}%)")
#     else:
#         st.success(f"🐱 Cat ({(1-pred)*100:.2f}%)")
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("cat_dog_classifier.keras")

st.title("🐱 Cat vs Dog Classifier")

uploaded_file = st.file_uploader(
    "Upload a cat or dog image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")

    st.image(img, caption="Uploaded Image", width=350)

    if st.button("Predict"):
        img_resized = img.resize((128, 128))
        img_array = np.array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        pred = model.predict(img_array, verbose=0)[0][0]

        if pred > 0.5:
            st.success(f"🐶 Dog ({pred*100:.2f}% confidence)")
        else:
            st.success(f"🐱 Cat ({(1-pred)*100:.2f}% confidence)")