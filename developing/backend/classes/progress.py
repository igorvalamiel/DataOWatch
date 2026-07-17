from tools.time_dealing import Time, Seconds_to_Time

class Progress():
    def __init__(self, TYPE):
        self.INDEX = -1
        self.PROGRESS = -1  # Only payloads have "progress" percentage
        self.TYPE = TYPE
        self.TARGET = None
        
        if self.TYPE == "payload_progress":
            self.TARGET = Payload()
        elif self.TYPE == "objective_updated":
            self.TARGET = Objective()
        
        self.UpdateAll()
    
    def AddIndex(self):
        self.TARGET.AddIndex()
        self.UpdateAll()
    
    def UpdateProgress(self):
        if self.TYPE == "payload_progress":
            self.TARGET.UpdateProgress()
        else:
            raise("Esse tipo de objetivo não possui porcentagem de progresso.")
        self.UpdateAll
    
    def UpdateAll(self):
        self.INDEX = self.TARGET.PROGRESS_INDEX
        if self.TYPE == "payload_progress":
            self.PROGRESS = self.TARGET.PAYLOAD_PROGRESS
            


class Objective():
    def __init__(self):
        self.PROGRESS_INDEX = 0 #checkpoints
    
    def AddIndex(self):
        self.PROGRESS_INDEX += 1



class Payload():
    def __init__(self):
        self.PROGRESS_INDEX = 0 #checkpoints
        self.PAYLOAD_PROGRESS = 0
    
    def AddIndex(self):
        self.PROGRESS_INDEX += 1
    
    def UpdateProgress(self, NEW_VALUE):
        self.PAYLOAD_PROGRESS = NEW_VALUE
