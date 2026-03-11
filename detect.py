from ultralytics import YOLO
import cv2
import time

model = YOLO("runs/detect/train/weights/best.pt")

cap = cv2.VideoCapture(0)

prev_time = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, conf=0.6)

    detected = False

    for r in results:

        for box in r.boxes:

            x1,y1,x2,y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            if conf > 0.6:

                detected = True

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)

                label = f"PAN CARD {conf:.2f}"

                cv2.putText(frame,label,
                            (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,(0,255,0),2)

                card = frame[y1:y2, x1:x2]

                cv2.imwrite("output/pancard.jpg",card)

    if not detected:
        cv2.putText(frame,"NOT PAN CARD",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,(0,0,255),2)

    curr_time = time.time()
    fps = 1/(curr_time-prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    cv2.putText(frame,f"FPS: {int(fps)}",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,(255,255,0),2)

    cv2.imshow("PAN CARD DETECTOR",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()