#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-25 21:19
# @Author  : ZD Liu


def selection_sort(obj_list):

    for i in range(len(obj_list)):
        min_ord = i
        for v in range(len(obj_list[i:])):
            if obj_list[min_ord] > obj_list[v]:
                min_ord = v + i
                print(min_ord)
        obj_list[i],obj_list[min_ord] = obj_list[min_ord],obj_list[i]


    return obj_list


if __name__ == "__main__":
    test_list = [2,5,4,2,3,4,8,9,7,6]
    res = selection_sort(test_list)
    print(res)