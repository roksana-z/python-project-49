import random


def is_even(number):
    return True if number % 2 == 0 else False


def get_correct_answer(number):
    return 'yes' if is_even(number) else 'no'


def get_question():
    return random.randint(1, 15)


def show_question(question):
    return question


def show_game_description():
    print('Answer "yes" if the number is even, otherwise answer "no".')
