import numpy
import timeit
from array import array
import os
from collections import ChainMap
from types import MappingProxyType


def binary_search(target, data_structure, min_idx, max_idx):
    iteration = 0
    while min_idx <= max_idx:
        iteration += 1
        mid_idx = (min_idx + max_idx) // 2
        if data_structure[mid_idx] == target:
            return mid_idx, iteration
        elif data_structure[mid_idx] < target:
            min_idx = mid_idx+1
        else:
            max_idx = mid_idx-1
    return -1, iteration


if __name__ == '__main__':
    elements_amount = 100000000
    min_idx = 0
    max_idx = elements_amount-1
    target = 88000
    repetitions = 1000
    string = ""
    string += "iterative binary search algorithm\n"
    string += "elements amount,min index,max index,target number,repetitions\n"
    string += str(elements_amount) + "," + str(min_idx) + "," + str(max_idx) + \
              "," + str(target) + "," + str(repetitions) +"\n"
    string += "algorithm result\n"
    string += "result,iteration\n"


    ls = list(range(elements_amount))

    data_structure_list = [ls, tuple(ls), numpy.array(ls), dict(zip(ls, ls)), array('l', ls),
                           ChainMap(dict(zip(ls, ls))), MappingProxyType(dict(zip(ls, ls)))]
    data_structures_types = [type(data_structure) for data_structure in data_structure_list]
    data_structure_dict = dict(zip(data_structures_types, data_structure_list))
    time_dict = dict(zip(data_structures_types, [0 for i in data_structure_list]))

    for rep in range(repetitions):
        for data_structure_type in data_structures_types:
            data_structure = data_structure_dict[data_structure_type]
            start = timeit.default_timer()
            result, iteration = binary_search(target, data_structure, min_idx, max_idx)
            end = timeit.default_timer()
            diff = end - start
            time_dict[data_structure_type] += diff
    string += str(result) + "," + str(iteration) + "\n"
    string += "performance table:\n"
    string += "data structure type,average elapsed time (seconds)\n"
    for data_structure_type in time_dict.keys():
        time_dict[data_structure_type] /= repetitions
        string += str(data_structure_type) + "," + str(time_dict[data_structure_type]) + "\n"
    print(string)
    file = open(os.getcwd() + os.sep + "Data Structures Performance Test.csv", "w")
    file.write(string)
    file.close()
