import random

correct = 'you guessed correctly!'
too_low = 'Too low!!'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 1000


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    try:
        return int(input('Guess the secret number? '))
    except:
        print("Only digits allowed")
    


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def play_again():
    '''user chooses whether to play again or not'''
    while True:
        user_choice = input('Would you like to play again? y or n?')
        if user_choice.lower() == "y" or user_choice.lower() == "n":
            return user_choice
            break
        else:
            print('Answer must be "y" or "n"')


def main():

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
    

        number_of_guesses += 1
        print(result)

        if result == correct:
            print(f'You got it right in {number_of_guesses} attempt(s).')
        (low, high) = configure_range()
        secret = generate_secret(low, high)
        number_of_guesses = 0

        while True:
            guess = get_guess()
            result = check_guess(guess, secret)

            number_of_guesses += 1
            print(result)

            if result == correct:
                print(f'You got it right in {number_of_guesses} attempt(s).')
                break
        replay = play_again()
        if replay == "y":
            continue
        else:
            break


if __name__ == '__main__':
    main()