#!/usr/bin/env python3.

from brain_games.game import play_game
from brain_games.games.brain_progression import get_correct_answer,\
    get_question, show_game_description, show_question


def main():
    play_game(get_question, show_game_description,
              show_question, get_correct_answer)


if __name__ == '__main__':
    main()
