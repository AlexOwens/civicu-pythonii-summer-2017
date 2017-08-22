class SpaceAge:
    
    def __init__(self, seconds):
       self.seconds = seconds
       
    def on_earth(self):
        seconds = self.seconds/(31557600)
        return round(seconds, 2)
    def on_mercury(self):
        seconds = self.seconds/(31557600*0.2408467)
        return round(seconds, 2)
    def on_venus(self):
        seconds = self.seconds/(31557600*0.61519726)
        return round(seconds, 2)
    def on_mars(self):
        seconds = self.seconds/(31557600*1.8808158)
        return round(seconds, 2)
    def on_jupiter(self):
        seconds = self.seconds/(31557600*11.862615)
        return round(seconds, 2)
    def on_saturn(self):
        seconds = self.seconds/(31557600*29.447498)
        return round(seconds, 2)
    def on_uranus(self):
        seconds = self.seconds/(31557600*84.016846)
        return round(seconds, 2)
    def on_neptune(self):
        seconds = self.seconds/(31557600*164.79132)
        return round(seconds, 2)

