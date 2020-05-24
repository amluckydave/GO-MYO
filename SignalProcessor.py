from scipy import signal
import numpy as np


def rectified(rawEMG):
    rectifiedEMG = abs(rawEMG)
    return rectifiedEMG


def filtered(Fb, Fa, rawEMG):
    filteredEMG = signal.filtfilt(Fb, Fa, rawEMG, axis=0)
    return filteredEMG


class SignalProcessor:
    def __init__(self, rawEMG,):
        self.rawEMG = rawEMG.astype(np.float64)

        order = 4
        fs = 0.05
        self.Fb, self.Fa = signal.butter(order, fs, 'low')

        self.rectified = True
        self.filtered = True

    def process(self):
        if self.rectified:
            self.rawEMG = rectified(self.rawEMG)
        if self.filtered:
            self.rawEMG = filtered(self.Fb, self.Fa, self.rawEMG)

        return self.rawEMG
