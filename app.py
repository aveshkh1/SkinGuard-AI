import gradio as gr
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# 🔹 Load trained model
model = tf.keras.models.load_model("/kaggle/input/deep-learning-model/tensorflow2/default/1/skin_cancer_vgg16_model.h5")

# 🔹 Class labels
class_labels = {0: "Benign (Non-Cancerous)", 1: "Malignant (Cancerous)"}


# 🔹 Prediction function
def predict_skin_cancer(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    y_pred = model.predict(img_array)[0][0]
    label = 1 if y_pred > 0.45 else 0
    confidence = y_pred if label == 1 else 1 - y_pred

    result = class_labels[label]
    confidence_text = f"Confidence: {confidence * 100:.2f}%"

    if label == 1:
        return f"⚠️ **{result}**\n\n🧬 {confidence_text}\n\nPlease consult a dermatologist for further evaluation."
    else:
        return f"✅ **{result}**\n\n🌿 {confidence_text}\n\nYour skin appears healthy and normal."


# 🎨 Custom CSS
custom_css = """
body { 
    font-family: 'Poppins', sans-serif; 
    background: linear-gradient(135deg, #f9f9fb 0%, #fcefee 100%);
}
.gradio-container {
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3, p, label { 
    font-family: 'Poppins', sans-serif; 
}
.output-textbox { 
    font-size: 18px !important; 
    line-height: 1.6; 
    color: #222; 
    font-weight: 500; 
}
footer { visibility: hidden }
"""

# 🧬 App Title and Description
title = "🧬 SkinGuard AI"
description = """
### 🩺 Smart Skin Cancer Detection  
Upload a **clear photo** of your skin mole or lesion.  
Our AI will predict whether it's **Benign** or **Malignant**, along with confidence level.  

> ⚠️ *Disclaimer: This tool is for educational and awareness purposes only — not a medical diagnosis.*
"""

# ⚙️ Build Interface
with gr.Blocks(theme=gr.themes.Soft(primary_hue="pink", secondary_hue="rose"), css=custom_css) as demo:
    gr.Markdown(f"<h1 style='text-align:center; color:#1f4e79;'>{title}</h1>")
    gr.Markdown(description)

    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Image(type="pil", label="Upload Skin Image")
            output_text = gr.Textbox(label="AI Diagnosis", lines=5, elem_classes=["output-textbox"])
            gr.Button("🔍 Analyze").click(predict_skin_cancer, inputs=image_input, outputs=output_text)

    gr.Markdown("""
    ---
    <div style='text-align:center; color:#555; font-size:15px; margin-top:10px;'>
    © 2025 <b>SkinGuard AI</b> | Developed by <b>Avesh Kharani</b> | For Awareness & Research Use Only
    </div>
    """)

demo.launch(debug=True)
