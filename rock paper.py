import random
while True:
    user = input("enter a choice rock,paper,scissors")
    possibleactions = ["rock","paper","scissors"]
    computerchoice = random.choice(possibleactions)
    print("computer choice is",computerchoice)
    print("user choice is",user)
    if user == computerchoice:
        print("it's tie")
    elif user == "rock":
        if computerchoice == "scissors":
            print("you won")
        else:
            print("computer won")
    elif user == "paper":
        if computerchoice == "rock":
            print("you won")
        else:
            print("computer won")
    elif user == "scissors":
        if computerchoice == "paper":
            print("you won")
        else:
            print("computer won")
    playagain =input("do you like to play again y/n")
    if playagain == "n":
        break 


        

