#!/usr/bin/python3
# -*- coding: utf8 -*-
# -*- date: 2018/12/14 -*-

import face_recognition

# 将图片加载成numpy格式
MJ = face_recognition.load_image_file("./MJ.jpg")
Picasso = face_recognition.load_image_file("./Picasso.jpg")
Mona_Lisa = face_recognition.load_image_file("./Mona_Lisa.jpg")
unknown = face_recognition.load_image_file("./unknown.jpg")

# 通过face_recognition.face_encodings获取图片中的第一个人脸
Mona_Lisa_face_encoding = face_recognition.face_encodings(Mona_Lisa)[0]
MJ_face_encoding = face_recognition.face_encodings(MJ)[0]
Picasso_face_encoding = face_recognition.face_encodings(Picasso)[0]
unknown_face_encoding = face_recognition.face_encodings(unknown)

known_faces = [
    Picasso_face_encoding,
    Mona_Lisa_face_encoding,
    MJ_face_encoding,
]

known_faces_str = [
    "Picasso's face",
    "Mona Lisa's face",
    "MJ's face",
]

# 检测未知图片中的人脸与已知人物进行对比
results_0 = face_recognition.compare_faces(known_faces, unknown_face_encoding[0])
print("\nKnown faces are \n\n>>>\n %s \n>>>\n"%known_faces_str)

isRecognized = False
#开始对比识别
for i in range(len(results_0)):
	if(results_0[i]):
		isRecognized = True
		print("Unknown face is %s."%known_faces_str[i])
#未识别
if(isRecognized == False):
	print("Unknown face is still unknown!")