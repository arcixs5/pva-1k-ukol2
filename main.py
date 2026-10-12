import random

moznosti = ["rock", "scissors", "paper"]

print("=== ROCK, SCISSORS, PAPER ===")
wins = 0
prohry = 0
remizi = 0
while True:
    print(f"wins {wins} / loses {prohry} / ties {remizi} "
          )
    hrac = input("Pick rock, paper, scissors or end").lower()


    if hrac == "end":
        print("Goodbye!")
        break

    if hrac not in moznosti:
        print("Invalid! Try again.")
        continue


    pocitac = random.choice(moznosti)

    print(f"You: {hrac}")
    print(f"Computer: {pocitac}")

    if hrac == pocitac:
        print("tie! 🤝")
        remizi += 1
    elif (
        (hrac == "rock" and pocitac == "scissors")
        or (hrac == "scissors" and pocitac == "paper")
        or (hrac == "paper" and pocitac == "rock")
    ):
        wins += 1
        print("You win!")
    else:
        prohry += 1
        print("You lose!")





