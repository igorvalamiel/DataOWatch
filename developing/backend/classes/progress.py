from tools.time_dealing import Time, Seconds_to_Time

class Progress():
    def __init__(self, TYPE):
        self.INDEX = -1
        self.PROGRESS = -1
        
        if TYPE == ""


class Objective():
    def __init__(self):
        self.OBJECTIVE_INDEX = 0 #checkpoints
    
    def AddIndex(self):
        self.OBJECTIVE_INDEX += 1
    
    def GetIndex(self):
        return self.OBJECTIVE_INDEX



class Payload():
    def __init__(self):
        self.OBJECTIVE_INDEX = 0 #checkpoints
        self.PAYLOAD_PROGRESS = 0
    
    def AddIndex(self):
        self.OBJECTIVE_INDEX += 1
    
    def GetIndex(self):
        return self.OBJECTIVE_INDEX
    
    def UpdateProgress(self, NEW_VALUE):
        self.PAYLOAD_PROGRESS = NEW_VALUE
    
    def GetProgress(self):
        return self.PAYLOAD_PROGRESS
