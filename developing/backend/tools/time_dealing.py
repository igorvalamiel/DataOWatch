class Time:
    def __init__(self, TIME : str):
        self.HOURS = 0
        self.MINUTES = 0
        self.SECONDS = 0

        self.GetTime(TIME=TIME)


    def GetTime(self, TIME):
        HR, MIN, SEC = TIME.split(':')
        self.HOURS = int(float(HR))
        self.MINUTES = int(float(MIN))
        self.SECONDS = float(SEC)


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
        return f"{int(self.HOURS)}:{int(self.MINUTES)}:{self.SECONDS:.2f}"




def Seconds_to_Time(SEC_INPUT : float):
    INT_PART = SEC_INPUT // 1

    SEC = (INT_PART % 60) + (SEC_INPUT - INT_PART)
    MIN = INT_PART // 60
    HR = 0
    if MIN >= 60:
        HR = MIN // 60
        MIN = MIN % 60
    
    print(Time(f"{HR}:{MIN}:{SEC}"))


Seconds_to_Time(123.21)
