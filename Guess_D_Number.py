import random
# we are guessing the computer number
def my_guess(x):
    comp_num=random.randint(1,x)
    mine_num=0
    while mine_num != comp_num:
        mine_num=int(input(f"Enter any number between 1 to {x}"))
        if mine_num > comp_num:
            print(f"you have entered {mine_num} which is high")
        elif mine_num < comp_num:
            print(f"you have entered {mine_num} which is low")

    print(f"yay! you entered right number i.e {mine_num}")
    print(f"computer generated number is also {comp_num}")
# y=int(input("enter any number"))
# my_guess(y)
# here computer is guessing our number
def comp_guess(x):
    low = 1
    high = x
    feedback=''
    while feedback != 'c':
        if low != high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is guess {guess} is too high (h),too low (l) or corect")
        if feedback=='l':
            low=guess+1
        elif feedback=='h':
            high=guess-1
    print(f"yay you have guessed the right number {guess}")

x=int(input("input any numbers"))
comp_guess(x)




