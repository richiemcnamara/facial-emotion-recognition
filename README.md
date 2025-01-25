# Emotion Detection and Face Bounding Box

This project utilizes a webcam feed to detect faces and analyze emotions using the DeepFace library. The system captures frames from the camera, detects faces using Haar cascades, analyzes the emotions of the detected faces, and displays the bounding boxes around the faces along with the detected emotion and confidence levels.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project processes real-time video captured from a webcam, detects faces, analyzes the emotions of the faces, and visualizes the results. It uses OpenCV for face detection and frame capture, while DeepFace is used for emotion analysis.

### Key Features

- Real-time face detection using Haar cascades.
- Emotion detection using DeepFace's pre-trained models.
- Draw bounding boxes around detected faces.
- Display the dominant emotion and its confidence level.
- Efficient frame processing by analyzing every 5th frame.

## Features

- **Face Detection**: The project uses OpenCV's Haar cascade classifier to detect faces in the video frames.
- **Emotion Analysis**: DeepFace analyzes the emotion of the detected faces, and the dominant emotion along with its confidence level is displayed on the screen.
- **Real-time Processing**: The project captures and processes video frames in real-time, displaying results immediately.
- **Optimized Performance**: The system analyzes every 5th frame to ensure efficient processing.

## Requirements

To run this project, you will need the following libraries:

- `opencv-python` for computer vision and frame capture.
- `deepface` for emotion detection.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/emotion-detection.git
   cd emotion-detection
