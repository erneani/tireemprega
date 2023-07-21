"""
CLI module.
This module is used to build the visual interface on CLI.
"""

import pyfiglet

from src.processor.processor import updated_match_user_course
from src.cli.questions import QUESTIONS


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ask_questions():
    """Requests all data from the user"""
    user_data = {}

    for record_tuple in QUESTIONS.items():
        user_data[record_tuple[0]] = input(QUESTIONS[record_tuple[0]] + " ")

    match = updated_match_user_course(user_data)

    show_match_result(user_data, match)


def beautiful_cli_name():
    """Write that dope name"""
    print(pyfiglet.figlet_format('ReEmprega'))


def show_match_result(user_data, match):
    """Returns a beautiful message with the Match Course"""
    print(f"Hey {user_data['name']}, that's nice! Seems like the course {bcolors.OKGREEN}{match[0]['title']}{bcolors.ENDC} will be the perfect match for you! \nCheck out this URL {match[0]['url']} to learn!")
    print(f"\nHere are some courses that might be a good fit for you:")
    for idx, course in enumerate(match[1:5]):
        print(f"{idx + 1}. {bcolors.WARNING}{course['title']}{bcolors.ENDC}: {course['url']}")


def run_app():
    """Places all functions in order to run CLI"""
    beautiful_cli_name()
    ask_questions()
