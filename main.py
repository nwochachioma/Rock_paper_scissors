import random

print ("Welcome to Rock, Paper & Scissors game \n")
print ('''Winning rules of the game are as follows: 
        Rock VS Paper => Paper wins
        Rock VS Scissors => Rock wins
        Paper VS Scissors => Scissors wins''')

def game():
    actions = ["R", "P", "S"]
    user_choice = input("\nEnter a choice R, P or S: ").upper()
    while user_choice not in actions:
        print ("You entered an invalid choice, please enter again")
        game()
        break
    cpu_choice = random.choice(actions)
    if user_choice == cpu_choice:
        print ("The outcome: Player (",user_choice,") ",": CPU (", cpu_choice,")")
        print ("It's a tie, please enter again\n")
        game()
    elif user_choice == "R":
        if cpu_choice == "P":
            print ("The outcome: Player (",user_choice,") ",": CPU (", cpu_choice,")")
            print ("You Lose ....")
        else:
            print ("The outcome: Player (",user_choice,") ",": CPU (", cpu_choice,")")
            print ("You Won !")
    elif user_choice == "R":
        if cpu_choice == "S":
            print ("The outcome: Player (",user_choice,") ",": CPU (", cpu_choice,")")
            print ("You Won !")
        else:
            print ("The outcome: Player (",user_choice,") ",": CPU (", cpu_choice,")")
            print ("You Lose ....")
    elif user_choice == "P":
        if cpu_choice == "S":
            print ("The outcome: Player (",user_choice,") ",": CPU (", cpu_choice,")")
            print ("You Lose ....")
        else:
            print ("The outcome: Player (",user_choice,") ",": CPU (", cpu_choice,")")
            print ("You Won !")
    elif user_choice == "S":
        if cpu_choice == "P":
            print ("The outcome: Player (",user_choice,") ",": CPU (", cpu_choice,")")
            print ("You Won !")
        else:
            print ("The outcome: Player (",user_choice,") ",": CPU (", cpu_choice,")")
            print ("You Lose ....")

    def again():
        again = input("\nDo you wish to continue? Y for Yes & N for No: ")
        if (again).upper() == "Y":
            game()
        elif (again).upper() == "N":
            print("See you again")
        else:
            again()
    again()
game()
