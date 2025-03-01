# Face-Detection-Using-OpenCV
A real-time Face Detection System built using OpenCV and Haar Cascade Classifier. This system captures live video from the webcam, processes the video frames to detect faces, and visually highlights the detected faces with rectangles in real-time.


## Features

-Real-Time Face Detection: Detects faces from a live video feed.

-Haar Cascade Classifier: Uses OpenCV's pre-trained Haar Cascade classifier to identify faces.


## Required Libraries:

opencv-python - for computer vision functionalities


## Run Locally

Clone the project

```bash
git clone https://github.com/your-username/Face-Detection-Using-OpenCV.git

```

Go to the project directory

```bash
cd Face-Detection-Using-OpenCV
```

Install dependencies

```bash
pip install opencv-python numpy
```

Run the script

```bash
python face_detection.py
```


## How It Works

-Webcam Capture: The script captures video from the default webcam using cv2.VideoCapture(0).

-Haar Cascade Classifier: A pre-trained Haar Cascade model is loaded (haarcascade_frontalface_default.xml) for face detection.

-Grayscale Conversion: The frame is converted to grayscale using cv2.cvtColor(), as face detection works better on grayscale images.

-Face Detection: The detectMultiScale() method detects faces, and rectangles are drawn around them using cv2.rectangle().

-Real-Time Display: The processed frame is displayed in a window, and it updates in real time.


## Output

![Screenshot (4)](https://github.com/user-attachments/assets/28394e58-1fd5-481a-8077-df71d8d86e91)


