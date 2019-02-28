#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-25 21:19
# @Author  : ZD Liu


def selection_sort(obj_list):
    opt_list = obj_list
    for n in range(len(opt_list)):
        q = n
        i = n
        while q <= len(opt_list)-1:
            if obj_list[q] < obj_list[i]:
                i = q
            q += 1
        obj_list[i], obj_list[n] = obj_list[n], obj_list[i]
    return  obj_list

if __name__ == "__main__":
    test_list = [2,1,3,0.9,45,5,3,3,54,5,3,345,566,5,4,2,3,4,8,9,7,6]
    res = selection_sort(test_list)
    print(res)