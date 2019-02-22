# import cv2
#
# video_full_path = "http://192.168.3.27:80"
# cap = cv2.VideoCapture(video_full_path)
# print cap.isOpened()
# frame_count = 1
# success = True
# while (success):
#     success, frame = cap.read()
#     print 'Read a new frame: ', success
#
#     params = []
#     # params.append(cv.CV_IMWRITE_PXM_BINARY)
#     params.append(1)
#     cv2.imwrite("video" + "_%d.jpg" % frame_count, frame, params)
#
#     frame_count = frame_count + 1
#
# cap.release()


import cv2
cap = cv2.VideoCapture("rtsp://admin:admin@192.168.3.27:554//Streaming/Channels/1")
ret,frame = cap.read()
while ret:
    ret,frame = cap.read()
    cv2.imshow("frame",ret)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()



# import cv2
# import numpy as np
#
# url = "rtsp://admin:admin@192.168.3.27/Streaming/Channels/1"
#
# cap = cv2.VideoCapture(url)
# cascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
# while True:
#     (ret, frame) = cap.read()
#     frame = cv2.flip(frame, 0)
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     rects = cascade.detectMultiScale(gray_frame, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
#     if len(rects) > 0:
#         for rect in rects:
#             x, y, w, h = rect
#             p1, p2 = (x, y), (x + w, y + h)
#             cv2.rectangle(frame, p1, p2, color=(0, 0, 255), thickness=2)
#     cv2.imshow("Video", frame)
#     cv2.waitKey(1)

