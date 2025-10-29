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

### 1. **Data Preparation**
- Dataset collected and trained in **Kaggle Notebook**  
- Preprocessing includes resizing images, normalization, and train-test split  
- Data augmentation used to reduce overfitting  

### 2. **Model Development**
- Implemented CNN model and fine-tuned using **VGG16 transfer learning**  
- Used **Binary Cross Entropy loss** and **Adam optimizer**  
- Achieved good training accuracy but observed overfitting on test data — further regularization can improve it  

### 3. **Evaluation**
- Evaluated using accuracy, confusion matrix, and ROC-AUC  
- Identified class imbalance; plans for data balancing or augmentation  

### 4. **Web Interface**
- Built with **Gradio** for seamless local testing  
- Users can upload skin images and view prediction results instantly  
- Example output:  
  - 🟢 *Benign* — Safe  
  - 🔴 *Malignant* — Needs medical attention  

---

## 🖥️ Usage

1. **Clone this repository**
   ```bash
   git clone https://github.com/aveshkh1/Skin-Guard-AI.git
   cd Skin-Guard-AI
