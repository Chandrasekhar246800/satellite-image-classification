# Satellite Image Classification with Deep Learning 🛰️

A deep learning project that classifies satellite images into 10 land cover categories using a Convolutional Neural Network (CNN). This project was built with Python, TensorFlow, and Keras on the EuroSAT dataset.



## Project Summary

This project tackles the challenge of land use and land cover classification from satellite imagery. I started by building a baseline model with a Random Forest Classifier, which achieved **67.48%** accuracy. To improve upon this, I implemented a Convolutional Neural Network (CNN), which is specifically designed for image data. By leveraging techniques like **data augmentation**, the final CNN model achieved a significantly higher accuracy.

### Final Model Performance
* **Accuracy:** **81.43%** on the unseen test set.

## Key Features
* **Data Processing:** Loaded and preprocessed a dataset of 27,000 satellite images.
* **Baseline Model:** Established an initial benchmark using a traditional machine learning approach (Random Forest).
* **Deep Learning Model:** Built, trained, and evaluated a CNN from scratch.
* **Model Improvement:** Implemented data augmentation (random flips, rotations) to create a more robust model.
* **Environment:** All development was done in a managed Python virtual environment (`venv`).

## Technologies Used
* **Python**
* **TensorFlow / Keras**
* **Scikit-learn**
* **NumPy** & **Pandas** for data manipulation
* **Pillow** for image processing
* **Matplotlib** for visualization
* **Git & GitHub** for version control

## How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd your-repository-name
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the Jupyter Notebook:**
    Open `land_cover_notebook.ipynb` and run the cells.
