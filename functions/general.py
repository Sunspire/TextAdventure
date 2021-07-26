def output(text, colorCode):
    color_code = {}
    color_code['reset'] = 0 #resets all colors
    color_code['black'] = 30
    color_code['red'] = 31
    color_code['green'] = 32
    color_code['yellow'] = 33
    color_code['blue'] = 34
    color_code['magenta'] = 35
    color_code['cyan'] = 36
    color_code['gray'] = 37
    
    if color_code.get(colorCode) is None:
        return '\33[31mfuntions > general > output > Unknown color'
    else:
        return ('\33[{code}m'.format(code=color_code.get(colorCode)) + text)

