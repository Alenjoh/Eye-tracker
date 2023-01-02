# *Scrolling Via Eye-Tracking* 


This code uses computer vision to track the position of a user's eyes and control the scrolling of a document. It captures video from the user's webcam and uses dlib's facial landmarks detector to locate the eyes. The code then compares the vertical position of the eyes to predefined upper and lower thresholds, and scrolls the document up or down accordingly.

This can be useful for users who prefer to navigate documents using eye movements, or who have mobility impairments that make it difficult to use a mouse or touchpad.

### *Requirements*

To use this code, you will need the following software and libraries installed on your computer:
```
Python 3
OpenCV (for capturing video and processing images)
dlib (for detecting facial landmarks)
pyautogui (for simulating mouse actions)
```
## *Usage*
```
Download or clone this repository.
Make sure you have all of the required libraries installed.
Run the code using python eye_tracking_scrolling.py.
The code will open a window showing the video capture from your webcam.
```
When you look above the center of the screen, the document will scroll up. When you look below the center of the screen, the document will scroll down.

## *Customization*

You can customize the scrolling speed and sensitivity by adjusting the values of the a and b variables in the code. These variables define the upper and lower thresholds for the vertical position of the eyes. You can also customize the size of the scrolling steps by adjusting the value
