import os
import re
import h5py
import shutil
import pandas as pd
import numpy as np
from myoLib.ges2code import ges2code
from myoLib.myoPath import myoRawPath, myoTrainedPath

rawPath = myoRawPath()
trainedPath = myoTrainedPath()


def Classify_Txt():
    filelist = os.listdir(rawPath)
    prefix = []
    for string in filelist:  # 提取待归类文件 类名
        n = re.findall(r'(.+?)-', string)
        n = ''.join(n)
        prefix.append(n)
    prefix = list(set(prefix))
    prefix.sort()  # 将类别列表进行排序，以确保顺序正确

    X_shape = (len(filelist), 400, 8)
    Y_shape = (len(filelist), 400, len(prefix))

    for i in prefix:  # 创建同名文件夹
        filePath = rawPath + '/' + i
        if not os.path.exists(filePath):
            os.makedirs(filePath)

    for file in filelist:  # 移动响应文件到同类文件夹中
        src = os.path.join(rawPath, file)

        n = ''.join(re.findall(r'(.+?)-', file))
        new_path = rawPath + '\\' + n
        dst = os.path.join(new_path, file)
        shutil.move(src, dst)

    X_data: np.ndarray = np.zeros(shape=X_shape, dtype=int)
    Y_data: np.ndarray = np.zeros(shape=Y_shape, dtype=int)
    row_index = -1
    for action_index, action in enumerate(prefix):
        for repeat_index, repeat_file in enumerate(os.listdir(os.path.join(rawPath, action))):
            repeat_txt_path = os.path.join(rawPath, action, repeat_file)  # 单个txt文件的路径
            DF = pd.read_csv(repeat_txt_path, header=None, sep='\t', )
            DF = DF.dropna(axis=1)
            row_index += 1
            X_data[row_index, :, :] = DF.values
            # Y_data[row_index, :, action_index] = 1
            Y_data[row_index, :, :] = ges2code().outer(action)

    h5Path = trainedPath + '/' + 'train.h5'
    with h5py.File(h5Path, mode='w', ) as f:
        f.create_dataset(name='/X_train', data=X_data)
        f.create_dataset(name='/Y_train', data=Y_data)
    print("读取【训练集】数据 完毕")

    shutil.rmtree(rawPath)
