# Coral Reef Health Detection System 🪸

## About the Project
The Coral Reef Health Detection System is a machine learning-based application that analyzes coral reef images and classifies them into three categories: **Healthy, Bleached, and Dead**. It uses a trained Convolutional Neural Network (CNN) model to predict coral health from uploaded images.

## Features
- Upload a coral reef image for analysis.
- Predict whether the coral is Healthy, Bleached, or Dead.
- Display the prediction through a simple web interface.
- Help support coral reef monitoring and awareness.

## Technologies Used
- **Python**
- **TensorFlow / Keras**
- **Flask**
- **OpenCV**
- **HTML and CSS**
- **Convolutional Neural Network (CNN)**

## Project Structure
CORAL/
├── app.py
├── coral_health_model.h5
├── templates/
│   └── index.html
└── archive/
    └── Dataset/
        ├── Healthy/
        ├── Bleached/
        └── Dead/

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/gayathri1307s/coral-reef-health-detection.git
   cd coral-reef-health-detection
   ```

2. Install the required dependencies:
   ```bash
   pip install flask tensorflow opencv-python numpy
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open the local URL displayed in the terminal in your browser.

## How to Use
1. Start the Flask application.
2. Upload a coral reef image through the web interface.
3. View the model's predicted coral health category.

## Future Improvements
- Improve prediction accuracy with more diverse coral reef images.
- Expand the dataset to include more coral conditions.
- Deploy the application for online access.



