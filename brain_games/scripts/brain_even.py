#!/usr/bin/env python3.
import prompt
import random
from brain_games.scripts.brain_games import greet

def is_even(number):
     return True if number % 2 == 0 else False

def generate_random_number():
    return random.randint(1, 15)

def check_is_even(number):
    return 'yes' if is_even(number) else 'no'

def brain_even():
    random_number = generate_random_number()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    user_name = prompt.string('May I have your name? ')
    print('Hello,' + user_name)
    counter = 0
    while counter < 3:
        print('Question:' + str(random_number))
        user_answer = prompt.string('Your answer:')
        correct_answer = check_is_even(random_number)
        if user_answer == correct_answer:
            print('Correct!')
            counter = counter + 1
            random_number = generate_random_number()
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}. Let\'s try again, {user_name}!')
            return

    print(f'Congratulations {user_name}!')
    return

def main():
    greet()
    brain_even()

if __name__ == '__main__':
    main()