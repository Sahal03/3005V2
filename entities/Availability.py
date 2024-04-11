class Availability:
    def __init__(self,day,start,end):
        self.day = day
        self.start = start
        self.end = end

    def isAvailable(self,day,start,end):
        if day!=self.day:
            return False
        if start>=self.start and end<=self.end:
            return True
        return False