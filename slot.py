class Slot:
    def __init__(self,max_s,min_s=0):
        self.max=max_s
        self.min=min_s

    def isValidEvent(self,event,totaltime):
        if event.duration>self.max or event.duration+totaltime>self.max:
            return False
        return True

    def isValidSession(self,totaltime):
        validsession=False
        if self.min:
            if totaltime<=self.max:
                validsession=True
        else:
            if totaltime==self.max:
                validsession=True 
        return validsession