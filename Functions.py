import numpy as np


def feature_mav(emg):
    MAV = np.sum(abs(emg), axis=0) / np.shape(emg)[0]
    return MAV


def feature_wl(emg):
    WL = np.sum(abs(np.diff(emg, axis=0)), axis=0)
    return WL


def feature_ssc(emg):
    epsilon = 1e-3
    rows, cols = np.shape(emg)
    SSC = np.zeros((1, cols))

    for colIdx in range(cols):
        signal = emg[:, colIdx]
        for idx in range(1, rows - 1):
            x_i = signal[idx - 1]
            x_i_2 = signal[idx]
            x_i_3 = signal[idx + 1]
            if (x_i - x_i_2) * (x_i_2 + x_i_3) >= epsilon:
                SSC[:, colIdx] = SSC[:, colIdx] + 1
    return SSC


def feature_rms(emg):
    RMS = np.sqrt(np.mean(np.square(emg), axis=0))
    return RMS


def feature_hjorth(emg):
    ACT = lambda x: np.var(x, axis=0)
    MOB = lambda x: np.sqrt(ACT(np.diff(x, axis=0)) / ACT(x))
    COMPLX = lambda x: MOB(np.diff(x, axis=0)) / MOB(x)
    np.seterr(divide='ignore', invalid='ignore')

    activities = ACT(emg)
    mobilities = MOB(emg)
    complexities = COMPLX(emg)
    outHjorth = [activities, mobilities, complexities]
    outHjorth = np.concatenate(outHjorth, axis=0)
    return outHjorth


class FunctionsProperties:
    def __init__(self):
        self.num_feature_mav = 8
        self.num_feature_wl = 8
        self.num_feature_ssc = 8
        self.num_feature_rms = 8
        self.num_feature_hjorth = 8 * 3
        self.funcBags = [feature_mav, feature_wl, feature_ssc, feature_rms, feature_hjorth]
        self.numFeatures = [self.num_feature_mav, self.num_feature_wl, self.num_feature_ssc,
                            self.num_feature_rms, self.num_feature_hjorth]
