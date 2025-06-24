#the code is a word decriptor where it takes the user word and turns it to a series of number
# Example output:
# Input: "ekness"
# Output: 
#e -> 4
#k -> 10
#n -> 13
#e -> 4
#s -> 18
#s -> 18
import string
import tkinter



#stupid main function
def crypt():
    #i honestly think the try except is useless cuz the only input is me and im not stupid for it but yeah 
    user_input=str(input("enter any random word "))
    #for all sorts of upper and lower case letters stored in a dict
    upper_case_letters={}#for upper letters
    lower_case_letters={}#for lower letters

    #using 2 for loops for the lower and upper i wanted to uhh make them in one for loop but python can't loop 2 arguments at the same time
    for i,char in enumerate(string.ascii_lowercase):
            upper_case_letters[char]=i

    for i,char in enumerate(string.ascii_uppercase):
            lower_case_letters[char]=i

    #if the for loop failed then yeah il probably figure it out later better than some wall of errors
    try:
        if user_input.isalpha():
            for char in user_input:
                if char in upper_case_letters:
                    print(f"{char} -> {upper_case_letters[char]}")
                elif char in lower_case_letters:
                    print(f"{char} -> {lower_case_letters[char]}")
    except:
        print("Failed instance:cant use numbers letters ONLY")
crypt() 