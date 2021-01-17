import random

def random_number():
    a = random.randint(1, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    while not (a != b and b != c and c != a and a != d and b != d and c != d):
        a = random.randint(1, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
    return [str(a), str(b), str(c), str(d)]


def play():
    number = random_number()

    print("Hi there!\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")

    no_guesses = 0

    no_bulls = 0
    continue_game = '1'

    while no_bulls != 4 and continue_game in ['1', 'Yes', 'yes', 'YES']:
        no_bulls = 0
        no_cows = 0
        no_guesses += 1
        guess = input("Enter a number: ")

        if len(guess) != 4:
            print("You must enter a 4-digit number!")
        else:
            guess = list(guess)

            for i in range(len(guess)):
                if guess[i] == number[i]:
                    no_bulls += 1
                if guess[i] != number[i] and guess[i] in number:
                    no_cows += 1

            print('{} bulls, {} cows'.format(no_bulls, no_cows))

            if no_bulls == 4:
                print("Winner!\n You've guessed the right number in {} guesses!".format(no_guesses))
            else:
                continue_game = input("Do you wish to continue? [1 -- Yes, 0 -- No]")

                if continue_game not in ['1', 'Yes', 'yes', 'YES'] and no_bulls != 4:
                    print("Looser\n fyi the correct number was {}".format(''.join(number)))



play()










