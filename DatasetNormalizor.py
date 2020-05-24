import numpy as np


def Normalized_Dataset(rawEMG):
    rawEMG = rawEMG.astype(np.float64)
    rawEMG = (2 * (rawEMG + 128)) / 256 - 1
    return rawEMG
