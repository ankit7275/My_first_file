import random
def guess(x):
    comp_num=random.randint(1,x)
    mine_num=0
    while mine_num != comp_num:
        mine_num=int(input(f"Enter any number between 1 to {x}"))
        if mine_num > comp_num:
            print(f"you have entered {mine_num} which is high")
        elif mine_num < comp_num:
            print(f"you have entered {mine_num} which is low")

    print(f"yay! you entered right number i.e {mine_num}")

guess(10)