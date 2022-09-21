import cv2  # OpenCV for frame count


# ===== Video metadata processing ==============================================


# Get a video's number of frames
def getNumFrames(filepath):
    # Hoping this doesn't take 15 years
    capture = cv2.VideoCapture(filepath)

    # Get the total number of frames
    length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    return length


# ===== Video processing =======================================================


# Compute the average pixel value of a particular frame
def getPixelFromFrame(frame):
    b, g, r = cv2.split(frame)

    # Compute the average red, green, and blue values
    avgR = sum(r) / len(r)
    avgG = sum(g) / len(g)
    avgB = sum(b) / len(b)

    # Return the average pixel value
    return (avgR, avgG, avgB)


# Iterate through a video and splice out frames
def readVideo(filepath):
    capture = cv2.videoCapture(filepath)

    rgbTuples = []

    while True:
        # Capture frame by frame
        ret, frame = capture.read()
        # Check if the frame was read correctly
        if not ret:
            print("Error reading frame (stream end?) Exiting...")
            break

        # HERE is where you handle frames as images simply

        # Compute the average pixel value of the frame
        rgbTuple = getPixelFromFrame(frame)
        rgbTuples.append(rgbTuple)

    # Release the capture
    capture.release()
    cv2.destroyAllWindows()

    return rgbTuples()
