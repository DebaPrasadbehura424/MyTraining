import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open nahi ho raha!")
    exit()

print("Camera started...")
print("Press Q to quit")


while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera se frame nahi mila!")
        break

    results = model(frame, verbose=False)


    annotated_frame = results[0].plot()

    cv2.imshow(
        "YOLOv8 Object Detection",
        annotated_frame
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

print("Camera closed.")