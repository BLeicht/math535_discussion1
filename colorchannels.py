from PIL import Image
import numpy as np
from skimage.measure import profile_line
from skimage import io
import matplotlib.pyplot as plt


# takes in image filepath and displays image in default viewer
def displayImage(filePath):
    image = Image.open(filePath)
    image.show()


# separates color channels of filepath image into rgb and saves them as Ondra_[red..blue]
def separateColorChannels(filePath):
    print("Separating color channels. One moment.\n")

    image = Image.open(filePath)
    image = np.asarray(image)
    
    redChannel = image.copy()
    greenChannel = image.copy()
    blueChannel = image.copy()

    for rows in range(image.shape[0]):
        for cols in range(image.shape[1]):
           redChannel[rows][cols][1] = 0
           redChannel[rows][cols][2] = 0

           greenChannel[rows][cols][0] = 0
           greenChannel[rows][cols][2] = 0

           blueChannel[rows][cols][0] = 0
           blueChannel[rows][cols][1] = 0

    redChannel = Image.fromarray(redChannel)
    greenChannel = Image.fromarray(greenChannel)
    blueChannel = Image.fromarray(blueChannel)
    
    redChannel.save("Ondra_red.jpg")
    greenChannel.save("Ondra_green.jpg")
    blueChannel.save("Ondra_blue.jpg")

# Creates the grayscale image of the image at the filepath
def grayifyImage(filePath):
    image = Image.open(filePath).convert("L")
    image.save("Ondra_gray.jpg")

def intensityProfile(filePath):
    image = io.imread("Ondra_gray.jpg", as_gray=True)
    
    p = profile_line(image, (460, 140), (872, 457))
    
    plt.plot(p)
    plt.ylabel('intensity')
    plt.xlabel('line path')
    plt.show()
