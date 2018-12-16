#!/usr/bin/python3
# -*- coding: utf8 -*-
# -*- date: 2018/12/14 -*-

import face_recognition
from PIL import Image, ImageDraw

# 将图片加载成numpy格式
MJ = face_recognition.load_image_file("./Resource/MJ.jpg")
Picasso = face_recognition.load_image_file("./Resource/Picasso.jpg")
Mona_Lisa = face_recognition.load_image_file("./Resource/Mona_Lisa.jpg")
unknown = face_recognition.load_image_file("./Resource/unknown.jpg")

# 通过face_recognition.face_encodings获取图片中的第一个人脸
Mona_Lisa_face_encoding = face_recognition.face_encodings(Mona_Lisa)[0]
MJ_face_encoding = face_recognition.face_encodings(MJ)[0]
Picasso_face_encoding = face_recognition.face_encodings(Picasso)[0]
unknown_face_encoding = face_recognition.face_encodings(unknown)

known_face_encodings = [
    Picasso_face_encoding,
    Mona_Lisa_face_encoding,
    MJ_face_encoding,
]

known_face_names = [
    "Picasso's face",
    "Mona Lisa's face",
    "MJ's face",
]


# 检测未知图片中的人脸与已知人物进行对比
results_0 = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding[0])
print("\nKnown faces are \n\n>>>\n %s \n>>>\n"%known_face_names)

isRecognized = False
#开始对比识别
for i in range(len(results_0)):
	if(results_0[i]):
		isRecognized = True
		print("Unknown face is %s."%known_face_names[i])
#未识别
if(isRecognized == False):
	print("Unknown face is still unknown!")
	
# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown)
face_encodings = face_recognition.face_encodings(unknown, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()

# You can also save a copy of the new image to disk if you want by uncommenting this line
# pil_image.save("image_with_boxes.jpg")
