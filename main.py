import colorchannels as colorchannels

def main():
    colorchannels.displayImage("./Ondra_sampling.jpg")
    
    colorchannels.separateColorChannels("./Ondra_sampling.jpg")
    colorchannels.displayImage("./Ombra_red.jpg")    
    colorchannels.displayImage("./Ombra_green.jpg")    
    colorchannels.displayImage("./Ombra_blue.jpg") 

if __name__ == "__main__":
    main()
