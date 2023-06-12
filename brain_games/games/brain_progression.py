import random


def get_correct_answer(*args):
    progression, hidden_position = args[0]
    return str(progression[hidden_position])


def show_question(*args):
    progression, index_of_hidden_number = args[0]
    new_progression = progression[:]
    new_progression[index_of_hidden_number] = '..'
    return ' '.join(map(str, new_progression))


def generate_arithmetic_progression(start_point, step, progression_length):
    progression = []
    for i in range(progression_length):
        progression.append(start_point + i*step)
    return progression


def get_question():
    progression_length = 10
    step = random.randint(1, 10)
    start_point = random.randint(1, 10)
    index_of_hidden_number = random.randint(0, progression_length - 1)
    progression = generate_arithmetic_progression(
        start_point, step, progression_length)
    return (progression, index_of_hidden_number)


def show_game_description():
    print('What number is missing in the progression?')
