from flask import Flask, request, jsonify, render_template
# 1. Add this import at the top
from flask_cors import CORS 
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Initialize the Flask application
app = Flask(__name__)
# 2. Add this line to enable CORS for all routes
CORS(app) 

# --- Load the Trained Model and Class Names ---
try:
    model = tf.keras.models.load_model('land_cover_classifier.keras')
    class_names = ['AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 
                   'Industrial', 'Pasture', 'PermanentCrop', 'Residential', 
                   'River', 'SeaLake']
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# We no longer need the home() route because Next.js is our homepage
# @app.route('/', methods=['GET'])
# def home():
#     return render_template('index.html')

# --- Define the prediction route ---
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded, check server logs.'})

    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided.'})

    file = request.files['image']
    
    try:
        # Read the image file into memory
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes)).resize((64, 64))
        
        # Preprocess the image
        img_array = np.array(img)[:, :, :3]  # Ensure 3 channels (RGB)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0) # Add batch dimension
        
        # Make a prediction
        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = float(np.max(prediction))
        
        # Return the result as JSON
        return jsonify({
            'predicted_class': predicted_class,
            'confidence': f"{confidence*100:.2f}%"
        })
    except Exception as e:
        return jsonify({'error': str(e)})

# --- Run the app ---
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)
    app.run(host="0.0.0.0", port=port)
