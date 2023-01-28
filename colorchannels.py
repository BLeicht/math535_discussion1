from PIL import Image
import numpy as np
from skimage.measure import profile_line
from skimage import io, exposure
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
    print("Slicing bit planes, one sec!\n")

    image = io.imread(filePath, as_gray=True)

    bitPlane = [np.zeros((808, 1010))]
    for i in range(7):
        bitPlane.append(np.zeros((808, 1010)))

    for rows in range(np.shape(image)[0]):
        for cols in range(np.shape(image)[1]):
            binaryNum = format(image[rows][cols], '#010b')
            for i in range(8):
                bitPlane[i][rows][cols] = binaryNum[i+2]*255

    for i in range(8):
        plane = Image.fromarray(bitPlane[i])
        plane.show()

# gives the intensity profile of a line from a given image
def intensityProfile(filePath):
    image = io.imread(filePath, as_gray=True)
    
    p = profile_line(image, (460, 140), (872, 457))
    
    plt.plot(p)
    plt.ylabel('intensity')
    plt.xlabel('line path')
    plt.show()

def histogramMaker(filePath):
    image = io.imread(filePath)

    colors = ("red", "green", "blue")

    plt.figure()
    plt.xlim([0, 256])

    for channel_id, color in enumerate(colors):
        histogram, bin_edges = np.histogram(image[:, :, channel_id], bins=256, range=(0, 256))
        plt.plot(bin_edges[0:-1], histogram, color=color)


    plt.title("Color histogram")
    plt.xlabel("Color value")
    plt.ylabel("Pixel count")

    plt.show() 


def addImages(filePathOne, filePathTwo):
    imageOne = io.imread(filePathOne, as_gray=True)
    imageTwo = io.imread(filePathTwo, as_gray=True)

    outputImage = np.add(imageOne, imageTwo)
    Image.fromarray(outputImage).show()
    return outputImage

def subImages(filePathOne, filePathTwo):
    imageOne = io.imread(filePathOne, as_gray=True)
    imageTwo = io.imread(filePathTwo, as_gray=True)

    outputImage = np.subtract(imageOne, imageTwo)
    Image.fromarray(outputImage).show()
    return outputImage

def multiplyImages(filePathOne, filePathTwo):
    imageOne = io.imread(filePathOne, as_gray=True)
    imageTwo = io.imread(filePathTwo, as_gray=True)

    outputImage = np.multiply(imageOne, imageTwo)
    Image.fromarray(outputImage).show()
    return outputImage


def andImages(filePathOne, filePathTwo):
    imageOne = io.imread(filePathOne, as_gray = True)
    imageTwo = io.imread(filePathTwo, as_gray = True)

    outputImage = nnp.logical_and(imageOne, imageTwo)
    Image.fromarray(outputImage).show()    
    return outputImage

def xorImages(filePathOne, filePathTwo):
    imageOne = io.imread(filePathOne, as_gray=True)
    imageTwo = io.imread(filePathTwo, as_gray=True)
     
    outputImage = np.logical_xor(imageOne, imageTwo)
    
    Image.fromarray(outputImage).show()

    return outputImage
