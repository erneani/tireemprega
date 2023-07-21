"""
Processor Module.
This module gets the user data and matchs it with a course.
"""


import csv
import os
import openai

from ast import literal_eval
from dotenv import load_dotenv
from src.processor.prompts import PROMPT_MAPPING


load_dotenv()
openai.api_key = os.getenv('OPENAI_SECRET_KEY')


def score_course(user_interests, user_data, course):
    score = 0.0

    matching_keywords = user_interests.intersection(course['keywords'])
    score += len(matching_keywords)

    score += course['rating']

    if user_data['level'].lower() in course['level'].lower():
        score += 300
    elif 'all' in course['level'].lower():
        score += 150
    else:
        score -= 300

    if float(course['price']) <= float(user_data['price']):
        score += 200
    else:
        score -= 200

    if float(course['duration']) <= float(user_data['duration']):
        score += 200
    else:
        score -= 200

    return score


def updated_match_user_course(user_data, top_n=5):
    user_tech_information = process_user_data(user_data)
    user_interests = extract_keywords(user_tech_information['interested_skills'] + " " + user_tech_information['interest_area'])

    courses = load_csv_database_with_keywords()

    scored_courses = [{"course": course, "score": score_course(user_interests, user_data, course)} for course in courses]

    top_courses = sorted(scored_courses, key=lambda x: x['score'], reverse=True)[:top_n]

    return [course['course'] for course in top_courses]


def match_user_course(user_data):
    """Matches the user data with the best course"""
    user_tech_information = process_user_data(user_data)
    courses_list = load_csv_database()

    filtered_courses = []

    for skill in literal_eval(user_tech_information['interested_skills']):
        for course in courses_list:
            if skill in course['title'] and course['rating'] > 0.76:
                filtered_courses.append(course)

    return filtered_courses


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
        courses_list = courses_list[1:]
        useful_courses_list = []

        for course in courses_list:
            useful_courses_list.append({
                "title": course[1],
                "url": course[2],
                "rating": 0 if course[6] == '' else float(course[6])
            })

        return useful_courses_list


def extract_keywords(text):
    return set(text.lower().split())


def load_csv_database_with_keywords():
    csv_path = os.path.join("datasets", "tech-courses-modified.csv")

    courses = []

    with open(csv_path, 'r', encoding="utf-8") as courses_file:
        courses_reader = csv.reader(courses_file)
        next(courses_reader)

        for row in courses_reader:
            title = row[1]
            url = row[2]
            price = 0 if row[3] == '' else float(row[3])
            level = row[5]
            duration = 0 if row[7] == '' else float(row[7])
            rating = 0 if row[6] == '' else float(row[6])
            keywords = extract_keywords(title)
            courses.append({"title": title, "url": url, "rating": rating, "keywords": keywords, "price": price, "level": level, "duration": duration})

    return courses
