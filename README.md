# 🩺 Skin Guard AI

**Skin Guard AI** is a deep learning–based web application that classifies skin lesions as *benign* or *malignant* using a Convolutional Neural Network (CNN) and Transfer Learning.  
The web interface is built using **Gradio**, providing an easy-to-use interface for quick predictions.

---

## 🚀 Features
- Upload an image and get instant skin disease classification  
- User-friendly Gradio interface  
- Supports local image upload and real-time results  
- Built with TensorFlow and transfer learning (VGG16 backbone)  

---

## 🧠 Tech Stack
- **Python 3.10+**
- **TensorFlow 2.18.0**
- **NumPy 1.26.4**
- **Scikit-learn 1.2.2**
- **Seaborn 0.12.2**
- **Gradio 5.38.1**

---

## ⚙️ Implementation Details

### 1. Data Preparation
- Dataset collected and trained in a **Kaggle Notebook**.  
- Preprocessing includes resizing images, normalization, and train-test split.  
- Data augmentation used to reduce overfitting.

### 2. Model Development
- Fine-tuned **VGG16** (transfer learning).  
- Loss: **Binary Crossentropy**. Optimizer: **Adam**.  
- Observed some overfitting — regularization/augmentation can improve it.

### 3. Evaluation
- Evaluated using accuracy, confusion matrix, and ROC-AUC.  
- Noted class imbalance; plan to address with augmentation or class weights.

### 4. Web Interface
- Built with **Gradio** for local testing.  
- Users can upload images and see predictions instantly.  
  - 🟢 *Benign* — Safe  
  - 🔴 *Malignant* — Needs medical attention

---

## 🖥️ Usage

1. **Clone this repository**
   ```bash
   git clone https://github.com/aveshkh1/Skin-Guard-AI.git
   cd Skin-Guard-AI
   
2.**Install dependencies**
   pip install -r requirements.txt
   python app.py

3.**Run the web app**
    python app.py

## 📁 Project Structure
Skin-Guard-AI/
│
├── app.py                     # Gradio web app
├── requirements.txt           # Python dependencies
├── skin_guard_notebook.ipynb  # Kaggle notebook for model training
├── README.md                  # Project documentation


## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Authors
Avesh Kharani
AI & Deep Learning Enthusiast

🧠 GitHub: aveshkh1

🔗 LinkedIn: aveshkharani7483

