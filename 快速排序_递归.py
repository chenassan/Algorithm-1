
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 19:16
# @Author  : CHENJIE
# @File    : 快速排序_递归.py
import sys
sys.setrecursionlimit(100000)
import random
#D&C分而治之
def quickly_sort(li):
    if len(li)<2:
        return li
    temp = li[0]
    small_l=[i for i in li[1:] if i <=temp]
    great_l=[i for i in li[1:] if i>temp]
    # for i in li[1:]:
    #     if temp <= li[i]:
    #         great_l.append(li[i])
    #     elif temp > li[_]:
    #         small_l.append(li[i])
    return quickly_sort(small_l) + [temp] + quickly_sort(great_l)


if __name__ == '__main__':
    ls = []
    for _ in range(20):
        ls.append(random.randint(1, 100))
    print(ls)
    sort_l = quickly_sort(ls)
    print（sort_l）
