import math
import random


def is_prime(number):
    if number < 2:
        return False
    sqrt_num = int(math.sqrt(number))
    for i in range(2, sqrt_num + 1):
        if number % i == 0:
            return False
    return True


def get_correct_answer(number):
    return 'yes' if is_prime(number) else 'no'


def show_question(question):
    return question


def get_question():
    return random.randint(1, 100)


def show_game_description():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
