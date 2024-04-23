import random
import sys
import random
from enum import Enum

def RockPaperScissors(name="Ayush"):
    class RPS(Enum):

        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playagain = True
    while playagain:
        playerchoice = int(input("Enter: \n 1 for Rock\n 2 for Paper\n 3 for Scissors\n\n"))
        computerchoice = int(random.choice("123"))

        if playerchoice<1 or playerchoice>3:
            sys.exit(f"{name} please enter values from 1 to 3.")
        print(f"{name} entered:  {str(RPS(playerchoice)).replace("RPS.","")}")
        print(f"Python enter: {str(RPS(computerchoice)).replace("RPS.","") }")

        if playerchoice == 1 and computerchoice == 3:
            print("🎉 You win! ")
        elif playerchoice == 2 and computerchoice == 1:
            print("🎉 You win! ")
        elif playerchoice == 3 and computerchoice == 2:
            print("🎉 You win! ")
        elif playerchoice == computerchoice:
            print("😲 Tie Game! ")
        else:
            print("🐍 Python win! ")

        choice = input("\nPlay again? Press 'Y' for Yes or Q to Quit: ")
        if choice == 'Y' or choice == 'y':
            continue
        else:
            print("\n🎉🎉🎉🎉🎉")
            print("Thanks for playing!!")
            playagain = False

    sys.exit("Bye! 👋")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Provides a personalised game experience")
    parser.add_argument("-n","--name",metavar="name",required=True,
                         help="The name of the person who is playing the game")
    args=parser.parse_args()
    RockPaperScissors(args.name)