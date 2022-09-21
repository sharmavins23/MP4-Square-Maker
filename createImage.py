import math
from PIL import Image


# ===== Image metadata =========================================================


# Get the image's dimensions
def getDimensions(frameCount):
    # Get the image's dimensions
    width = math.floor(math.sqrt(frameCount))
    height = math.ceil(frameCount / width)
    dims = (width, height)

    return dims


# ===== Image loading ==========================================================


# Load an image from a file and compute its average RGB value
def loadAndAverage(filepath):
    img = Image.open(filepath)
    width, height = img.size

    # Iterate through the image and compute the average RGB value
    rTotal = 0
    gTotal = 0
    bTotal = 0
    for i in range(width):
        for j in range(height):
            # Get the pixel value
            rgbTuple = img.getpixel((i, j))

            # Add the RGB values to the total
            rTotal += rgbTuple[0]
            gTotal += rgbTuple[1]
            bTotal += rgbTuple[2]

    # Compute the average RGB value
    rAvg = rTotal / (width * height)
    gAvg = gTotal / (width * height)
    bAvg = bTotal / (width * height)

    # Return the average RGB value as a tuple
    return (rAvg, gAvg, bAvg)


# ===== Image construction =====================================================


# Construct the image
def constructImage(rgbTuples, dims, filepath):
    # Unpack dimensions tuple
    width, height = dims

    # Create the image
    img = Image.new("RGB", (width, height))

    # Iterate through the image and set the pixel values
    for i in range(width):
        for j in range(height):
            # Compute the index of the pixel
            pixelIndex = (i * width) + j

            # Check if the pixel index is out of bounds
            if pixelIndex >= len(rgbTuples):
                rgbTuple = (0, 0, 0)
            else:
                # Get the pixel value
                rgbTuple = rgbTuples[i * width + j]

            # Set the pixel value
            img.putpixel((i, j), rgbTuple)

    # Save the image
    img.save(filepath)
