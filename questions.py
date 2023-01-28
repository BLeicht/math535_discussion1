import colorchannels as colorchannels

def main():
    #questionOne()
    #questionTwo()
    #questionThree()
    questionFour()
    #questionFive()

def questionOne():
    colorchannels.displayImage("./Ondra_sampling.jpg")

    colorchannels.separateColorChannels("./Ondra_sampling.jpg")
    colorchannels.displayImage("./Ondra_red.jpg")    
    colorchannels.displayImage("./Ondra_green.jpg")    
    colorchannels.displayImage("./Ondra_blue.jpg") 


def questionTwo():
    colorchannels.grayifyImage("./Ondra_sampling.jpg")
    colorchannels.displayImage("./Ondra_gray.jpg")
    colorchannels.bitPlaneSlicing("./Ondra_gray.jpg") 


def questionThree():
    colorchannels.intensityProfile("./Ondra_gray.jpg")

def questionFour():
    colorchannels.histogramMakerRGB("./Ondra_sampling.jpg")


def questionFive():
    colorchannels.addImages("./Ondra_red.jpg", "./Ondra_blue.jpg")
    colorchannels.xorImages("./Ondra_sampling.jpg", "./Ondra_green.jpg")
    colorchannels.bitShiftRightOne("./Ondra_sampling.jpg")

