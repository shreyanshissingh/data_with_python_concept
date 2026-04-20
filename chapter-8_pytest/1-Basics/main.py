class Weather:
    def __init__(self, temp, rain_probability:float):
        self.temp = temp
        self.rain_probability = rain_probability

    def is_hot(self):
        if self.temp > 30:
            return True
        else:
            return False
        
    def is_rainy(self):
        if self.rain_probability > 0.5:
            return True
        else:
            return False