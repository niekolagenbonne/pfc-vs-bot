import random
choisir_signe_player_int = 1
while choisir_signe_player_int != 0:
    choisir_signe_bot = random.randint(1, 3)
    choisir_signe_player = input("Veuillez choisir un signe entre la pierre(1) le feuille(2) et le ciseaux(3)! 0 pour quitter\n")

    try:
        choisir_signe_player_int = int(choisir_signe_player)     
    except:
        print("Veuillez rentrer un chiffre correct!")
    
    if choisir_signe_player_int != 0 and choisir_signe_player_int <= 3:
        #bot
        if choisir_signe_bot == 1:
            print("Le bot a choisi le pierre!")
        if choisir_signe_bot == 2:
            print("Le bot a choisi la Feuille!")
        if choisir_signe_bot == 3:
            print("Le bot a choisi la ciseaux!")
        #and
        print("et")
        #and
        #player
        if choisir_signe_player_int == 1:
            print("Vous avez choisi la pierre!")
        if choisir_signe_player_int == 2:
            print("Vous avez choisi la feuille!")
        if choisir_signe_player_int == 3:
            print("Vous avez choisi le ciseaux!")
        
        tab = [ ["égalité!!","perdu!!","gagné!!"], ["!!","égalité!!","perdu!!"], ["perdu!!","gagné!!","égalité!!"] ]
        print(tab[choisir_signe_player_int-1][choisir_signe_bot-1])
    elif choisir_signe_player_int > 3:
        print("Veuillez rentrer un chiffre correct!")
    else:
        print("au revoir")
    