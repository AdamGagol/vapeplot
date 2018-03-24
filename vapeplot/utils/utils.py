#!/usr/bin/env python
import numpy as np


def hex_to_int_(col):
    color = int(col[1:],16)
    r = color%256
    g = (color%(256**2) - r)//256
    b = (color%(256**3) - 256*g - r)//256**2
    return np.array((r,g,b))

def full_hex_(col):
    hex1 = hex(col)[2:]
    if len(hex1) == 1:
        hex1 = '0' + hex1
    return hex1
    
def int_to_hex_(col):
    color = col[0] + 256*col[1] + 256**2*col[2]
#     print(hex(color), hex(col[2])[2:], hex(col[1])[2:] + hex(col[0])[2:])
    return '#' + full_hex_(col[2]) + full_hex_(col[1]) + full_hex_(col[0])

def prolong_(palette, mult = 4):
    new_palette = []
    for i in range(len(palette) - 1):
        col1, col2 = hex_to_int_(palette[i]), hex_to_int_(palette[i+1])
        for m in range(mult):
            new_palette.append(int_to_hex_(((1-m/mult)*col1 + (m/mult)*col2).astype(int) ))
    new_palette.append(palette[-1])
    return new_palette
