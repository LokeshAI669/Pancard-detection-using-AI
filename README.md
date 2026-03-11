##### PAN Card Detection using AI
Project Overview

This project is an AI-based PAN Card Detection System built using YOLO (Ultralytics) and OpenCV.
The system detects a PAN card in real-time using a webcam and draws a bounding box around the detected card with a confidence score.

It can also crop and save the detected PAN card image automatically.

This project demonstrates how Computer Vision and Deep Learning models can be integrated with real-time camera systems.


Demo Output

Example output when the PAN card is detected:
Bounding box around the PAN card
Confidence score displayed
FPS counter for performance


Technologies Used

Python
YOLO (Ultralytics)
OpenCV
Deep Learning
Computer Vision


This project uses the YOLO Object Detection Model.
Model details:
Model: YOLO (Ultralytics)
Training framework: PyTorch
Custom trained dataset for PAN Card detection


Project Workflow
Camera Input
     ↓
YOLO Model Detection
     ↓
Bounding Box Around PAN Card
     ↓
Confidence Score Display
     ↓
Crop Detected PAN Card
     ↓
Save Image to Output Folder



Requirements
Required Python libraries:
- ultralytics
- opencv-python
- numpy


Features
- Real-time PAN card detection
- Bounding box visualization
- Confidence score display
- Automatic cropped image saving
- FPS display for performance monitoring
