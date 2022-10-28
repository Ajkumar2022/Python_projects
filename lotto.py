# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:24:30 2022

@author: aksaa
"""

import random

lotto=[]
while True:
    value1=random.randint(0,50)
    if value1 not in lotto:
        lotto.append(value1)
    if len(lotto)==6:
        break
    
print(lotto)