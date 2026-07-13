import sys
import os

# importantdo codigo python que ta em outra pasta
CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CURRENT_PATH)

from extractData import GetData


# -------------------------------------------------------------------------------------------


class Match:
    def __init__(self, PATHWAY):

        # pegando dados
        DATA = GetData(PATHWAY)
        while True:
            try:
                ROW = next(DATA)
                print(ROW)
            except:
                print("Arquivo lido com sucesso!")
                break




# -------------------------------------------------------------------------------------------


# só pra desenvolvimento de código isso aqui
PATH = "developing/data/"
FILE_NAME = "teste0.csv"
FILE_PATH = PATH+FILE_NAME
teste = Match(FILE_PATH)