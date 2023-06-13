"""
Stores all prompt functions to be used on ChatPGT queries.
"""


def get_tech_skills_list(user_input):
    """Prompt to get the skills from the user Input"""
    prompt = f"""
    I want you to act as a career counselor. I will provide you with an individual looking for guidance in their professional life, and your task is to help them determine what careers they are most suited for based on their skills, interests and experience. You should also conduct research into the various options available, explain the job market trends in different industries and advice on which qualifications would be beneficial for pursuing particular fields.

    I'm building an app for recommending courses based on user input with Python.
    Please, help me deduce the keywords of the user input related to the skills, technologies and programming languages necessary to achieve his objective of learning.

    The user input is

    '{user_input}'

    Give me back a python list data structure with a minimum of 5 items that you could extract and deduce from the user input regarding to technology, skill and programming language. For example, if the user wants to learn about the frontend area you could deduce HTML, CSS and JS. Note: I want only a python list without any explanation. Note 2: Don't be too broad, try to give me more specific skills, technologies and programming languages. Note 3: Order the list as it was like a roadmap, the basic knowledge first and after the complex ones.
    """
    messages = _prepare_message(prompt)

    return messages


def get_interested_area(user_input):
    """Prompt to get the interest area from the user Input"""
    prompt = f"Give me the interest area from the sentence: {user_input}. Don't write any other text."
    messages = _prepare_message(prompt)

    return messages


def _prepare_message(prompt):
    """Generates the System message to ChatGPT"""
    return [
        {
            "role": "system",
            "content": "You are a helpful and objective assistant"
        },
        {
            "role": "user",
            "content": prompt
        }
    ]


PROMPT_MAPPING = {
    'interested_skills': get_tech_skills_list,
    'interest_area': get_interested_area,
}
