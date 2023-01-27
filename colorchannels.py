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


# splits the image into its bit planes
def bitPlaneSlicing(filePath):
    image = io.imread(filePath, as_gray=True)
    
    bitPlaneOne = np.zeros((808, 1010))
    bitPlaneTwo = np.zeros((808, 1010))
    bitPlaneThree = np.zeros((808, 1010))
    bitPlaneFour = np.zeros((808, 1010))
    bitPlaneFive = np.zeros((808, 1010))
    bitPlaneSix = np.zeros((808, 1010))
    bitPlaneSeven = np.zeros((808, 1010))
    bitPlaneEight = np.zeros((808, 1010))
    
    for rows in range(np.shape(image)[0]):
        for cols in range(np.shape(image)[1]):

            binaryNum = format(image[rows][cols], '#010b')


            bitPlaneOne[rows][cols] = binaryNum[2]*255
            bitPlaneTwo[rows][cols] = binaryNum[3]*255
            bitPlaneThree[rows][cols] = binaryNum[4]*255
            bitPlaneFour[rows][cols] = binaryNum[5]*255
            bitPlaneFive[rows][cols] = binaryNum[6]*255
            bitPlaneSix[rows][cols] = binaryNum[7]*255
            bitPlaneSeven[rows][cols] = binaryNum[8]*255
            bitPlaneEight[rows][cols] = binaryNum[9]*255

    plane = Image.fromarray(bitPlaneOne)
    plane.show()
    plane = Image.fromarray(bitPlaneTwo)
    plane.show()
    plane = Image.fromarray(bitPlaneThree)
    plane.show()
    plane = Image.fromarray(bitPlaneFour)
    plane.show()
    plane = Image.fromarray(bitPlaneFive)
    plane.show()
    plane = Image.fromarray(bitPlaneSix)
    plane.show()
    plane = Image.fromarray(bitPlaneSeven)
    plane.show()
    plane = Image.fromarray(bitPlaneEight)
    plane.show()

def intensityProfile(filePath):
    image = io.imread(filePath, as_gray=True)
    
    p = profile_line(image, (460, 140), (872, 457))
    
    plt.plot(p)
    plt.ylabel('intensity')
    plt.xlabel('line path')
    plt.show()
