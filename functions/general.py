def output(text, color_code):
    color_codes = {}
    color_codes['reset'] = 0  # resets all colors
    color_codes['black'] = 30
    color_codes['red'] = 31
    color_codes['green'] = 32
    color_codes['yellow'] = 33
    color_codes['blue'] = 34
    color_codes['magenta'] = 35
    color_codes['cyan'] = 36
    color_codes['gray'] = 37

    if color_codes.get(color_code) is None:
        return '\33[31mfuntions > general > output > Unknown color'
    else:
        return '\33[{code}m'.format(code=color_codes.get(color_code)) + text
