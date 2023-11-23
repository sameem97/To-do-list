import re


def check_date_format(date):
    date_format = re.compile(r"\d{2}/\d{2}/\d{2}(?:\d{2})?$")
    if date_format.match(date):
        return True
    return False
