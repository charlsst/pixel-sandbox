import random
import colorsys

class Particle :
    def __init__(self) :
        self.colour = self.randomise_colour((194, 178, 128))

    def getColour(self) :
        return self.colour

    def randomise_colour(self, base_colour_rgb : tuple[int,int,int]) :
        base_colour_hsv = colorsys.rgb_to_hsv(base_colour_rgb[0]/255, base_colour_rgb[1]/255, base_colour_rgb[2]/255)
        base_colour_hsv = (base_colour_hsv[0] + random.uniform(-0.01, 0.01),
                           base_colour_hsv[1] + random.uniform(-0.1, 0.1),
                           base_colour_hsv[2] + random.uniform(-0.1, 0.1))
        red, green, blue = colorsys.hsv_to_rgb(base_colour_hsv[0], base_colour_hsv[1], base_colour_hsv[2])
    
        red = max(0, min(1, red))
        green = max(0, min(1, green))
        blue = max(0, min(1, blue))

        return int(red * 255), int(green * 255), int(blue * 255)

