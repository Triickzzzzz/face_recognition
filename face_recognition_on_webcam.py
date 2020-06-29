from PIL import Image, ImageDraw, ImageFont
import face_recognition
from cv2 import cv2


# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)
process_this_frame = 0

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Search for every 2nd frame for stability
    if process_this_frame % 2 == 0:
        # Find all the faces in the frame of video
        face_locations = face_recognition.face_locations(rgb_frame)

    process_this_frame += 1

    # Loop through each face and draw box around the face
    for (top, right, bottom, left)  in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
