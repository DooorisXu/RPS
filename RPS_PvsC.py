from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assugn a random play to the computer
computer = t[randint(0,2)]

#set player to faulse
player = False

while player == False:
    #set player to true
    player = input ("Rock, Paper, Scissors?")
    #if there is a tie
    if player == computer :
        print ("Tie!")
    #is the player inputs rock
    elif player == "Rock":
        if computer == "Paper":
            print("You lost", computer, "covers", player)
        else:
            print("You won!", player, "smashes", computer)
    #if the player inputs paper
    elif player == "Paper":
        if computer == "Scissors":
            print("You lost", computer, "covers", player)
        else:
            print("You won!", player, "smashes", computer)
    #if the player inputs scissors
    elif player == "Scissors":
        if computer == "Rock":
            print("You lost", computer, "smashes", player)
        else:
            print("You won!", player, "cut", computer)
    #if there is a spelling error
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, set it to false so the loop contiues
    player = False
    computer = t[randint(0,2)]