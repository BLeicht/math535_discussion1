from PIL import Image
import numpy as np

def displayImage(filePath):
    image = Image.open(filePath)
    image.show()

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
    
    redChannel.save("Ombra_red.jpg")
    greenChannel.save("Ombra_green.jpg")
    blueChannel.save("Ombra_blue.jpg")
