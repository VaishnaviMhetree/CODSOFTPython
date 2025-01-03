import random
option=["rock","paper","scissor"]
while 1:
    player=input("Enter rock/paper/scissor:")
    computer="".join(random.sample(option,1))
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player==computer:
        print("It's a tie!")
    elif player=="rock" and computer=="scissor":
        print("You won!")
    elif player=="rock" and computer=="paper":
        print("You lose!")
    elif player=="scissor" and computer=="rock":
        print("You won!")
    elif player=="scissor" and computer=="paper":
        print("You won!")
    elif player=="paper" and computer=="scissor":
        print("You lose!")
    elif player=="paper" and computer=="rock":
        print("You lose!")