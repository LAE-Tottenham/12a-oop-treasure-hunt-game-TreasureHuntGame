class map():
    def __init__(self, name, location,xc,yc, locked=False):
        self.name = name
        self.location=location
        self.locked = locked
        self.items = []
        self.x= xc
        self.y=yc
        # add more atributes as needed
            
    def returnx(self):
        x=self.x
        return x
    def returny(self):
        y=self.y
        return y
    

    # add more methods as needed
