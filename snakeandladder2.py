print("Are you ready to play snake and ladder?")
print("Enter to play")
input()
print("This Game can only be played by 2 humans at once.")
print("Press Enter to know the Rules")
input()
print("        RULES:-              ")
print("1. The Ladder gets you 8 numbers ahead.")
print("2. The Snake sends you 6 numbers behind.")
print("3. The Dice numbers will be randomly given.")
print("4. Reach 100 to win the game")
print("5. There are no extra chances and each player will get a chance alternatively.")
print("NOTE: THE SNAKES ARE ON 8, 15, 27, 39, 43, 55, 67, 72, 89, 93")
print("THE LADDERS ARE ON 5, 14, 23, 33, 45, 59, 66, 75, 83, 91")
goal1 = 0
goal2 = 0
goal = 0
current_place = 0
snake_list = [8, 15, 27, 39, 43, 55, 68, 72, 89, 93]
ladder_list = [5, 14, 24, 32, 45, 59, 61, 75, 84, 91]
print("Enter PLAYER 1 Name: ")
player1 = input()
print("Enter PLAYER 2 Name: ")
player2 = input()
while goal != 100:
    print("{}, press enter to roll the dice.".format(player1))
    input()
    import random
    ran = random.randint(1, 6)
    print("Your number is {}".format(ran))

    if goal1 + ran <= 100:
        goal1 = goal1 + ran
        print("Your current place is {}".format(goal1))
        print()
        print()
        if goal1 in snake_list:
            goal1 -= 6
            print("Oops, now Your current place is {}".format(goal1))
            print()
            print()
        elif goal1 in ladder_list:
            goal1 += 8
            print("yayy, now ur place is {}".format(goal1))
            print()
            print()
    else:
        print("Close call, try again")
        print("You current place is {}".format(goal1))
        print()
        print()
    if goal1 == 100:
        break


    print("{}, press enter to roll the dice.".format(player2))
    input()
    import random
    ran1 = random.randint(1, 6)
    print("Your number is {}".format(ran1))

    if goal2 + ran1 <= 100:
        goal2 = goal2 + ran1

        print("Your current place is {}".format(goal2))
        print()
        print()
        if goal2 in snake_list:
            goal2 -= 6
            print("Oops, now Your current place is {}".format(goal2))
            print()
            print()
        elif goal2 in ladder_list:
            goal2 += 8
            print("yayy, ur current place is {}".format(goal2))
            print()
            print()
    else:
        print("close call, try again")
        print("You current place is {}".format(goal2))
        print()
        print()
    if goal2 == 100:
        break
    if goal1 > goal2:
        goal = goal1
    elif goal2 > goal1:
        goal = goal2


if goal2 == 100:
    print("FINALLYYY {}, YOU WON".format(player2))
elif goal1 == 100:
    print("FINALLYYY {}, YOU WON".format(player1))

