import numpy as np


def thumb():
    code = 't'
    return code


def six():
    code = 'x'
    return code


def ok():
    code = 'k'
    return code


def peace():
    code = 'p'
    return code


def adduct():
    code = 'ad'
    return code


def abduct():
    code = 'ab'
    return code


def ring():
    code = 'g'
    return code


def fist():
    code = 'f'
    return code


def waveIn():
    code = 'i'
    return code


def waveOut():
    code = 'o'
    return code


def seven():
    code = 'v'
    return code


def relax():
    code = 'r'
    return code


def default():
    code = 'stop'
    return code


class ges2code:
    switcher = {}

    def __init__(self):
        self.switcher = {
            '1': thumb,
            '2': six,
            '3': ok,
            '4': peace,
            '5': adduct,
            '6': abduct,
            '7': ring,
            '8': fist,
            '9': waveIn,
            '10': waveOut,
            '11': seven,
            '12': relax
        }

    def outer(self, Num):
        func = self.switcher.get(str(Num), default)
        code = func()
        return code
