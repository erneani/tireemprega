"""
CLI module.
This module is used to build the visual interface on CLI.
"""

import pyfiglet

from src.cli.questions import QUESTIONS


def ask_questions():
    """Requests all data from the user"""
    user_data = {}

    for record_tuple in QUESTIONS.items():
        user_data[record_tuple[0]] = input(QUESTIONS[record_tuple[0]] + " ")

    print(user_data)


def beautiful_cli_name():
    """Write that dope name"""
    print(pyfiglet.figlet_format('ReEmprega'))


def run_app():
    """Places all functions in order to run CLI"""
    beautiful_cli_name()
    ask_questions()
