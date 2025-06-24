#Un jeu au hazard se deroule de la facon suivante:
#on paie 2 euros pour jouer et on lance 2 dices (chacun est de 6 cotes: 1, 2, 3, 4, 5, 6)
#si le joueur obtient un double (2 fois: 1 ou 2 fois : 2 ou ...)
#il recupere sa mise et recoite la somme des points marquee
#si non, il ne recoit rien et perd sa mise
#Ecrire le code python pour simuler ce jeu
import random

euros = 4
score = 4
highestScore = 0

input(f"You have {euros} euros, to play you have to pay 4, press enter: ")
for i in range(5):
    input(f"You have {score} score, to play, press enter: ")

    r1 = random.randrange(1, 7)
    r2 = random.randrange(1, 7)

    print(f"Dice 1: {r1}")
    print(f"Dice 2: {r2}")

    if r1 == r2:
        print(f"You gained {r1 + r2} score!")
        score += r1 + r2
        highestScore = max(score, highestScore)
    else:
        print("You lost score...")
        score -= 2

print("The game ended.")
print(f"Your score: {score}")
print(f"Your highest score: {highestScore} euros")