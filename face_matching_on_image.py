
import os
from PIL import Image, ImageDraw
from PIL import ImageFont
import face_recognition
import numpy as np

known_faces_encodings = []
known_names = []

# loop threw files in the known image directory and select jpg and png
for img in os.listdir("known_faces"): 
    if img.endswith(".jpg") or img.endswith(".png"):
        # Load image with unknown face
        image = face_recognition.load_image_file("known_faces/" + img)

        #Encode face from image and add encodings and nasme to lists
        img_encoding = face_recognition.face_encodings(image)[0]
        known_faces_encodings.append(img_encoding)
        known_names.append(img.split(".")[0])


img = "unknown_faces/unknown2.jpg"
# Load image with unknown face
unknown_image = face_recognition.load_image_file(img)

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Covert image to pil-format to draw on top of it
pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_faces_encodings, face_encoding)

    name = "Unknown"

    face_distances = face_recognition.face_distance(known_faces_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_names[best_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=3)

    # Draw a label with a name below the face     
    font = ImageFont.truetype("arial.ttf", 20)
    draw.text((left-5, bottom + 5), name, fill=(0, 255, 0, 0), font=font)

del draw
pil_image.show()


