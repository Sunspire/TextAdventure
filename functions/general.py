import json

color_codes = {
    'reset': 0,
    'black': 30,
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'magenta': 35,
    'cyan': 36,
    'gray': 37
}

def output(text, color_code):
    if color_codes.get(color_code) is None:
        return '\33[31mfuntions > general > output > Unknown color'

    return f'\33[{color_codes.get(color_code)}m{text}'

def is_json(the_json):
    try:
        json_string = json.loads(the_json)
    except ValueError as e:
        return False
    return True