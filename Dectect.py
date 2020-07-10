# import libraries
from cv2 import cv2
import face_recognition
import threading
#import Sunday
def facedetect():

    video_capture = cv2.VideoCapture(0)
    image = face_recognition.load_image_file("./FileDetect/FaceID/Phuc.jpg")
    face_encoding = face_recognition.face_encodings(image)
   # image = face_recognition.load_image_file("./FileDetect/FaceID/obama.jpg")
   # face_encoding[1] = face_recognition.face_encodings(image)
    #image2 = face_recognition.load_image_file("./FileDetect/FaceID/Xhuy.jpg")
    #face_encoding2 = face_recognition.face_encodings(image2)[0]
    #image3 = face_recognition.load_image_file("./FileDetect/FaceID/Tam.jpg")
    #face_encoding3 = face_recognition.face_encodings(image3)[0]

    known_faces = [
    face_encoding,
    ]

    # Initialize variables
    face_locations = []
    face_encodings = []
    face_names = []

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)

        # Display the results
        face_names = []
        name = None
        name1 = None
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(known_faces,face_encoding,tolerance = 0.6)

            name = None
            if match[0]:
                name = "Phuc"
            if match[1]:
                name = "Obama"  
            else: name = ""
        #  else: name = "ERROR"
            face_names.append(name)
        
        

        for top, right, bottom, left in face_locations:
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)
        if name != None or name1!=None:
            if name !=None: return name
            else: return name1
        # Hit 'q' on the keyboard to quit!
#     if cv2.waitKey(1) & 0xFF == ord('q'):
   #         break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
g = threading.Thread(name='facedetect', target=facedetect)
g.setDaemon(True)
g.start()