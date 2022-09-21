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
