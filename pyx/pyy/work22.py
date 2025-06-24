import random

def display_hangman(tries):
    """Displays the hangman figure based on number of tries left"""
    stages = [
        # Final state: head, torso, both arms, both legs
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # Head, torso, both arms, one leg
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # Head, torso, both arms
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # Head, torso, one arm
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # Head and torso
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # Head
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # Initial empty state
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]




def get_word():

    words=["developer","python","algorithm","functions","data-sciene","machine learning"]
    return random.choice(words).upper()

def play_hangman():
    word= get_word()
    word_completion ='_' * len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess= input("Enter your guess word or letter: ").upper()


        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)



                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter ==guess]
                for index in indices:
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)


                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        
        else:
            print("Not a valid guess.")
            
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations, you guessed the word!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}")

if __name__ == "__main__":
    play_hangman()


            