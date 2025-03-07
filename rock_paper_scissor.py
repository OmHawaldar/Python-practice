
import random

def play_game():
  user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
  computer_choice = random.choice(["rock", "paper", "scissors"])

  print("You chose: ",user_choice)
  print("Computer chose: ",computer_choice)

  if user_choice == computer_choice:
    print("It's a tie!")
  elif user_choice == "rock":
    if computer_choice == "scissors":
      print("You win!")
    else:
      print("Computer wins!")
  elif user_choice == "paper":
    if computer_choice == "rock":
      print("You win!")
    else:
      print("Computer wins!")
  elif user_choice == "scissors":
    if computer_choice == "paper":
      print("You win!")
    else:
      print("Computer wins!")
  else:
    print("Invalid input. Please choose rock, paper, or scissors.")

while True:
  play_game()
  play_again = input("Do you want to play again? (yes/no): ").lower()
  if play_again != "yes":
    break
