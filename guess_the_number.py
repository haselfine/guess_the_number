import random

correct = 'you guessed correctly!'
<<<<<<< HEAD
too_low = 'too low!!!!!'
=======
too_low = 'Too low!!'
>>>>>>> dbf0cdd09ba7123b6ef715b446cb0b1c6eb1333c
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


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


def main():

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


if __name__ == '__main__':
    main()