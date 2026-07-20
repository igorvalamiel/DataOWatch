from tools.time_dealing import Time, Seconds_to_Time
from .progress import Progress

class Round():
    def __init__(self, ID, TEAM1, TEAM2, GAME_MODE):
        self.ID = ID
        self.GAME_MODE = GAME_MODE
        self.ATTACK_TEAM = ""
        self.DURATION = None
        self.TEAM1_SCORE = 0
        self.TEAM2_SCORE = 0
        self.TEAM1_CONTROL = 0
        self.TEAM2_CONTROL = 0
        self.BEGIN_TIME = 0
        self.END_TIME = 0
        self.WINNER = ["Empate", TEAM1, TEAM2]
        self.TARGET = None #Objectives, Payload or Robot

        self.TARGET = Progress(self.GAME_MODE)


    def BeginRound(self, ROW):
        self.BEGIN_TIME = Seconds_to_Time(ROW[2])

    def EndRound(self, ROW):
        self.ATTACK_TEAM = ROW[4]
        self.TEAM1_SCORE = int(ROW[5])
        self.TEAM2_SCORE = int(ROW[6])
        if self.GAME_MODE in ["Controle", "Flashpoint"]:
            if len(ROW) > 9:
                self.TEAM1_CONTROL = ROW[8]
                self.TEAM2_CONTROL = ROW[9]
        else:
            self.TEAM1_CONTROL = 0
            self.TEAM2_CONTROL = 0
        self.END_TIME = Seconds_to_Time(ROW[2])
        self.DURATION = self.END_TIME - self.BEGIN_TIME

        self.WINNER = self.CalculateWinner()


    def CalculateWinner(self):
        if self.TEAM1_SCORE > self.TEAM2_SCORE: return self.WINNER[1]
        elif self.TEAM1_SCORE < self.TEAM2_SCORE: return self.WINNER[2]
        else: return self.WINNER[0]


    def __repr__(self):
        STRING_LINE = """"""
        STRING_LINE += "-"*20
        STRING_LINE += f"\nROUND {self.ID}:"
        STRING_LINE += f"\n     Attacking team: {self.ATTACK_TEAM}"
        STRING_LINE += f"\n     Duration: {self.DURATION}"
        STRING_LINE += f"\n     Team 1 Score: {self.TEAM1_SCORE}"
        STRING_LINE += f"\n     Team 2 Score: {self.TEAM2_SCORE}"
        STRING_LINE += f"\n     Team 1 Control (%): {self.TEAM1_CONTROL}"
        STRING_LINE += f"\n     Team 2 Control (%): {self.TEAM2_CONTROL}"
        
        if self.TARGET:
            STRING_LINE += f"\n     Último Checkpoint/Estágio: {self.TARGET.INDEX}"
            # Se for modo de escolta ou híbrido, mostra a porcentagem da carga
            if self.TARGET.MODE in self.TARGET.PAYLOAD_MODES:
                STRING_LINE += f"\n     Progresso Final da Carga: {self.TARGET.PROGRESS}"
        
        STRING_LINE += f"\n     Winner: {self.WINNER}"
    
        return STRING_LINE
