import cv2
import mediapipe as mp
import numpy as np

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def draw_finger_style_hand(image, hand_landmarks):
    h, w = image.shape[:2]
    
    fingers = [
        [(0, 1), (1, 2), (2, 3), (3, 4)],  
        [(0, 5), (5, 6), (6, 7), (7, 8)],   
        [(0, 9), (9, 10), (10, 11), (11, 12)],  
        [(0, 13), (13, 14), (14, 15), (15, 16)],  
        [(0, 17), (17, 18), (18, 19), (19, 20)]  
    ]
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]
    
    for finger, color in zip(fingers, colors):
        for start, end in finger:
            start_point = (int(hand_landmarks.landmark[start].x * w), 
                           int(hand_landmarks.landmark[start].y * h))
            end_point = (int(hand_landmarks.landmark[end].x * w), 
                         int(hand_landmarks.landmark[end].y * h))
            
            cv2.line(image, start_point, end_point, color, 8)
            
            cv2.circle(image, start_point, 5, (255, 255, 255), -1)
            cv2.circle(image, end_point, 5, (255, 255, 255), -1)
    
    palm_points = [0, 5, 9, 13, 17]
    palm_pts = np.array([(int(hand_landmarks.landmark[idx].x * w), 
                          int(hand_landmarks.landmark[idx].y * h)) for idx in palm_points], np.int32)
    cv2.polylines(image, [palm_pts], True, (255, 255, 255), 2)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    image = np.zeros_like(frame)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_results = face_detection.process(frame_rgb)

    hand_results = hands.process(frame_rgb)

    if face_results.detections:
        for detection in face_results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(image, bbox, (0, 255, 0), 2)

    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            draw_finger_style_hand(image, hand_landmarks)

    cv2.imshow('Finger Style Hand and Face Tracking', image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

