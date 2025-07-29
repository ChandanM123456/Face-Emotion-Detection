
# Face Emotion Detection 😄😡😢

This project is a real-time facial emotion recognition system using your webcam. It utilizes the `facial_emotion_recognition` Python package and OpenCV to detect and display emotions like happy, sad, angry, etc., directly from webcam feed.

## 🔗 GitHub Repo

Clone this repository:

```bash
git clone https://github.com/ChandanM123456/Face-Emotion-Detection.git
cd Face-Emotion-Detection
```

## 📁 Project Structure

* `facialemotionrecognization.py` – Main script to run the webcam-based facial emotion detector.
* Uses `facial_emotion_recognition` Python package (make sure to install it).

## ⚙️ Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, you can install manually:

```bash
pip install facial_emotion_recognition opencv-python
```

> Note: `facial_emotion_recognition` internally uses deep learning models, so installation might also include `torch`, `numpy`, and other dependencies.

## 🚀 How to Run

### Step-by-step:

1. Clone the repository (if not already done):

   ```bash
   git clone https://github.com/ChandanM123456/Face-Emotion-Detection.git
   cd Face-Emotion-Detection
   ```

2. Run the Python script:

   ```bash
   python facialemotionrecognization.py
   ```

3. The webcam window will open and display the video feed with emotion labels on detected faces.

4. Press the `ESC` key to exit the application.

## 🧠 How It Works

* Captures frames from your webcam using OpenCV.
* Uses `facial_emotion_recognition` to detect faces and classify emotions in real time.
* Overlays the recognized emotion label on the video feed.

## 📌 Notes

* Ensure your webcam is working properly.
* This application runs on CPU (`device='cpu'`), but can be modified to use GPU if available.

## 🙌 Credits

* [facial\_emotion\_recognition PyPI Package](https://pypi.org/project/facial-emotion-recognition/)
* OpenCV library for real-time computer vision.

---

Would you like me to generate a `requirements.txt` file as well?
