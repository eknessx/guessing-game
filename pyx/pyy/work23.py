import random
import sys
import time



def loading_bar(duration=3,bar_length=20):
    print("Loading")
    for x in range(bar_length+1):
        progress = "█" * x + "-" * (bar_length - x)
        percentage= int((x / bar_length)*100)
        sys.stdout.write(f"\r[{progress}] {percentage}%")
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    print("\nLoaded!\n")
    print("return teh user ")
loading_bar()
        