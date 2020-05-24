from os import path, makedirs


def myoPath():
    rootPath = path.expanduser('~')
    try:
        makedirs(rootPath + r'\linkMYO')
        addrSHU = rootPath + r'\linkMYO'
    except:
        addrSHU = rootPath + r'\linkMYO'

    return addrSHU


def myoRawPath():
    rootPath = path.expanduser('~')
    try:
        makedirs(rootPath + r'\linkMYO\trainFile')
        addrSHU = rootPath + r'\linkMYO\trainFile'
    except:
        addrSHU = rootPath + r'\linkMYO\trainFile'

    return addrSHU


def myoTrainedPath():
    rootPath = path.expanduser('~')
    try:
        makedirs(rootPath + r'\linkMYO\CLFile')
        addrSHU = rootPath + r'\linkMYO\CLFile'
    except:
        addrSHU = rootPath + r'\linkMYO\CLFile'

    return addrSHU
