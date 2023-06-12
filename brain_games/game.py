import prompt
from brain_games.scripts.brain_games import greet


def play_game(
        get_question,
        show_game_description,
        show_question, get_correct_answer):
    greet()
    user_name = prompt.string('May I have your name? ')
    print('Hello,' + user_name)
    show_game_description()
    question = get_question()
    counter = 0
    while counter < 3:
        print('Question:' + str(show_question(question)))
        user_answer = prompt.string('Your answer:')
        correct_answer = str(get_correct_answer(question))
        if user_answer == correct_answer:
            print('Correct!')
            counter = counter + 1
            question = get_question()
        else:
            print(
                f'{user_answer} is wrong answer ;(.'
                f'Correct answer was {correct_answer}.'
                f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations {user_name}!')
