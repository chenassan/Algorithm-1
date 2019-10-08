#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 1:31
# @Author  : CHENJIE
# @File    : 选择排序_二分查找.py
# import random

###################################快速排序###############################################
def find_min(arg):
    min_arg = arg[0]
    min_index= 0
    for _ in range(1,len(arg)):
        if min_arg > arg[_]:
            min_arg = arg[_]
            min_index = _
    return min_index
def sort_min(arg):
    new_agr = []
    for _ in range(len(arg)):
        index=find_min(arg)
        new_agr.append(arg.pop(index))
    return  new_agr

###################################二分查询################################################
def binary_search_(arg,lis):
    star_index=0
    end_index = len(lis)
    for _ in range(end_index):
        midl_index = ((end_index- star_index) // 2) +star_index
        if arg > lis[midl_index]:
            star_index = midl_index
        elif arg < lis[midl_index]:
            end_index = midl_index
        else : return midl_index
    return None


if __name__ == '__main__':
    l = []
    for _ in range(1000):
        l.append(random.randint(1, 1000))
    # print(l)
    sort_l =sort_min(l)
    a = random.choice(sort_l)
    print('a',a)
    # print(sort_l)
    index_id =binary_search_(a,sort_l)
    if index_id:
        print('id:{} ,值{}'.format(index_id,sort_l[index_id]) )
    else:print('None')
