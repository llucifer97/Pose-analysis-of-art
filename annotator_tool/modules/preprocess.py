import json
import os
from typing import List, Any, Union, Iterator, Tuple

from natsort import natsorted
# noinspection PyTypeChecker
from pandas import DataFrame, Index, Series
from pandas.core.arrays import ExtensionArray
from pandas.core.generic import NDFrame
from pandas.io.json import json_normalize
import statistics


# noinspection PyTypeChecker
def load_json_file(num_file: object, folder_path):
    """

    :type folder_path: object
    :param folder_path:
    :type num_file: object
    """
    print('Loading the json file......please wait it may take some time depending on size of file')
    json_arr = []  # type: List[Any]
    for i in range(num_file):
        try:
            with open(folder_path + str(i) + '.json') as f:
                d = json.load(f)
                json_arr.append(d)

        except IOError:
            print('file ' + '' + str(i) + '.json' + '' + ' not' + '' + ' found')
    print('LOaded')
    return json_arr


def sort_json_file(json_path):
    print('sorting the json files in natural way!')
    # This is the path where all the files are stored.
    # Open one of the files,
    lst = []  # type: List[Union[bytes, str]]
    for data_file in os.listdir(json_path):  # type: Union[bytes, str]
        lst.append(data_file)
    json_file = natsorted(lst)  # type: list
    return [json_file, lst]


# noinspection PyTypeChecker
def map_json_to_pose(json_file: object, peeps: object) -> object:
    print('mapping the json file and no of pose!')
    #  lets connect the number of peeps,json file name and arr[] i.e keypoints
    mapped = zip(json_file, peeps)  # type: Iterator[Tuple[Any, Any]]  
    # converting values to print as set
    mapped = set(mapped)
    json_to_peeps = list(mapped)
    json_to_peeps = natsorted(json_to_peeps)  # type: list
    return json_to_peeps


# noinspection PyTypeChecker
def get_pose_list(json_arr2: object) -> object:
    """

    :type json_arr2: object
    """
    arr = []  # type: List[Union[Union[Series, ExtensionArray, None, Index, NDFrame, DataFrame], Any]]
    for j in range(0, len(json_arr2)):  # type: int
        try:
            keypt = json_normalize(json_arr2[j]['people'])  # type: DataFrame
            for i in range(len(keypt['pose_keypoints_2d'])):
                arr.append(keypt['pose_keypoints_2d'][i])
            print(j)
            print(keypt['pose_keypoints_2d'])
        except KeyError as e:
            print('I got a KeyError - reason "%s"' % str(e))
    return arr


# noinspection PyTypeChecker
def remove_confidence_map(arr: object):
    """

    :type arr: object
    """
    point = []  # type: List[Any]
    for j in range(len(arr)):
        for i in range(0, 53):
            if i == 0 or i == 1 or i == 3 or i == 4 or i == 6 or i == 7 or i == 9 or i == 10 or i == 12 or i == 13 or \
                    i == 15 or i == 16 or i == 18 or i == 19 or i == 21 or i == 22 or i == 24 or i == 25 or i == 27 \
                    or i == 28 or i == 30 or i == 31 or i == 33 or i == 34 or i == 36 or i == 37 or i == 39 or i == \
                    40 or i == 42 or i == 43 or i == 45 or i == 46 or i == 48 or i == 49 or i == 51 or i == 52:
                point.append(arr[j][i])
    return point


# noinspection PyTypeChecker
def convert(lst: object, var_lst: object) -> object:
    """

    :type lst: object
    :type var_lst: object
    """
    idx = 0  # type: int
    for var_len in var_lst:
        yield lst[idx: idx + var_len]
        idx += var_len


# noinspection PyTypeChecker
def divide_chunks(l, n: object):
    """

    :type n: object
    :param l:
    :param n:
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]


def remove_zero(n, boolean):
    """

    :param n: 
    """
    if boolean == True:
        for j in range(n):
            for i in range(36):
                if points36[j][i] == 0:
                    points36[j][i] = statistics.stdev(points36[j])


def file_number(fn):
    num = fn.split('.')[0]
    min_val = sum(ppl[:int(num)])
    max_value = sum(ppl[int(num) + 1:int(num) + 2]) + sum(ppl[:int(num)])  # type: Union[int, Any]
    return min_val, max_value


def makefolder(jsonfile):
    try:

        assert isinstance(jsonfile, object)
        os.makedirs(jsonfile)
    except OSError:
        pass


def select_json(j, points36):
    """

    :param j: 
    :return: 
    :type points36: object
    """
    global x_data
    x_data = []
    y_data = []
    for i in range(36):
        if i % 2 == 0:
            x_data.append(points36[j][i])
        else:
            y_data.append(points36[j][i])
    X = x_data
    Y = y_data  # type: List[Any]

    return X, Y
