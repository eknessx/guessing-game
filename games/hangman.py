import random, math

words = ["fish", "eating", "walking", "list", "house", "car", "mosheyang", "van", "fireworks", "food", "football", "basketball", "paper", "plane", "airplane", "sphere", "circle", "square", "length"]

chosenWord = words[(int)(random.random() * len(words))]
chosenWord = list(chosenWord)

guessingWord = []
for i in range(0, len(chosenWord)):
    guessingWord.append("_")

attempts = 0
maxAttempts = 5
while guessingWord.__contains__("_"):
    if attempts == maxAttempts:
        break

    for i in guessingWord:
        print(i, end="")
    print("\n")
    letter = input("Your Guess: ")
    if not chosenWord.__contains__(letter) and not guessingWord.__contains__(letter):
        attempts += 1
        print("Incorrect Guess...")
        print(maxAttempts - attempts, "Attempts left")
    elif not guessingWord.__contains__(letter):
        print("Correct Guess!")
    while chosenWord.__contains__(letter):
        guessingWord[chosenWord.index(letter)] = letter
        chosenWord[chosenWord.index(letter)] = "_"
if guessingWord.__contains__("_"):
    print("You lost...")
else:
    print("You won!")
    for i in guessingWord:
        print(i, end="")
