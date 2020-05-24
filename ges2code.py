import numpy as np


def thumb():
    code = np.zeros(12, int)
    code[0] = 1
    return code


def six():
    code = np.zeros(12, int)
    code[1] = 1
    return code


def ok():
    code = np.zeros(12, int)
    code[2] = 1
    return code


def peace():
    code = np.zeros(12, int)
    code[3] = 1
    return code


def adduct():
    code = np.zeros(12, int)
    code[4] = 1
    return code


def abduct():
    code = np.zeros(12, int)
    code[5] = 1
    return code


def ring():
    code = np.zeros(12, int)
    code[6] = 1
    return code


def fist():
    code = np.zeros(12, int)
    code[7] = 1
    return code


def waveIn():
    code = np.zeros(12, int)
    code[8] = 1
    return code


def waveOut():
    code = np.zeros(12, int)
    code[9] = 1
    return code


def seven():
    code = np.zeros(12, int)
    code[10] = 1
    return code


def relax():
    code = np.zeros(12, int)
    code[11] = 1
    return code


def default():
    code = np.zeros(12, int)
    code[11] = 1
    return code


class ges2code:
    switcher = {}

    def __init__(self):
        self.switcher = {
            't': thumb,
            'x': six,
            'k': ok,
            'p': peace,
            'ad': adduct,
            'ab': abduct,
            'g': ring,
            'f': fist,
            'i': waveIn,
            'o': waveOut,
            'v': seven,
            'r': relax
        }

    def outer(self, String):
        func = self.switcher.get(String, default)
        code = func()
        return code
