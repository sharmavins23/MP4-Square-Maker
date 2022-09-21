import cv2  # OpenCV for frame count


# ===== Video metadata processing ==============================================


# Get a video's number of frames
def getNumFrames(filepath):
    # Hoping this doesn't take 15 years
    capture = cv2.VideoCapture(filepath)

    # Get the total number of frames
    length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    return length


# Get a video's framerate
def getFramerate(filepath):
    capture = cv2.VideoCapture(filepath)
    framerate = capture.get(cv2.CAP_PROP_FPS)
    return framerate


# ===== Video processing =======================================================


# Get a particular frame from a video and save it to a file
def getFrame(filepath, seconds):
    capture = cv2.VideoCapture(filepath)

    capture.set(cv2.CAP_PROP_POS_MSEC, seconds * 1000)
    hasFrames, image = capture.read()
    if hasFrames:
        outputFilename = f"proc/frame.png"
        cv2.imwrite(outputFilename, image)
