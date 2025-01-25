import cv2
from capture import capture_frame

def main():
    """
    Start the camera capture and processing loop.

    This function initializes the camera capture using `cv2.VideoCapture(0)` and then 
    enters the capture loop, where frames are captured from the camera and processed 
    using the `capture_frame` function. The loop will continue until the user presses 
    the 'q' key to exit.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The function starts the camera capture loop and processes frames. The loop 
        continues until the 'q' key is pressed.
    
    Notes
    -----
    If the camera cannot be initialized, an error message may be displayed.
    """
    cap = cv2.VideoCapture(0)
    capture_frame(cap)

if __name__ == "__main__":
    main()
