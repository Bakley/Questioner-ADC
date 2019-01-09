"""Validation function to check app."""
import re


def check_for_empty_string(input_data):
    """
    Checks if data presented by a user is empty.
    """

    if input_data.strip() == "":
        return 'All fields are required'
    return None


def check_number_format(input_number):
    """
    Check if value is a number.
    """
    try:
        int(input_number)
    except ValueError:
        return False
    else:
        if int(input_number) <= 0:
            return False
        return True


def check_name_format(input_name):
    """
    Checks if name is 5 Characters and No integer allowed.
    """
    length_regex = re.compile(r'.{5,}')
    length = True if length_regex.search(input_name) is not None else False

    uppercase_regex = re.compile(r'[A-Z]')
    uppercase = True if uppercase_regex.search(
        input_name) is not None else False

    return(length and uppercase is True)


def check_username_format(username):
    """
    Username should be 8 character long
    Contain special character
    Has an Integer and has a capitalize letter
    """
    length_regex = re.compile(r'.{8,}')
    length = True if length_regex.search(username) is not None else False

    uppercase_regex = re.compile(r'[A-Z]')
    uppercase = True if uppercase_regex.search(username) is not None else False

    special_char_regex = re.compile(r'[_@]')
    special_char = True if special_char_regex.search(
        username) is not None else False

    number_regex = re.compile(r'[0-9]')
    number = True if number_regex.search(username) is not None else False

    return(length and uppercase and special_char and number is True)


def check_password_strength(password):
    """
    Password should be 8 character long
    Contain special character
    Has an Integer
    Has a capital letter
    """
    length_regex = re.compile(r'.{8,}')
    length = True if length_regex.search(password) is not None else False

    uppercase_regex = re.compile(r'[A-Z]')
    uppercase = True if uppercase_regex.search(password) is not None else False

    special_char_regex = re.compile(r'[_@]')
    special_char = True if special_char_regex.search(
        password) is not None else False

    number_regex = re.compile(r'[0-9]')
    number = True if number_regex.search(password) is not None else False
    return(length and uppercase and special_char and number is True)


def check_email_format(input_email):
    """
    Should be email worthy.
    """
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",
                input_email):
        res = True
    else:
        res = False
    return res
