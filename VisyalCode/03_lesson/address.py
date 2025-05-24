class Address:
    def __init__(self, index, sity, stret, hous, apt ):
        self.index = index
        self.sity = sity
        self.stret = stret
        self.hous = hous    
        self.apt = apt
    def __str__(self):
        return f"{self.index} {self.sity}, {self.stret}, {self.hous}, {self.apt}"