def thumb():
    code = 'thumb'
    return code


def six():
    code = 'six'
    return code


def ok():
    code = 'ok'
    return code


def peace():
    code = 'peace'
    return code


def adduct():
    code = 'adduct'
    return code


def abduct():
    code = 'abduct'
    return code


def ring():
    code = 'ring'
    return code


def fist():
    code = 'fist'
    return code


def waveIn():
    code = 'waveIn'
    return code


def waveOut():
    code = 'waveOut'
    return code


def seven():
    code = 'seven'
    return code


def relax():
    code = 'relax'
    return code


def default():
    code = 'relax'
    return code


class code2ges:
    switcher = {}

    def __init__(self):
        self.switcher = {
            '0': thumb,
            '1': six,
            '2': ok,
            '3': peace,
            '4': adduct,
            '5': abduct,
            '6': ring,
            '7': fist,
            '8': waveIn,
            '9': waveOut,
            '10': seven,
            '11': relax
        }

    def outer(self, numGes):
        func = self.switcher.get(str(numGes), default)
        code = func()
        return code
