# Cat vs Dog Classifier 🐱🐶

A deep learning-based image classification web application that predicts whether an uploaded image contains a **cat** or a **dog**. The model is built using **TensorFlow/Keras** and deployed with **Streamlit**.

## 🌐 Live Demo

🚀 **Try the app here:**
[Cat vs Dog Classifier Live App](https://cat-dog-classifier-bnemxgg3snkzgllpxr4dtw.streamlit.app/?utm_source=chatgpt.com)

---

## 📌 Features

* Upload an image in JPG, JPEG, or PNG format.
* Predicts whether the image is a **Cat** or **Dog**.
* Displays prediction confidence.
* Interactive and user-friendly web interface.
* Real-time inference using a trained CNN model.

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* NumPy
* Pillow (PIL)
* Streamlit

---

## 📊 Dataset

Dataset used: **Cats vs Dogs (Microsoft Asirra Dataset)**

* Total Images: **23,262**
* Corrupted Images Removed: **1,738**
* Training Images: **18,609**
* Validation Images: **4,653**
* Image Resolution: **128 × 128**

---

## 🧠 Model Architecture

Custom Convolutional Neural Network (CNN):

```text
Input (128×128×3)
│
├── Conv2D (32 filters, ReLU)
├── MaxPooling2D
│
├── Conv2D (64 filters, ReLU)
├── MaxPooling2D
│
├── Conv2D (128 filters, ReLU)
├── MaxPooling2D
│
├── Flatten
├── Dense (128, ReLU)
├── Dropout (0.5)
│
└── Dense (1, Sigmoid)
```

---

## 📈 Training Results

| Epoch | Training Accuracy | Validation Accuracy |
| ----- | ----------------- | ------------------- |
| 1     | 63.6%             | 71.1%               |
| 2     | 74.9%             | 79.0%               |
| 3     | 80.1%             | 80.0%               |
| 4     | 83.7%             | 80.1%               |
| 5     | 86.9%             | 80.7%               |

### Final Performance

* **Training Accuracy:** 86.9%
* **Validation Accuracy:** 80.65%
* **Optimizer:** Adam
* **Loss Function:** Binary Crossentropy
* **Epochs:** 5

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/cat-dog-classifier.git
cd cat-dog-classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📂 Project Structure

```text
cat-dog-classifier/
│
├── app.py
├── cat_dog_classifier.keras
├── requirements.txt
├── README.md
```

---

## 🎯 Future Improvements

* Improve accuracy using Transfer Learning (MobileNetV2).
* Add support for more animal classes.
* Display prediction probabilities with charts.
* Deploy using Docker and cloud services.
* Add image augmentation and hyperparameter tuning.

---

## 📷 Sample Workflow

1. Upload a cat or dog image.
2. The image is resized to **128 × 128**.
3. The CNN model processes the image.
4. The app displays the predicted class and confidence score.

---

## 👨‍💻 Author

**Shristi Kumari**
First-Year Undergraduate Student | Machine Learning & Competitive Programming Enthusiast

* GitHub: *https://github.com/shris-ti-18*
* LinkedIn: *https://www.linkedin.com/in/shristi-kumari-6a10a1397/*

⭐ If you found this project useful, consider giving the repository a star!
