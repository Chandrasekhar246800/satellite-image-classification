
# Satellite Image Classification with Deep Learning 🛰️

A full-stack deep learning project that classifies satellite images into 10 land cover categories using a Convolutional Neural Network (CNN). Built with Python (Flask, TensorFlow, Keras) for the backend and Next.js (React) for the frontend. Trained on the EuroSAT dataset.

---

## Project Summary

This project tackles the challenge of land use and land cover classification from satellite imagery. It includes:

- **Backend:** Flask API serving a trained CNN model for image classification
- **Frontend:** Next.js web app for uploading images and viewing predictions

### Final Model Performance
* **Accuracy:** **81.43%** on the unseen test set.

## Key Features
- **Data Processing:** Loaded and preprocessed a dataset of 27,000 satellite images
- **Baseline Model:** Random Forest Classifier (**67.48%** accuracy)
- **Deep Learning Model:** Custom CNN (**81.43%** accuracy)
- **Model Improvement:** Data augmentation (random flips, rotations)
- **Full-stack App:** User-friendly web interface for predictions

## Technologies Used
- **Python, Flask, TensorFlow, Keras, Scikit-learn**
- **NumPy, Pandas, Pillow**
- **Next.js, React**
- **Git & GitHub**

---

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Chandrasekhar246800/satellite-image-classification.git
cd satellite-image-classification
```

### 2. Run the Backend (Flask API)
```bash
cd satellite-app
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python app.py
# The API will run on http://127.0.0.1:5000
```

### 3. Run the Frontend (Next.js)
```bash
cd ../satellite-frontend
npm install
# Create a .env.local file with the following line:
# NEXT_PUBLIC_API_URL=http://127.0.0.1:5000
npm run dev
# The app will run on http://localhost:3000
```

---

## 🚀 Deployment Guide

### Deploy Backend (Flask + ML) on Render
1. Go to [https://render.com/](https://render.com/) and sign up.
2. Click "New Web Service" and connect your GitHub repo.
3. Set root directory to `satellite-app`.
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python app.py`
6. Make sure your Flask app uses `host='0.0.0.0'` and `port=os.environ.get('PORT', 5000)` (already set).
7. Deploy and copy your public backend URL (e.g., `https://your-backend.onrender.com`).

### Deploy Frontend (Next.js) on Vercel
1. Go to [https://vercel.com/](https://vercel.com/) and sign up.
2. Import your GitHub repo and set root directory to `satellite-frontend`.
3. In project settings, add an environment variable:
    - `NEXT_PUBLIC_API_URL=https://your-backend.onrender.com`
4. Deploy and get your public frontend URL.

---

## Environment Variables

**Frontend:**
Create a `.env.local` file in `satellite-frontend`:
```
NEXT_PUBLIC_API_URL=https://your-backend.onrender.com
```

**Backend:**
No special environment variables needed for basic deployment.

---

## Project Structure

```
satellite-image-classification/
├── satellite-frontend/      # Next.js frontend
├── satellite-app/           # Flask backend + ML model
├── data/                    # EuroSAT images
├── land_cover_classifier.keras
├── requirements.txt
└── README.md
```

---

## License

MIT License. See [LICENSE](LICENSE) for details.
