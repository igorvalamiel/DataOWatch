import sys
import os

# importantdo codigo python que ta em outra pasta
CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CURRENT_PATH)

from extractData import GetData
from tools.time_dealing import Time, Seconds_to_Time
from .round import Round
from .player import Player


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
        self.PLAYERS = {}

        # pegando dados
        for ROW in GetData(PATHWAY):

            # tirando [] do tempo de jogo
            ROW[0] = ROW[0].strip("[]")

            if ROW[1] == "match_start": self.MatchStart(ROW)
            elif ROW[1] == "match_end": self.MatchEnd(ROW)
            elif ROW[1] == "round_start":
                self.CURRENT_ROUND = Round(self.ROUND_ID, self.TEAM1, self.TEAM2, self.GAME_MODE)
                self.CURRENT_ROUND.BeginRound(ROW)
            elif ROW[1] == "round_end":
                self.CURRENT_ROUND.EndRound(ROW)
                self.ROUND_LIST.append(self.CURRENT_ROUND)
            elif ROW[1] == "payload_progress":
                if self.CURRENT_ROUND:
                    self.CURRENT_ROUND.TARGET.UpdateProgress(ROW[3])
            elif ROW[1] == "objective_updated":
                if self.CURRENT_ROUND:
                    self.CURRENT_ROUND.TARGET.AddIndex()
            elif ROW[1] == "objective_captured":
                if self.CURRENT_ROUND:
                    self.CURRENT_ROUND.TARGET.AddIndex()
            
            elif ROW[1] == "hero_spawn":
                PLAYER = Player(ROW[3], ROW[4], ROW[5])
                NICK = str(ROW[4])
                self.PLAYERS[NICK] = PLAYER
            elif ROW[1] == "kill":
                PLAYER = self.PLAYERS[ROW[4]]
                PLAYER.Kill(ROW)
            elif ROW[1] == "defensive_assist":
                PLAYER = self.PLAYERS[ROW[4]]
                PLAYER.AddDefAssist()
            elif ROW[1] == "offensive_assist":
                PLAYER = self.PLAYERS[ROW[4]]
                PLAYER.AddOffenAssist()

            # ONly if Mercy
            elif ROW[1] == "mercy_rez":
                if ROW[5] != "Mercy": raise "Esse herói não pode ressucitar outro."
                PLAYER = self.PLAYERS[ROW[4]]
                PLAYER.MercyRez(ROW[7], ROW[8])


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
        print("="*50)
        print(f"RESUMO DA PARTIDA - MAPA: {self.MAP} ({self.GAME_MODE})")
        print("="*50)
        print(f"Time 1: {self.TEAM1} | Pontuação Final: {self.TEAM1_SCORE}")
        print(f"Time 2: {self.TEAM2} | Pontuação Final: {self.TEAM2_SCORE}")
        print(f"Duração total: {self.DURATION}")
        print(f"Vencedor da Partida: {self.WINNER}")
        print(f"Total de Rounds no Log: {self.ROUNDS}")
        print(f"Total de Rounds Processados: {len(self.ROUND_LIST)}") # Excelente para ver se o parser não pulou nada
        
        print("\nDETALHES DOS ROUNDS:")
        for r in self.ROUND_LIST: 
            print(r)
        print("="*50)

        print("\nDETALHES DOS PLAYERS:")
        for i in self.PLAYERS.values():
            print("="*50)
            print(i)
        


# -------------------------------------------------------------------------------------------
