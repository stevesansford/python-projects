import random

# initialize default game state
game_state = [1, 100, 10, 0]


def game_settings(game_state):
    print('\nPlease configure your game:\n')
    game_state[0] = int(
        input(f'Enter the lower number: (Cur: {game_state[0]}) '))
    game_state[1] = int(
        input(f'Enter the higher number: (Cur: {game_state[1]}) '))
    game_state[2] = int(
        input(f'Enter the maximum number of guesses: (Cur: {game_state[2]}) '))
    game_state[3] = 0

    return


def start_game(game_state):

    number = random.randint(game_state[0], game_state[1])
    counter = 1
    for _ in range(game_state[2]):
        try:
            guess = int(input(
                f'Guess the number between {game_state[0]} and {game_state[1]}: '))
        except ValueError:
            print('You need to make better choices!')
            continue

        for i in range(game_state[0], game_state[1]):
            if guess == number:
                print(f'You nailed it! The number was {number}!')
                game_state[3] = counter

                while True:
                    restart = input("Do you want to play again? (y/n): ")
                    if restart.lower() == 'y':
                        start_game(game_state)
                    elif restart.lower() == 'n':
                        return
                    else:
                        print("That is not a vaild choice")
            elif guess < number:
                print("You're too low!")
                counter += 1
                break
            elif guess > number:
                print("You're too high!")
                counter += 1
                break
            else:
                break
    print('\nI regret to inform you that you have failed to guess the number within the allotted number of guesses!\n')


def main():
    while True:
        print('\nWelcome to the Number Guessing Game!')
        print('-' * 36)
        print(f'High Score: {game_state[3]}')
        print('')
        print('1. START')
        print('2. Settings')
        print('3. Exit')
        print('')
        menu_choice = input('Select Option: ')

        if menu_choice == '1':
            start_game(game_state)
        elif menu_choice == '2':
            game_settings(game_state)
        elif menu_choice == '3':
            print('Thanks for playing!')
            exit()
        else:
            print('You need to make better choices!')


main()
