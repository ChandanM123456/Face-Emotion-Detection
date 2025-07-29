from facial_emotion_recognition import EmotionRecognition
import cv2
import sys
import os # For checking if running in IDLE to decide suppression method

# Initialize EmotionRecognition model
er = EmotionRecognition(device='cpu')

# Initialize webcam capture.
cam = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cam.isOpened():
    print("Error: Could not open webcam. Please check your setup.")
    exit()

print("Webcam opened successfully. Press 'ESC' to exit.")

# Define a function to suppress prints (more robust than direct redirection)
class SuppressPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w') # Redirect to null device
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

while True:
    success, frame = cam.read()

    if not success:
        print("Error: Could not read frame from webcam. Exiting loop.")
        break

    # --- Suppress prints from recognise_emotion for this call ---
    with SuppressPrints():
        frame = er.recognise_emotion(frame, return_type='BGR')

    # Display the processed frame
    cv2.imshow('Facial Emotion Recognition', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
print("Application closed.")
