import random
def choose():
    my_choice=input("Enter yours choice 'r' for Rock"
                    " 's' for Scissor 'p' for paper")
    comp_choice=random.choice(["r","p","s"])
    print(f"And the computer choice is {comp_choice}")

    if my_choice == comp_choice:
        return 'Tie'
    if rule(my_choice,comp_choice):
        return  "Yay! you have won"

    return 'you lost'

def rule(player,opponent):
    # r>s, s>p, p>r
    if (player=='r' and opponent=='s') or (player == 's' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
print(choose())