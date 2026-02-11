import random
import string


def generate_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


def generate_random_user_id(length=126):
    # chars = string.ascii_letters + string.digits
    # return "".join(random.choice(chars) for _ in range(length))
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))