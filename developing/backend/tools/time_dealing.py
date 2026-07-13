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
        H, M, S = 0

        S += self.SECONDS + other.SECONDS
        if S >= 60:
            S -= 60
            M += 1
        
        M += self.MINUTES + other.MINUTES
        if M >= 60:
            M -= 60
            H += 1
        
        H += self.HOURS + other.HOURS

        return Time(f"{H}:{M}:{S}")


    def __sub__(self, other):
        H, M, S = 0, 0, 0
        
        S = self.SECONDS - other.SECONDS
        if S < 0:
            S += 60
            M -= 1
        
        M += self.MINUTES - other.MINUTES
        if M < 0:
            M += 60
            H -= 1
        
        H += self.HOURS - other.HOURS
        
        if H < 0: raise ValueError("Resultado da subtração não pode ser negativo.")
        
        return Time(f"{H}:{M}:{S}")


    def __mul__(self, other):
        raise("Essa classe não suporta multiplicação.")

    def __truediv__(self, other):
        raise("Essa classe não suporta divisão.")
    
    def __repr__(self):
        return f"{self.HOURS}:{self.MINUTES}:{self.SECONDS}"
