# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

ftemp = [60, 70, 75, 80, 85, 90, 95, 100 , 105]

def ftoc(f):
    f -= 32
    f += (5/9)
    return f

for t in ftemp:
    print(t, "Fahrenheit equals = {0:.2f}".format(ftoc(t)), "Celsius")