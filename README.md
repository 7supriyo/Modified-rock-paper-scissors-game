# Modified-rock-paper-scissors-game
Added a 4th category - 'Water" in ROCK-PAPER-SCISSORS GAME

If you select 'Water' and your opponent selects 'Paper' or 'Scissors' - then the person selecting 'Water' wins. However, 'Rock' can defeat 'Water'.
At the end - publish round-wise winners so it is easier to see the winner of the overall match.
![My first design 1](https://github.com/user-attachments/assets/2c8b456f-fc98-42e1-a749-2781a5d47565)
Here's a step-by-step guide:
 ### Step 1: Set Up Your Environment
1. Install Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install VS Code**: Download and install Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/).

### Step 2: Create a New Python File
1. Open VS Code.
2. Create a new file and save it with a `.py` extension, e.g., `rock_paper_scissors_water.py`.

### Step 3: Write the Game Code

Here's a simple implementation of the game:

```python
import random

# Define the choices
choices = ["Rock", "Paper", "Scissors", "Water"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "Rock" and computer_choice in ["Scissors", "Water"]) or \
         (user_choice == "Paper" and computer_choice in ["Rock", "Water"]) or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Water" and computer_choice in ["Paper", "Scissors"]):
        return "User"
    else:
        return "Computer"

# Function to play a single round
def play_round():
    user_choice = input("Enter your choice (Rock, Paper, Scissors, Water): ").capitalize()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter Rock, Paper, Scissors, or Water: ").capitalize()
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    print(f"Round result: {winner} wins!")
    return winner

# Main function to play multiple rounds and determine the overall winner
def main():
    rounds = int(input("Enter the number of rounds: "))
    user_wins = 0
    computer_wins = 0
    draws = 0
    
    for _ in range(rounds):
        winner = play_round()
        if winner == "User":
            user_wins += 1
        elif winner == "Computer":
            computer_wins += 1
        else:
            draws += 1
    
    print("\nFinal Results:")
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Draws: {draws}")
    
    if user_wins > computer_wins:
        print("Overall winner: User")
    elif computer_wins > user_wins:
        print("Overall winner: Computer")
    else:
        print("Overall result: It's a draw!")

if __name__ == "__main__":
    main()
```

### Step 4: Run the Game
1. Open a terminal in VS Code.
2. Navigate to the directory where your Python file is saved.
3. Run the game by typing `python rock_paper_scissors_water.py` and pressing Enter.

This code will prompt the user to enter their choice, randomly select a choice for the computer, and determine the winner for each round. After all rounds are played, it will display the overall winner based on the number of rounds won by each player.

