import random


def get_random_operator():
    operators = ['-', '+', '*']
    return operators[random.randint(0, 2)]


def get_correct_answer(*args):
    a, operator, b = args[0]
    match operator:
        case '-':
            return a - b
        case '+':
            return a + b
        case '*':
            return a * b
        case _:
            return


def show_question(*args):
    a, operator, b = args[0]
    return f'{a} {operator} {b}'


def get_question():
    a = random.randint(1, 15)
    b = random.randint(1, 15)
    operator = get_random_operator()
    return (a, operator, b)


def show_game_description():
    print('What is the result of the expression?')
