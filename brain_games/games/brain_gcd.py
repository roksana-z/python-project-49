import math
import random


def get_correct_answer(*args):
    a, b = args[0]
    return str(math.gcd(a, b))


def show_question(*args):
    a, b = args[0]
    return f'{a} {b}'


def get_question():
    a = random.randint(1, 15)
    b = random.randint(1, 15)
    return (a, b)


def show_game_description():
    print('Find the greatest common divisor of given numbers.')
