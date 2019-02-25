#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-25 21:18
# @Author  : ZD Liu

def bubble_sort(obj_list):
    for i in obj_list:
        n = 0
        while n + 1 < len(obj_list):
            if obj_list[n] > obj_list[n+1]:
                obj_list[n+1],obj_list[n] = obj_list[n],obj_list[n+1]
            n += 1
    return obj_list

if __name__ == '__main__':
    test_list = [2,5,4,2,3]
    res = bubble_sort(test_list)
    print(res)