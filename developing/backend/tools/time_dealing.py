class Time:
    def __init__(self, TIME : str):
        self.HOURS = 0
        self.MINUTES = 0
        self.SECONDS = 0

        self.GetTime(TIME=TIME)


    def GetTime(self, TIME):
        HR, MIN, SEC = TIME.split(':')
        self.HOURS = HR
        self.MINUTES = MIN
        self.SECONDS = SEC

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        raise("Essa classe não suporta multiplicação.")

    def __truediv__(self, other):
        raise("Essa classe não suporta divisão.")
    