# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:28:19 2022

@author: salva
"""

def is_prime(n):
    if n > 0:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

for thousand in range(1,1001):
    if (is_prime(thousand)):
        print(thousand)