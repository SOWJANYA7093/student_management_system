import re


def validate_email(email):

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        return True

    return False


def validate_age(age):

    if age.isdigit():

        age = int(age)

        if age > 0 and age <= 100:
            return True

    return False


def validate_date(date):

    pattern = r"^\d{4}-\d{2}-\d{2}$"

    if re.match(pattern, date):
        return True

    return False