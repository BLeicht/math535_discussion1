import colorchannels as colorchannels

def main():
    questionOne()
    questionTwo()
    questionThree()
    #questionFour()
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

def questionThree():
    colorchannels.intensityProfile("./Ondra_gray.jpg")
