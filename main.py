from readVideo import getNumFrames, readVideo
from createImage import getDimensions, constructImage


# Driver code
if __name__ == "__main__":
    # Put your input filename here
    filename = "beemovie.mp4"

    filepathIn = "in/" + filename + ".mp4"  # CHANGE THIS if different filetype
    filepathOut = "out/" + filename + ".png"

    # Compute dimensions of the video
    frameCount = getNumFrames(filepathIn)
    dims = getDimensions(frameCount)

    # Read the video for RGB tuples
    rgbTuples = readVideo(filepathIn)

    # Construct the image
    constructImage(rgbTuples, dims, filepathOut)
