#!/bin/python3

import math
import os
import random
import re
import sys


def median(arr):
    arr.sort()
    if len(arr) == 1:
        return arr[0]
    elif len(arr) % 2 == 0:
        m = len(arr)//2
        return (arr[m-1]+arr[m])//2
    else:
        return arr[(len(arr)//2)]


def activityNotifications(expenditure, d):
    count = 0
    toLook = expenditure[d:]
    for i in toLook:
        if i >= 2*median(expenditure[:d]):
            count += 1
        d += 1

    return count


if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50]
    print(activityNotifications(arr, 3))
