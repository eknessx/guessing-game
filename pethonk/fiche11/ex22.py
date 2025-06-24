question = {
    "name": "majd",
    "i am insane": True,
    "year": 2025,
}

feelings = ("happy", "normal", "bad", "insane")

def ask():
    status = 0

    option1 = input("What's your name? ").strip().lower()
    option2 = input("How do you feel? ").strip().lower()
    option3 = int(input("What year do you live in? "))

    if option2 == "happy":
        status += 1
        print("Oh well, a happy believer.")
    elif option2 == "normal":
        status += 1
        print("Normal is weird in most cases, but it's okay if you dont act crazy.")
    elif option2 == "bad":
        status -= 1
        print("Feeling bad... well, everyone does sometimes. It sucks.")
    elif option2 == "insane":
        status -= 1
        print("If you're at that level of mental struggle, I get your pain.")
    else:
        print("Feeling not recognized, staying neutral.")

    if option3 < 2025:
        print("Oh, so you're from Gen Z or Alpha.")
        option5 = input("Gen Z or Alpha? ").strip().lower()
        if option5 == "alpha":
            status -= 1
            print("Internet brat ")
        elif option5 == "z":
            status += 1
            print("Miss the old days?")
        else:
            print("Okay, cool.")

    if option1 == question["name"]:
        print("It's you! Oh well, want to talk?")
        option4 = input("Yes or no? ").strip().lower()
        if option4 == "yes":
            status += 1
            print("Glad to talk with you.")
        else:
            print("Bye.")

    return status

# Run and print the result
try:
    final_status = ask()
    print("\nYour final status is:", final_status)
except Exception as e:
    print("An error occurred:", e)
