import cv2
from deepface import DeepFace

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame):
    """
    Detect faces in the input frame and return the bounding boxes

    Parameters
    ----------
    frame : numpy.ndarray
        The input frame (image) in which to detect faces. The frame is expected 
        to be a color image in BGR format (height x width x 3).

    Returns
    -------
    faces : list of tuple
        A list of bounding boxes, where each bounding box is a tuple (x, y, w, h)
        representing the top-left corner (x, y) and width (w), height (h) of the detected face.
    """
     
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def analyze_emotion(face_region):
    """
    Analyze the emotion of a given face region using DeepFace.

    Parameters
    ----------
    face_region : numpy.ndarray
        The region of the frame containing the detected face. The region is expected 
        to be a cropped image from the original frame.

    Returns
    -------
    result : dict
        A dictionary containing the analysis result, with the dominant emotion and its confidence.
        Example structure:
        {
            'dominant_emotion': 'happy',
            'emotion': {
                'happy': 0.95,
                'sad': 0.03,
                'surprise': 0.01,
                ...
            }
        }
    """
    result = DeepFace.analyze(
        img_path=face_region,
        actions=['emotion'],
        enforce_detection=False
    )
    return result

def draw_face_bounding_box(frame, bounding_box):
    """"
    Draw a bounding box around the detected face in the frame.

    Parameters
    ----------
    frame : numpy.ndarray
        The frame (image) where the bounding box will be drawn. It is modified in place.

    bounding_box : tuple
        A tuple (x, y, w, h) representing the coordinates and size of the bounding box.
        - (x, y) is the top-left corner.
        - (w, h) is the width and height of the bounding box.

    Returns
    -------
    None
    """
    if bounding_box:
        x, y, w, h = bounding_box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

def draw_emotion_text(frame, bounding_box, emotion_label, emotion_confidence):
    """
    Draw the emotion label and confidence text on the frame.

    Parameters
    ----------
    frame : numpy.ndarray
        The frame (image) where the text will be drawn. It is modified in place.

    bounding_box : tuple
        A tuple (x, y, w, h) representing the coordinates and size of the face bounding box.
        
    emotion_label : str
        The detected emotion label (e.g., 'happy', 'sad').

    emotion_confidence : float
        The confidence level of the detected emotion, in the range [0, 100].

    Returns
    -------
    None
    """
    if bounding_box and emotion_label:
        x, y, w, h = bounding_box
        emotion_text = emotion_label.upper()
        confidence_text = f"({emotion_confidence:.1f}%)"
        
        (emotion_text_width, emotion_text_height), _ = cv2.getTextSize(emotion_text, cv2.FONT_HERSHEY_SIMPLEX, 1.25, 3)
        (confidence_text_width, confidence_text_height), _ = cv2.getTextSize(confidence_text, cv2.FONT_HERSHEY_SIMPLEX, 0.75, 2)
        
        background_rect_width = min(emotion_text_width + confidence_text_width + 30, w)
        background_rect_height = max(emotion_text_height, confidence_text_height) + 20
        center_x = x + (w // 2)
        start_x = center_x - (background_rect_width // 2)
        
        cv2.rectangle(
            frame,
            (start_x, y - background_rect_height - 15),
            (start_x + background_rect_width, y),
            (0, 0, 0),
            -1
        )
        
        cv2.putText(frame, emotion_text, (start_x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (255, 255, 255), 3)
        cv2.putText(frame, confidence_text, (start_x + 10 + emotion_text_width + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
