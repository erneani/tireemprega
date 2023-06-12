"""
Processor Module.
This module gets the user data and matchs it with a course.
"""


import csv
import os
import openai

from dotenv import load_dotenv
from src.processor.prompts import PROMPT_MAPPING


load_dotenv()
openai.api_key = os.getenv('OPENAI_SECRET_KEY')


def match_user_course(user_data):
    """Matches the user data with the best course"""
    user_tech_information = process_user_data(user_data)
    courses_list = load_csv_database()

    return 'Match'


def process_user_data(user_data):
    """Processes all data from User using ChatGPT"""
    processed_user_data = {}

    for prompt_tuple in PROMPT_MAPPING.items():
        chatgpt = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt_tuple[1](user_data[prompt_tuple[0]])
        )

        processed_user_data[prompt_tuple[0]] = chatgpt.choices[0].message.content

    return processed_user_data


def load_csv_database():
    """Loads our CSV file into an courses List"""
    with open('datasets/tech-courses-modified.csv', 'r') as courses_file:
        courses_reader_spam = csv.reader(courses_file)
        courses_list = list(courses_reader_spam)

        print(courses_list)

        return courses_list
