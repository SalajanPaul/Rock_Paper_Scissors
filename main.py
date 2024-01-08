import random
import sys


def play():
    user = input("Rock[r], paper[p] or scissors[s] ",)
    computer = random.choice(["r", "p", "s"])
    print(computer)

    if user not in ["r", "p", "s"]:
        print("You need to enter a valid letter!")
        sys.exit()


    if user == computer:
        return "It's a tie!"


    if is_win(user, computer):
        return "You won"

    return "You lost"


def is_win(player, opponemt):
    if (player == "r" and opponemt == "s") or (player == "s" and opponemt == "p") or \
            (player == "p" and opponemt == "r"):
        return True




print(play())