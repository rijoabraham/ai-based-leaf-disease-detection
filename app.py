from pathlib import Path
from flask import Flask, redirect, render_template, request
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd
import os
import urllib.request
import gdown
import time
# ========== Google Drive Auto Model Download ==========

model_path = "plant_disease_model_1_latest.pt"

if not os.path.exists(model_path):
    print("Downloading model from Google Drive...")
    # Correct ID from your share link
    gdown.download("https://drive.google.com/uc?id=1XBo4fdRs3mihkqfIYhgnfr5a79b63ZUo", model_path, quiet=False)

# =======================================================

# Set base directory
BASE_DIR = Path(__file__).resolve().parent

# Load crop season information
crop_seasons = pd.read_csv(BASE_DIR / "crop_seasons.csv")

# Load disease and supplement information
disease_info = pd.read_csv(BASE_DIR / "disease_info.csv", encoding='cp1252')
supplement_info = pd.read_csv(BASE_DIR / "supplement_info.csv", encoding='cp1252')

# Function to reload data (clears any caching)
def reload_data():
    global disease_info, supplement_info
    disease_info = pd.read_csv(BASE_DIR / "disease_info.csv", encoding='cp1252')
    supplement_info = pd.read_csv(BASE_DIR / "supplement_info.csv", encoding='cp1252')

# Load CNN model
model = CNN.CNN(39)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

# Function to make predictions
def prediction(image_path):
    image = Image.open(image_path).convert('RGB')
    image = image.resize((224, 224))
    input_data = TF.to_tensor(image)
    input_data = input_data.unsqueeze(0)
    with torch.no_grad():
        output = model(input_data)
    output = output.detach().numpy()
    
    # Apply softmax to get probabilities
    exp_output = np.exp(output - np.max(output))
    probabilities = exp_output / np.sum(exp_output, axis=1, keepdims=True)
    
    index = np.argmax(output)
    accuracy = float(probabilities[0][index]) * 100  # Convert to percentage
    return index, round(accuracy, 2)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/index')
def ai_engine_page():
    return render_template('index.html')

@app.route('/mobile-device')
def mobile_device_detected_page():
    return render_template('mobile-device.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    reload_data()  # Reload data to pick up any CSV changes
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename

        upload_folder = BASE_DIR / "static"
        upload_folder.mkdir(exist_ok=True)
        file_path = upload_folder / filename
        image.save(file_path)

        pred, accuracy = prediction(file_path)
        title = disease_info['disease_name'][pred]
        description = disease_info['description'][pred]
        prevent = disease_info['Possible Steps'][pred]
        image_url = disease_info['image_url'][pred]
        supplement_name = supplement_info['supplement name'][pred]
        supplement_image_url = supplement_info['supplement image'][pred]
        supplement_buy_link = supplement_info['buy link'][pred]
        supplement_price = supplement_info['price'][pred]

        return render_template('submit.html', title=title, desc=description, prevent=prevent,
                               image_url=image_url, pred=pred, sname=supplement_name,
                               simage=supplement_image_url, buy_link=supplement_buy_link, accuracy=accuracy,
                               sprice=supplement_price, spred=pred)

@app.route('/market', methods=['GET', 'POST'])
def market():
    reload_data()  # Reload data each time to pick up any CSV changes
    return render_template('market.html', supplement_image=list(supplement_info['supplement image']),
                           supplement_name=list(supplement_info['supplement name']),
                           disease=list(disease_info['disease_name']),
                           prices=list(supplement_info['price']),
                           buy=list(supplement_info['buy link']))

@app.route('/crop-seasons')
def crop_seasons_page():
    global crop_seasons
    crop_seasons = pd.read_csv(BASE_DIR / "crop_seasons.csv")
    crop_data = crop_seasons.to_dict('records')
    return render_template('crop-seasons.html', crops=crop_data)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/shipping-payment')
def shipping_payment():
    return render_template('shipping-payment.html')

@app.route('/track-order')
def track_order():
    return render_template('track-order.html')

# Handling 404 error

@app.errorhandler(404)
def handle_404(e):
    if request.path.startswith('/hybridaction/'):
        return '', 204  # Cleanly ignore bot/extension hits
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
