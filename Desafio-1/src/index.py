nome = input("Digite seu nome:")
XP = float(input("Digite seu XP(experiência):"))

ranks = [{"minXP": 0, "maxXP": 1000, "level": "Ferro"},
        {"minXP": 1001, "maxXP": 2000, "level": "Bronze"},
        {"minXP": 2001, "maxXP": 5000, "level": "Prata"},
        {"minXP": 5001, "maxXP": 7000, "level": "Ouro"},
        {"minXP": 7001, "maxXP": 8000, "level": "Platina"},
        {"minXP": 8001, "maxXP": 9000, "level": "Ascendente"},
        {"minXP": 9001, "maxXP": 10000, "level": "Imortal"},
        {"minXP": 10001, "maxXP": float("inf"), "level": "Radiante"}
]

def getLevelXP(xp):
    for i in ranks:
        if i["minXP"] <= xp <= i["maxXP"]:
            return i["level"]
         


print("O Herói de nome:", nome, "está no nível:" , getLevelXP(XP))



