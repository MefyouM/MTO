#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    formated_string = format_string
    print(format_string)
    shouldDo=True
    for idx in range(0,len(formated_string)):
        if shouldDo:
            if formated_string[idx] == '#' and formated_string[idx+1] == 'k':
                print(param.swapcase(),end="")
                shouldDo=False
            else:
                print(formated_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
