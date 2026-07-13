import os

PATH = "developing/data/"
FILE_NAME = "teste0.csv"
FILE_PATH = PATH+FILE_NAME

with open(FILE_PATH, "r", encoding="utf-8") as FILE:
    for ROW in FILE:
        # tratando a linha
        CLEAN_ROW = ROW.strip()
        if not CLEAN_ROW: continue

        # jogando os dados numa lista
        DATA = CLEAN_ROW.split(',')
        print(DATA)
        break