from ultralytics import YOLO

def train_model():

    # Load pretrained YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
        data="data.yaml",
        epochs=10,
        imgsz=640
    )

if __name__ == "__main__":
    train_model()