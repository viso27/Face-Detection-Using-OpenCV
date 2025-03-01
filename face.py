import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Capture video from the webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()    
    if not ret:
        print("Failed to grab frame")
        break
    frame_resized = cv2.resize(frame, (640, 480))
    # Convert the image to grayscale for better accuracy
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Face Detection ', frame_resized)
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
