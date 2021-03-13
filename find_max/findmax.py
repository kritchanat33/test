# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 13:02:29 2021

@author: TIMER
"""

def find_max(data):
    max_idx = 0
    for idx, val in enumerate(data):
        if data[max_idx] < val:
            max_idx = idx
    return max_idx
