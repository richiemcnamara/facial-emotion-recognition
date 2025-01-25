import cv2
from utils import detect_faces, analyze_emotion, draw_face_bounding_box, draw_emotion_text

frame_counter = 0  # Counter for periodic analysis
bounding_box = None  # Store the bounding box for the face
emotion_label = None  # Store the detected emotion
emotion_confidence = None  # Store the confidence level of the emotion

def analyze_frame(frame):
    """
    Process the input frame to detect faces, analyze emotions, and display the results.

    This function detects faces in the frame, analyzes the emotion of the first detected face, 
    and draws the bounding box and emotion label with confidence on the frame.

    Parameters
    ----------
    frame : numpy.ndarray
        The input frame (image) from the camera, expected to be in BGR format 
        (height x width x 3).

    Returns
    -------
    None
        The function modifies the input frame by drawing the face bounding box and 
        emotion label with confidence, and displays it in a window.
    
    Notes
    -----
    The emotion analysis is performed every 5th frame to reduce processing time.
    The function also handles errors and prints any exceptions encountered during analysis.
    """
    global bounding_box, emotion_label, emotion_confidence, frame_counter

    try:
        if frame_counter % 5 == 0:
            faces = detect_faces(frame)
            
            if len(faces) > 0:
                x, y, w, h = faces[0]
                bounding_box = (x, y, w, h)
                
                face_region = frame[y:y + h, x:x + w]
                result = analyze_emotion(face_region)
                
                if result:
                    emotion_label = result[0].get('dominant_emotion', "Unknown")
                    emotion_confidence = result[0].get('emotion', {}).get(emotion_label, 0)

        frame_counter += 1

    except Exception as e:
        print(f"Error during emotion analysis: {e}")

    draw_face_bounding_box(frame, bounding_box)
    draw_emotion_text(frame, bounding_box, emotion_label, emotion_confidence)
    
    cv2.imshow('Camera', frame)


def capture_frame(cap):
    """
    Capture frames from the camera and process them for emotion analysis.

    This function continuously captures frames from the camera, processes each frame 
    to detect faces and analyze emotions, and then displays the resulting frame with 
    the bounding box and emotion label. The loop terminates when the 'q' key is pressed.

    Parameters
    ----------
    cap : cv2.VideoCapture
        The video capture object used to capture frames from the camera.

    Returns
    -------
    None
        The function continuously captures and processes frames in a loop. The loop
        terminates when the 'q' key is pressed.

    Notes
    -----
    If a frame cannot be grabbed, the function prints an error message and breaks the loop.
    """
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        analyze_frame(frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
