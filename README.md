# Emotion Detection and Face Bounding Box

This project utilizes a webcam feed to detect faces and analyze emotions using the DeepFace library. The system captures frames from the camera, detects faces using Haar cascades, analyzes the emotions of the detected faces, and displays the bounding boxes around the faces along with the detected emotion and confidence levels.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Overview

This project processes real-time video captured from a webcam, detects faces, analyzes the emotions of the faces, and visualizes the results. It uses OpenCV for face detection and frame capture, while DeepFace is used for emotion analysis.

## Features

- **Face Detection**: The project uses OpenCV's Haar cascade classifier to detect faces in the video frames.
- **Emotion Analysis**: DeepFace analyzes the emotion of the detected faces, and the dominant emotion along with its confidence level is displayed on the screen.
- **Real-time Processing**: The project captures and processes video frames in real-time, displaying results immediately.
- **Optimized Performance**: The system analyzes every 5th frame to ensure efficient processing.

## Requirements

To run this project, you will need the following libraries:

- `opencv-python` for computer vision and frame capture.
- `deepface` for emotion detection.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/emotion-detection.git
   cd emotion-detection
   ```
   
2. **Install dependencies**:

   You can install the required dependencies using `pip` by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

   This will install all necessary libraries listed in the `requirements.txt` file.

3. **Install DeepFace dependencies** (if needed):

   Depending on your environment, you may need to install some additional dependencies for DeepFace. You can do this by following the instructions provided by DeepFace's documentation. Usually, you will need to install `tensorflow` and `keras`:

   ```bash
   pip install tensorflow
   pip install keras
   ```

## Usage

1. **Run the project**:

   To start the application, run the `main.py` script. This will initialize the camera capture and start processing the frames.

   ```bash
   python main.py
   ```

2. **Exit the program**:

   Press the 'q' key to exit the camera feed and close the application.

3. **Expected Behavior**:

   The program will:
   - Open the webcam and start capturing video.
   - Detect faces in each frame.
   - Analyze the emotion of the detected faces using DeepFace.
   - Draw bounding boxes around detected faces.
   - Display the detected emotion and its confidence level.
   
   The program will continue until the 'q' key is pressed.

## File Structure

```
emotion-detection/
│
├── main.py            # Entry point to start the capture and analysis process.
├── capture.py         # Contains functions for capturing frames and analyzing them.
├── utils.py           # Contains helper functions for face detection, emotion analysis, and drawing results.
├── requirements.txt   # File that lists all required dependencies for the project.
└── README.md          # This README file.
```
