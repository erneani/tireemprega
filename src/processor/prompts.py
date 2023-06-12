"""
Stores all prompt functions to be used on ChatPGT queries.
"""


def get_tech_skills_list(user_input):
    """Prompt to get the skills from the user Input"""
    prompt = f"Create a Python list with all skills from the following sentence: '{user_input}'. Write ONLY the list."
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
