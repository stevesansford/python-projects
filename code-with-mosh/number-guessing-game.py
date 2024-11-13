import random

print('\nWelcome to the Dice Rolling Game!\n')

counter = 1

while True:
    user_choice = input("Roll the dice? (y/n): ")

    if user_choice.lower() == 'y':
        number_of_dice = input('How many dice would you like to roll? ')
        list_of_results = []

        for i in range(int(number_of_dice)):
            list_of_results.append(random.randint(1, 6))

        print(f'\nRoll {counter}: {list_of_results}\n')
        counter += 1
    elif user_choice.lower() == 'n':
        print('\nExiting game...\n')
        break
    else:
        print('\nYou should make better choices!\n')

