# transformando dados numericos em tipos numericos
def StringToNumber(s):
    s = s.strip()

    # tentando transformar em int
    try: return int(s)
    except ValueError: pass

    # tentando transformar em float
    try: return float(s)
    except: pass

    # se não der, é string mesmo
    return s


def GetData(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as FILE:
        for ROW in FILE:
            # tratando a linha
            CLEAN_ROW = ROW.strip()
            if not CLEAN_ROW: continue

            # jogando os dados numa lista e tratando
            DATA = [StringToNumber(item) for item in CLEAN_ROW.split(',')]
            
            # retornando linha por linha
            yield DATA
