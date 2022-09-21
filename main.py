from readVideo import getFrame, getNumFrames, getFramerate
from createImage import getDimensions, loadAndAverage, constructImage
import sys


# ===== Progress bar ===========================================================


# Thanks https://stackoverflow.com/questions/3160699/python-progress-bar
def progressBar(it, prefix="", size=60, out=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count),
              end='\r', file=out, flush=True)

    show(0)

    for i, item in enumerate(it):
        yield item
        show(i+1)

    print("\n", flush=True, file=out)


# ===== Main ===================================================================


# Driver code
if __name__ == "__main__":
    # Put your input filename here
    filename = "beemovie"

    filepathIn = "in/" + filename + ".mp4"  # CHANGE THIS if different filetype
    filepathOut = "out/" + filename + ".png"

    procImagePath = f"proc/frame.png"

    # Compute dimensions of the video
    print("Computing dimensions...")
    frameCount = getNumFrames(filepathIn)
    framerate = getFramerate(filepathIn)
    print(f"Framecount: {frameCount}, framerate: {framerate}")
    dims = getDimensions(frameCount)
    print(f"Dimensions received. W{dims[0]} x H{dims[1]}")

    # Read the video for RGB tuples
    print(f"Video read. Processing images...")
    rgbTuples = []
    seconds = 0
    for i in progressBar(range(frameCount), "Image progress: ", 40):
        # Get the frame and save it to the disk
        getFrame(filepathIn, seconds)
        # Save the image path
        rgbTuples.append(loadAndAverage(procImagePath))

        # Increment the seconds
        seconds += framerate

    # Construct the image
    print(f"Images processed. Constructing image...")
    constructImage(rgbTuples, dims, filepathOut)
