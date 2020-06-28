from PIL import Image, ImageDraw
import face_recognition


img = "unknown_faces/unknown2.jpg"

# Load image with unknown face
unknown_image = face_recognition.load_image_file(img)

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)

# Covert image to pil-format to draw on top of it
pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left) in face_locations:
    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=3)

del draw
pil_image.show()
