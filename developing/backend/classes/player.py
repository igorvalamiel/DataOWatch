class Player():
    def __init__(self, TEAM, NAME, HERO, PREV_HERO=False, PREV_HERO_TIME=False):
        self.TEAM = TEAM
        self.NAME = NAME
        self.HERO = HERO
        self.HEROS_PLAYED = {} # Futuramente adicionar kills e assistencias por heroi jogado
        self.KILLS = []
        self.DEF_ASSIST = 0
        self.OFFEN_ASSIST = 0

        # Only if Mercy
        self.REZ = {}

        if PREV_HERO_TIME:
            if PREV_HERO in self.HEROS_PLAYED:
                self.HEROS_PLAYED[PREV_HERO] += PREV_HERO_TIME
            else:
                self.HEROS_PLAYED[PREV_HERO] = PREV_HERO_TIME
    
    def Kill(self, ROW):
        KILL = Kill(ROW[2], ROW[3], ROW[4], ROW[5], ROW[6], ROW[7], ROW[8], ROW[9], ROW[10], ROW[11], ROW[12])
        print(KILL)
    
    def AddDefAssist(self):
        self.DEF_ASSIST += 1
    
    def AddOffenAssist(self):
        self.OFFEN_ASSIST += 1
    
    # Only if Mercy
    def MercyRez(self, PLAYER, HERO):
        if PLAYER in self.REZ:
            self.REZ[PLAYER].append(HERO)
        else:
            self.REZ[PLAYER] = [HERO]

    def __repr__(self):
        RETURN_TXT = ""
        RETURN_TXT += "Jogador: " + str(self.NAME)
        RETURN_TXT += "\nTime: " + str(self.TEAM)
        RETURN_TXT += "\nHerois: "
        for hero, time in self.HEROS_PLAYED.items(): RETURN_TXT += f"\n   {hero} - {time} jogado"
        RETURN_TXT += f"\nKills = {self.KILLS}"
        RETURN_TXT += f"\nDefensive Assistences = {self.DEF_ASSIST}"
        RETURN_TXT += f"\nOffensive Assistences = {self.OFFEN_ASSIST}"
        if self.REZ:
            RETURN_TXT += f"Mercy Rez: ["
            for player, hero in self.REZ.items(): RETURN_TXT += f"{player} ({hero}), "
            RETURN_TXT += ']'

        return RETURN_TXT

class Kill():
    def __init__(self, TEMPO, KILLER_TEAM, KILLER_NAME, KILLER_HERO, VICT_TEAM, VICT_NAME, VICT_HERO, ABILITY, DAMAGE, IS_CRITICAL, IS_ENVIR):
        self.TEMPO = TEMPO
        self.KILLER_TEAM = KILLER_TEAM
        self.KILLER_NAME = KILLER_NAME
        self.KILLER_HERO = KILLER_HERO
        self.VICT_TEAM = VICT_TEAM
        self.VICT_NAME = VICT_NAME
        self.VICT_HERO = VICT_HERO
        self.ABILITY = ABILITY
        self.DAMAGE = DAMAGE
        self.IS_CRITICAL = IS_CRITICAL
        self.IS_ENVIR = IS_ENVIR
    
    def __repr__(self):
        TXT = f"{self.KILLER_NAME} ({self.KILLER_HERO}) --- {self.ABILITY} --> {self.VICT_NAME} ({self.VICT_HERO})  :   Dano = {self.DAMAGE}"
        return TXT
