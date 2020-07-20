import random

#prompts to start the game and acquire username
name = input('\nWhat is your name? ')
start_game = input(f"\nHello, {name.capitalize()}! Would you like to play Rock, Paper, Scissors? (Enter Y to start) ")

#scoreboard counter
total_games = 0
ai_games = 0
user_games = 0
draws = 0
game_on = False

#Initialize game
if start_game.lower() == 'y':
    game_on = True

#Gameplay loop
while game_on:
    try:
        user_choice = int(input("\nEnter 1 for Rock, 2 for Paper, 3 for Scissors: "))

    except ValueError:
        print("Please enter a value of 1, 2, or 3!\n")

    else:
        ai_choice = random.randint(1,3)
        if user_choice == ai_choice:
            total_games += 1
            draws += 1
            print("\nIt's a draw!")
            print(f"Total Games: {total_games}")
            print(f"Total Draws: {draws}")
            print(f"AI Wins: {ai_games}")
            print(f"{name.capitalize()} Wins: {user_games}")
            another_one = input('\nWould you like to play another round? (Enter "Y" to continue) ')
            if another_one.lower() == 'y':
                continue
            else:
                break

        elif user_choice == 1 and ai_choice == 2:
            total_games += 1
            ai_games += 1
            print(f"\nTough luck, {name.capitalize()}! Paper beats Rock! The AI won!")
            print(f"Total games: {total_games}")
            print(f"Total Draws: {draws}")
            print(f"AI Wins: {ai_games}")
            print(f"{name.capitalize()} Wins: {user_games}")
            another_one = input('\nWould you like to play another round? (Enter "Y" to continue) ')
            if another_one.lower() == 'y':
                continue
            else:
                break

        elif user_choice == 1 and ai_choice == 3:
            total_games += 1
            user_games += 1
            print(f"\nCongrats, {name.capitalize()}! Rock beats Scissors! You've won!")
            print(f"Total Games: {total_games}")
            print(f"Total Draws: {draws}")
            print(f"AI Wins: {ai_games}")
            print(f"{name.capitalize()} Wins: {user_games}")
            another_one = input('\nWould you like to play another round? (Enter "Y" to continue) ')
            if another_one.lower() == 'y':
                continue
            else:
                break

        elif user_choice == 2 and ai_choice == 1:
            total_games += 1
            user_games += 1
            print(f"\nCongrats, {name.capitalize()}! Rock beats Scissors! You've won!")
            print(f"Total Games: {total_games}")
            print(f"Total Draws: {draws}")
            print(f"AI Wins: {ai_games}")
            print(f"{name.capitalize()} Wins: {user_games}")
            another_one = input('\nWould you like to play another round? (Enter "Y" to continue) ')
            if another_one.lower() == 'y':
                continue
            else:
                break

        elif user_choice == 2 and ai_choice == 3:
            total_games += 1
            ai_games += 1
            print(f"\nTough luck, {name.capitalize()}, the AI won!")
            print(f"Total Games: {total_games}")
            print(f"Total Draws: {draws}")
            print(f"AI Wins: {ai_games}")
            print(f"{name.capitalize()} Wins: {user_games}")
            another_one = input('\nWould you like to play another round? (Enter "Y" to continue) ')
            if another_one.lower() == 'y':
                continue
            else:
                break

        elif user_choice == 3 and ai_choice == 1:
            total_games += 1
            ai_games += 1
            print(f"\nTough luck, {name.capitalize()}, the AI won!")
            print(f"Total games: {total_games}")
            print(f"Total Draws: {draws}")
            print(f"AI Wins: {ai_games}")
            print(f"{name.capitalize()} Wins: {user_games}")
            another_one = input('\nWould you like to play another round? (Enter "Y" to continue) ')
            if another_one.lower() == 'y':
                continue
            else:
                break

        elif user_choice == 3 and ai_choice == 2:
            total_games += 1
            user_games += 1
            print(f"\nCongrats, {name.capitalize()}! You've won!")
            print(f"Total Games: {total_games}")
            print(f"Total Draws: {draws}")
            print(f"AI Wins: {ai_games}")
            print(f"{name.capitalize()} Wins: {user_games}")
            another_one = input('\nWould you like to play another round? (Enter "Y" to continue) ')
            if another_one.lower() == 'y':
                continue
            else:
                break

#post-game summary
print(f"\nGoodbye, {name.capitalize()}!")
print(f"\nFinal Score Count:")
print(f"Total Games: {total_games}")
print(f"Total Draws: {draws}")
print(f"AI Wins: {ai_games}")
print(f"{name.capitalize()} Wins: {user_games}\n")
