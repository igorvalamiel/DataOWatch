import sys
import os

# importantdo codigo python que ta em outra pasta
CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CURRENT_PATH)

from extractData import GetData
from tools.time_dealing import Time, Seconds_to_Time
from .round import Round
from .progress import Progress


# -------------------------------------------------------------------------------------------


class Match:
    def __init__(self, PATHWAY):
        self.MAP = ""
        self.GAME_MODE = ""
        self.TEAM1 = ""
        self.TEAM2 = ""
        self.DURATION = None
        self.ROUNDS = 0
        self.TEAM1_SCORE = 0
        self.TEAM2_SCORE = 0
        self.WINNER = ""
        self.ROUND_LIST = []
        self.ROUND_ID = len(self.ROUND_LIST)+1 # esse identificador é o tamanho da lista pq é o ultimo index que ainda não existe
        self.CURRENT_ROUND = None
        self.TARGET = None #Objectives or Payload

        # pegando dados
        for ROW in GetData(PATHWAY):

            # tirando [] do tempo de jogo
            ROW[0] = ROW[1::-1]

            if ROW[1] == "match_start": self.MatchStart(ROW)
            if ROW[1] == "match_end": self.MatchEnd(ROW)
            if ROW[1] == "setup_complete":
                self.TARGET = Progress(self.GAME_MODE)
            if ROW[1] == "round_start":
                self.CURRENT_ROUND = Round(self.ROUND_ID, self.TEAM1, self.TEAM2)
                self.CURRENT_ROUND.BeginRound(ROW)
            if ROW[1] == "round_end":
                self.CURRENT_ROUND.EndRound(ROW)
                self.ROUND_LIST.append(self.CURRENT_ROUND)

        print("Arquivo lido com sucesso!")
        print("="*50)
    
    # Pegando dados iniciais
    def MatchStart(self, ROW):
        self.MAP = ROW[3]
        self.GAME_MODE = ROW[4]
        self.TEAM1 = ROW[5]
        self.TEAM2 = ROW[6]

    # Pegando dados finais
    def MatchEnd(self, ROW):

        # vendo se o jogo realmente começou
        if self.MAP == "": raise("Erro: O jogo não foi iniciado.")

        self.DURATION = Seconds_to_Time(ROW[2])
        self.ROUNDS = int(ROW[3])
        self.TEAM1_SCORE = int(ROW[4])
        self.TEAM2_SCORE = int(ROW[5])

        # verificando vencedor
        if self.TEAM1_SCORE > self.TEAM2_SCORE: self.WINNER = self.TEAM1
        elif self.TEAM1_SCORE < self.TEAM2_SCORE: self.WINNER = self.TEAM2
        else: self.WINNER = "Empate"

    # função para printar o resumo de informações
    def Info(self):
        print("Mapa: ", self.MAP)
        print("Modo: ", self.GAME_MODE)
        print("Time 1: ", self.TEAM1)
        print(f"Pontuação - {self.TEAM1}: ", self.TEAM1_SCORE)
        print("Time 2: ", self.TEAM2)
        print(f"Pontuação - {self.TEAM2}: ", self.TEAM2_SCORE)
        print("Duração total: ", self.DURATION)
        print("Rounds: ", self.ROUNDS)
        print("Vencedor: ", self.WINNER)
        for i in self.ROUND_LIST: print(i)
        # print("Round ID: ", self.ROUND_ID)
        # print("Current Round: ", self.CURRENT_ROUND)
        # print("Target: ", self.TARGET)


# -------------------------------------------------------------------------------------------
