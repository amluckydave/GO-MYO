import os
import h5py
import numpy as np
import pandas as pd
from typing import List, Tuple, NoReturn, Mapping, Dict, Sequence, Optional


class DatasetGenerator(object):
    """
    加载文件夹下的所有子文件夹下的txt数据，生成一个h5数据集集合。
    该数据集集合包含所有受试者的数据集。
    """

    def __init__(self, data_path: str, h5save_path: str):
        """
        :param data_path:文件夹
        """
        self.X_shape = (210, 400, 8)
        self.Y_shape = (210, 400, 6)

        self.X_train_shape = (30, 400, 8)
        self.Y_train_shape = (30, 400, 6)
        self.X_test_shape = (180, 400, 8)
        self.Y_test_shape = (180, 400, 6)

        self.H5SavePath = h5save_path
        self.subj_names: List[str] = os.listdir(data_path)
        self.subj_path_list: List[str] = [data_path + '\\' + subj_name + '\\ClassifiedTxt'
                                          for subj_name in self.subj_names]
        self.ClassesList: List[str] = os.listdir(self.subj_path_list[0])
        self.ClassesList.sort()  # 将类别列表进行排序，以确保顺序正确
        print("类别列表为：", self.ClassesList)

        np.random.seed(0)
        sampleIndices = np.random.permutation(35)
        self.trainIndices = sampleIndices[0:5]
        self.testIndices = sampleIndices[5:35]

        f = h5py.File(h5save_path, mode='w', )
        for subj_name, subj_path in zip(self.subj_names, self.subj_path_list):
            print("开始读取{:s}的数据".format(subj_name))
            X_train, Y_train, X_test, Y_test = self.load_single_subj_txt(subj_path=subj_path)
            f.create_dataset(name=f'/{subj_name:s}/X_train', data=X_train)
            f.create_dataset(name=f'/{subj_name:s}/Y_train', data=Y_train)
            f.create_dataset(name=f'/{subj_name:s}/X_test', data=X_test)
            f.create_dataset(name=f'/{subj_name:s}/Y_test', data=Y_test)
        f.close()
        print(f"h5文件已保存！保存路径为:{h5save_path:s}")

    def load_single_subj_txt(self, subj_path: str) -> (np.ndarray, np.ndarray):
        """
        加载单个人的txt文本为numpy数组
        :param subj_path:
        :return: X,Y
        """
        X_data: np.ndarray = np.zeros(shape=self.X_shape, dtype=int)
        Y_data: np.ndarray = np.zeros(shape=self.Y_shape, dtype=int)

        X_train_data: np.ndarray = np.zeros(shape=self.X_train_shape, dtype=int)
        Y_train_data: np.ndarray = np.zeros(shape=self.Y_train_shape, dtype=int)
        X_test_data: np.ndarray = np.zeros(shape=self.X_test_shape, dtype=int)
        Y_test_data: np.ndarray = np.zeros(shape=self.Y_test_shape, dtype=int)

        row_index = -1
        for action_index, action in enumerate(self.ClassesList):
            for repeat_index, repeat_file in enumerate(os.listdir(os.path.join(subj_path, action))):
                repeat_txt_path = os.path.join(subj_path, action, repeat_file)  # 单个txt文件的路径
                DF = pd.read_csv(repeat_txt_path, header=None, sep='\t', )
                DF = DF.dropna(axis=1)
                row_index += 1
                X_data[row_index, :, :] = DF.values
                Y_data[row_index, :, action_index] = 1

            temp_row_index = row_index+1
            tagRowI = int(temp_row_index/35)-1
            tagRowJ = temp_row_index-35
            for i, j in enumerate(self.trainIndices):
                X_train_data[i+tagRowI*5, :, :] = X_data[j+tagRowJ, :, :]
                Y_train_data[i+tagRowI*5, :, :] = Y_data[j+tagRowJ, :, :]

            for i, j in enumerate(self.testIndices):
                X_test_data[i+tagRowI*30, :, :] = X_data[j+tagRowJ, :, :]
                Y_test_data[i+tagRowI*30, :, :] = Y_data[j+tagRowJ, :, :]

        return X_train_data, Y_train_data, X_test_data, Y_test_data
