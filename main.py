import colorchannels as colorchannels

def main():
    #Question 1
    colorchannels.displayImage("./Ondra_sampling.jpg")
    
    colorchannels.separateColorChannels("./Ondra_sampling.jpg")
    colorchannels.displayImage("./Ondra_red.jpg")    
    colorchannels.displayImage("./Ondra_green.jpg")    
    colorchannels.displayImage("./Ondra_blue.jpg") 

    #Question 2
    colorchannels.grayifyImage("./Ondra_sampling.jpg")
    colorchannels.displayImage("./Ondra_grayscale.jpg")

if __name__ == "__main__":
    main()
