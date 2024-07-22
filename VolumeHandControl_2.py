import cv2
import pyautogui
import mediapipe as mp
import math

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.5)
mp_drawings = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    tipIds = [4, 8, 12, 16, 20]






    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            print(hand_landmarks)


            for id, lm in enumerate(hand_landmarks.landmark):
                draw = True
                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cv2.circle(frame, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
                cv2.circle(frame, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
                cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

                xList = []
                yList = []
                bbox = []
                lmList = []


                h,w,_=frame.shape
                pt1 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                pt2 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                x1, y1 = int(pt1.x*w),int(pt1.y*h)
                x2, y2 = int(pt2.x*w),int(pt2.y*h)
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                length = math.hypot(x2 - x1, y2 - y1)
                xList.append(cx)
                yList.append(cy)

                lmList.append([id, cx, cy])

                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                bbox = xmin, ymin, xmax, ymax

                if draw:


                 cv2.rectangle(frame, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                              (0, 255, 0), 2)





            mp_drawings.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            #index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            #thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

            #if index_finger_y < thumb_y:
             #   hand_gesture = 'Pointing Up'
              #  pyautogui.press('volumeup')
            #elif index_finger_y > thumb_y:
             #   hand_gesture = 'Pointing Down'
              #  pyautogui.press('volumedown')
            #else:
             #   hand_gesture = 'other'

            #cv2.putText(frame, hand_gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Hand Gesture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
