import sys
import os

# importantdo codigo python que ta em outra pasta
CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CURRENT_PATH)

from extractData import GetData


# -------------------------------------------------------------------------------------------


class Match:
    def __init__(self, PATHWAY):
        self.MAP = ""
        self.GAME_MODE = ""
        self.TEAM1 = ""
        self.TEAM2 = ""
        self.winner = ""

        # pegando dados
        for ROW in GetData(PATHWAY):

            # Match Start
            if ROW[1] == "match_start": self.MatchStart(ROW)

        print("Arquivo lido com sucesso!")
    
    # Getting starting info
    def MatchStart(self, ROW):
        self.MAP = ROW[3]
        self.GAME_MODE = ROW[4]
        self.TEAM1 = ROW[5]
        self.TEAM1 = ROW[6]






# -------------------------------------------------------------------------------------------


# só pra desenvolvimento de código isso aqui
PATH = "developing/data/"
FILE_NAME = "teste1.csv"
FILE_PATH = PATH+FILE_NAME
teste = Match(FILE_PATH)

print(teste.MAP)
