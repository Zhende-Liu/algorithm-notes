#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-25 21:19
# @Author  : ZD Liu

def insertion_sort(obj_list):
    for i in range(len(obj_list)-1):
        p = i + 1
        while obj_list[p] < obj_list[i] and i >= 0:
            obj_list[p],obj_list[i] = obj_list[i], obj_list[p]
            p -= 1
            i -= 1
    return obj_list



if __name__ == '__main__':
    test_list = [2, 4, 1, 3, 0.9, 45, 5, 3, 3, 54, 5, 3, 345, 566, 5, 4, 2, 3, 4, 8, 9, 7, 6]
    res = insertion_sort(test_list)
    print(res)
