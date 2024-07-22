Real-Time Hand Gesture Recognition: Uses MediaPipe and OpenCV for detecting hand gestures.
Video Capture: Accesses the default camera using cv2.VideoCapture(0).
Hand Landmark Detection: Detects hand landmarks with MediaPipe's Hands module.
Drawing and Bounding Box: Draws landmarks and a bounding box around the detected hand.
Gesture Recognition (commented): Includes logic for detecting gestures (e.g., pointing up or down) and simulating key presses with pyautogui.
Dependencies: Requires opencv-python, pyautogui, and mediapipe packages.
Exit: Press 'q' to quit the application.
