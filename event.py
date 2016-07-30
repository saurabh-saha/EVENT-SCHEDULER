class Event:
    def __init__(self,name,duration):
        self.name=name
        self.duration=duration
        self.scheduled=False

    def __repr__(self):
        return self.name