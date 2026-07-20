from tools.time_dealing import Time, Seconds_to_Time

class Progress():
    def __init__(self, MODE):
        self.INDEX = -1
        self.PROGRESS = -1  # Only payloads have "progress" percentage
        self.MODE = MODE
        self.TARGET = None

        self.PAYLOAD_MODES = ["Escolta", "Híbrido"]
        self.OBJECTVE_MODES = ["Controle", "Flashpoint"]
        self.ROBOT_MODES = ["Batalha"]
        
        if self.MODE in self.PAYLOAD_MODES:
            self.TARGET = Payload()
        elif self.MODE in self.OBJECTVE_MODES:
            self.TARGET = Objective()
        else:
            self.TARGET = Robot()
        
        self.UpdateAll()
    
    def AddIndex(self):
        self.TARGET.AddIndex()
        self.UpdateAll()
    
    def UpdateProgress(self, NEW_VALUE):
        if self.MODE in self.PAYLOAD_MODES:
            self.TARGET.UpdateProgress(NEW_VALUE)
        else:
            raise("Esse tipo de objetivo não possui porcentagem de progresso.")
        self.UpdateAll()
    
    def UpdateAll(self):
        self.INDEX = self.TARGET.PROGRESS_INDEX
        print("Index: ", self.INDEX)
        if self.MODE in self.PAYLOAD_MODES:
            self.PROGRESS = self.TARGET.PAYLOAD_PROGRESS
            print("Progress: ", self.PROGRESS)
            


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


class Robot():
    def __init__(self):
        self.PROGRESS_INDEX = 0
    
    def AddIndex(self):
        self.PROGRESS_INDEX += 1