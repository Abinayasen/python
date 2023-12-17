import math
import cv2
import numpy as np
from keras.models import load_model
from cvzone.HandTrackingModule import HandDetector

model = load_model('/cnn8grps_rad1_model.h5')
white = np.ones((400, 400, 3), np.uint8) * 255
cv2.imwrite("C:\\Users\\devansh raval\\PycharmProjects\\pythonProject\\white.jpg", white)

capture = cv2.VideoCapture(0)

hd = HandDetector(maxHands=1)
hd2 = HandDetector(maxHands=1)

offset = 29

def draw_lines(white, points, offset):
    os = ((400 - w) // 2) - 15
    os1 = ((400 - h) // 2) - 15
    for t in range(0, 4, 1):
        cv2.line(white, (points[t][0] + os, points[t][1] + os1), (points[t + 1][0] + os, points[t + 1][1] + os1), (0, 255, 0), 3)
    # Add similar lines drawing for other ranges

while True:
    try:
        _, frame = capture.read()
        frame = cv2.flip(frame, 1)
        hands = hd.findHands(frame, draw=False, flipType=True)

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            image = frame[y - offset:y + h + offset, x - offset:x + w + offset]
            white = cv2.imread("C:\\Users\\devansh raval\\PycharmProjects\\pythonProject\\white.jpg")

            handz = hd2.findHands(image, draw=False, flipType=True)

            if handz:
                hand = handz[0]
                pts = hand['lmList']

                draw_lines(white, pts, offset)

                cv2.imshow("2", white)

                white = white.reshape(1, 400, 400, 3)
                prob = np.array(model.predict(white)[0], dtype='float32')
                ch1 = np.argmax(prob, axis=0)
                prob[ch1] = 0
                ch2 = np.argmax(prob, axis=0)
                prob[ch2] = 0
                ch3 = np.argmax(prob, axis=0)
                prob[ch3] = 0

                pl = [ch1, ch2]

                # Continue with your conditions...
                # ...
                
    except Exception as e:
        traceback.print_exc()

