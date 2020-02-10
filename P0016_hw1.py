#!/usr/bin/env python3

def topAndBottomLine(width, edges, middle):
    print(edges, end='')
    for _ in range(width-2):
        print(middle, sep = '', end = '')
    print(edges)

hight = 20
width = 15

topAndBottomLine(width, '+', '-')
for _ in range(hight-2):
    topAndBottomLine(width, '|', ':')
topAndBottomLine(width, '+', '-')

    
    
