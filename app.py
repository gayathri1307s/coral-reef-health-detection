from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import cv2
import urllib.request

app = Flask(__name__)
# Load your trained model
model = tf.keras.models.load_model("coral_health_model.h5")
classes = ["Healthy", "Bleached", "Dead"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Case 1: file uploaded
    if "file" in request.files and request.files["file"].filename != "":
        file = request.files["file"]
        filepath = "uploaded.jpg"
        file.save(filepath)
        img = cv2.imread(filepath)

    # Case 2: URL provided
    elif "image_url" in request.form and request.form["image_url"] != "":
        url = request.form["image_url"]
        try:
            resp = urllib.request.urlopen(url)
            image_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
            img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        except:
            return "Failed to download image from URL"

    else:
        return "No image provided"

    # Preprocess image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224,224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Make prediction
    pred = model.predict(img)
    class_idx = np.argmax(pred)
    return f"Predicted Coral Health: {classes[class_idx]}"

if __name__ == "__main__":
    app.run(debug=True)
