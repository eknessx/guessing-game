import random, time

DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # Fixed typo (was CANAVS_HEIGHT)

QUIZ_DURATION = 52
MIN_DICE = 2
MAX_DICE = 6

REWARD = 4
PENALTY = -3

# The program hangs if all of the dice can't fit on the screen:
assert MAX_DICE <= 14

# Dice faces
D1 = ([
    "+-------+",
    "|       |",
    "|   O   |",
    "|       |",
    "+-------+"
], 1)



D2a = ([
    "+-------+",
    "| O     |",
    "|       |",
    "|     O |",
    "+-------+"
], 2)

D2b = ([
    "+-------+",
    "|     O |",
    "|       |",
    "| O     |",
    "+-------+"
], 2)

D3a = ([
    "+-------+",
    "| O     |",
    "|   O   |",
    "|     O |",
    "+-------+"
], 3)

D3b = ([
    "+-------+",
    "|     O |",
    "|   O   |",
    "| O     |",
    "+-------+"
], 3)

D4 = ([
    "+-------+",
    "| O   O |",
    "|       |",
    "| O   O |",
    "+-------+"
], 4)

D5 = ([
    "+-------+",
    "| O   O |",
    "|   O   |",
    "| O   O |",
    "+-------+"
], 5)

D6a = ([
    "+-------+",
    "| O   O |",
    "| O   O |",
    "| O   O |",
    "+-------+"
], 6)

D6b = ([
    "+-------+",
    "| O O O |",
    "|       |",
    "| O O O |",
    "+-------+"
], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]


def explain():
    print(f"""
        You have to add up the sides of all the dice displayed on the screen.
        You have {QUIZ_DURATION} seconds to answer as many as you can.
        You get {REWARD} points for a correct answer,
        and a penalty of {abs(PENALTY)} point(s) for an incorrect answer.
    """)
    input("Press Enter to start...")


def main():
    correctAnswers = 0
    incorrectAnswers = 0
    startTime = time.time()

    while time.time() < startTime + QUIZ_DURATION:
        sumAnswer = 0
        diceFaces = []
        topLeftDiceCorners = []
        numDice = random.randint(MIN_DICE, MAX_DICE)

        for _ in range(numDice):
            die = random.choice(ALL_DICE)
            diceFaces.append(die[0])
            sumAnswer += die[1]

        # Determine positions
        for _ in range(len(diceFaces)):
            while True:
                left = random.randint(0, CANVAS_WIDTH - DICE_WIDTH)
                top = random.randint(0, CANVAS_HEIGHT - DICE_HEIGHT)

                overlaps = False
                for prevLeft, prevTop in topLeftDiceCorners:
                    if (
                        abs(left - prevLeft) < DICE_WIDTH and
                        abs(top - prevTop) < DICE_HEIGHT
                    ):
                        overlaps = True
                        break

                if not overlaps:
                    topLeftDiceCorners.append((left, top))
                    break

        # Draw dice to canvas
        canvas = {}
        for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
            dieFace = diceFaces[i]
            for dy in range(DICE_HEIGHT):
                for dx in range(DICE_WIDTH):
                    canvas[(dieLeft + dx, dieTop + dy)] = dieFace[dy][dx]

        # Print canvas
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                print(canvas.get((x, y), ' '), end='')
            print()

        # Player input
        response = input("Enter the sum: ").strip()
        if response.isdigit() and int(response) == sumAnswer:
            correctAnswers += 1
        else:
            print(f"Incorrect! The answer was {sumAnswer}")
            incorrectAnswers += 1
            time.sleep(1)

    # Score summary
    score = (correctAnswers * REWARD) + (incorrectAnswers * PENALTY)
    print("\nGame Over!")
    print(f"Correct:   {correctAnswers}")
    print(f"Incorrect: {incorrectAnswers}")
    print(f"Final Score: {score}")


# Start game
explain()
if __name__=="__main__":
    main()

