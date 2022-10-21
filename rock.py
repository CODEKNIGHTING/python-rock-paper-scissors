import random
userwins = 0
computerwins = 0
options = ["rock", "paper", "scissors"]
while True:
    userchioce = input("type rock/paper/scissors/ or q to quit\n").lower()
    if userchioce == "q":
        print("soory to hear you want to quit")
        break

    if userchioce not in options:
        print("type the rock/paper/scissors")
        continue
    random_number = random.randint(0, 2)
    # rock is 0 paper is 1 and scissors is 2
    computerchioce = options[random_number]
    print("computer picked " + computerchioce + ".")

    if userchioce == "rock" and computerchioce == "scissors":
        print("you won")
        userwins += 1

    elif userchioce == "paper" and computerchioce == "rock":
        print("you won")
        userwins += 1

    elif userchioce == "scissors" and computerchioce == "paper":
        print("you won")
        userwins += 1

    else:
        print("you lose")
        computerwins += 1

print("you won", userwins, "times.")
print("you computer", userwins, "times.")
print("goodbye!")