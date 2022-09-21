from readVideo import getNumFrames, readVideo
from createImage import getDimensions, constructImage


# Driver code
if __name__ == "__main__":
    # Put your input filename here
    filename = "beemovie"

    filepathIn = "in/" + filename + ".mp4"  # CHANGE THIS if different filetype
    filepathOut = "out/" + filename + ".png"

    # Compute dimensions of the video
    print("Computing dimensions...")
    frameCount = getNumFrames(filepathIn)
    dims = getDimensions(frameCount)
    print(f"Dimensions received. W{dims[0]} x H{dims[1]}")

    # Read the video for RGB tuples
    print(f"Reading video...")
    rgbTuples = readVideo(filepathIn)

    # Construct the image
    constructImage(rgbTuples, dims, filepathOut)
