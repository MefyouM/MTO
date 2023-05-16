#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    sign = ""
    morf = ""
    final = ""
    add = ""
    indeks = 0
    dif = 0
    c = 0
    for i in range(len(param)):
        sign = param[i]
        if sign == "0":
            sign = "o"
        elif sign == "A":
            sign = "G"
        elif sign == "B":
            sign = "H"
        elif sign == "C":
            sign = "I"
        elif sign == "D":
            sign = "J"
        elif sign == "E":
            sign = "K"
        elif sign == "F":
            sign = "L"
        elif sign == "a":
            sign = "g"
        elif sign == "b":
            sign = "h"
        elif sign == "c":
            sign = "i"
        elif sign == "d":
            sign = "j"
        elif sign == "e":
            sign = "k"
        elif sign == "f":
            sign = "l"
        morf += sign
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.':
                indeks = format_string[idx:].index("j")
                final = format_string[idx+2:idx+indeks]
                morf = morf[:int(final)]
                dif = int(final) - len(param)
                if dif > 0:
                    for i in range(dif):
                        add = add + "o"
                    morf = add + morf
                print(morf[:int(final)],end="")
                shouldDo=False
                c = len(final)+1
            else:
                print(format_string[idx],end="")
        else:
            if c == 0:
                shouldDo=True
            else:
                c = c-1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
