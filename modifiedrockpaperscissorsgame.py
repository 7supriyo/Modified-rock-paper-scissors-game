import random

you_score = 0
computer_score = 0
round_winners = []

def get_user_choice():
    """
    Function to get user's choice (rock, paper, scissors, or water)
    """
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors, or water): ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors', 'water']:
            return user_choice
        else:
            print("Invalid choice! Please enter 'rock', 'paper', 'scissors', or 'water'.")

def get_computer_choice():
    """
    Function to randomly generate computer's choice
    """
    return random.choice(['rock', 'paper', 'scissors', 'water'])

def determine_winner(user_choice, computer_choice):
    """
    Function to determine the winner of the game
    """
    global you_score, computer_score, round_winners

    if user_choice == computer_choice:
        round_winners.append("Tie")
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        you_score += 1
        round_winners.append("You")
        return "Congratulations! You win this round!"
    elif user_choice == 'water' and (computer_choice == 'paper' or computer_choice == 'scissors'):
        you_score += 1
        round_winners.append("You")
        return "Congratulations! You win this round!"
    else:
        computer_score += 1
        round_winners.append("Computer")
        return "Computer wins this round!"


"""
Function to play the game
"""
print("Let's play Rock, Paper, Scissors, Water!")
print("\n")
n = int(input("How many rounds do you want to play? "))
count = 1

while n > 0:
    print(f"Round: {count}")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))
    count += 1
    n -= 1

print("\nRound-wise Winners:")
for i, winner in enumerate(round_winners, start=1):
    print(f"Round {i}: {winner}")

if you_score > computer_score:
    print("You won the overall match!")
elif you_score < computer_score:
    print("Computer won the overall match!")
else:
    print("The match is tied!")
