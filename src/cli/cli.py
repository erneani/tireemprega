"""
CLI module.
This module is used to build the visual interface on CLI.
"""

import pyfiglet


def ask_questions():
    """Requests all data from the user"""
    user_data = {}
    user_data['name'] = input("What is your name? ")
    user_data['age'] = input("What is your age? ")
    user_data['current_profession'] = input("What is you current profession? ")
    user_data['interest_area'] = input("What is your area of interest? ")
    user_data['experience'] = (
        input("How many years of experience you have in Tech? "))
    user_data['interested_skills'] = (
        input("Which skills are you interested in? "))
    user_data['english_level'] = input("What is your english level? ")
    user_data['time_to_job'] = (
        input("In how many months do you want to achieve this Job? "))
    user_data['dedication_time'] = input("How much hours/day you can study? ")
    user_data['soft_skills'] = input("Which Soft Skills do you have? ")

    print(user_data)


def beautiful_cli_name():
    """Write that dope name"""
    print(pyfiglet.figlet_format('ReEmprega'))


def run_app():
    """Places all functions in order to run CLI"""
    beautiful_cli_name()
    ask_questions()
