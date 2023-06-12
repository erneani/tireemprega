"""
CLI module.
This module is used to build the visual interface on CLI.
"""

import pyfiglet

from src.processor.processor import match_user_course
from src.cli.questions import QUESTIONS


def ask_questions():
    """Requests all data from the user"""
    user_data = {}

    for record_tuple in QUESTIONS.items():
        user_data[record_tuple[0]] = input(QUESTIONS[record_tuple[0]] + " ")

    match = match_user_course(user_data)

    show_match_result(user_data, match)


def beautiful_cli_name():
    """Write that dope name"""
    print(pyfiglet.figlet_format('ReEmprega'))


def show_match_result(user_data, match):
    """Returns a beautiful message with the Match Course"""
    print(f"Hey {user_data.name}, that's nice! Seems like the course {match.course.title} will be the perfect match for you!")


def run_app():
    """Places all functions in order to run CLI"""
    beautiful_cli_name()
    ask_questions()
