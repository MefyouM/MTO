#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    morf = ""
    sign = ""
    final = ""
    indeks = 0
    c = 0
    d = 0
    dotDetected = False
    for i in range(len(param)):
        sign = param[i]
        if sign == "0":
            sign = "a"
        elif sign == "1":
            sign = "b"
        elif sign == "2":
            sign = "c"
        elif sign == "3":
            sign = "d"
        elif sign == "4":
            sign = "e"
        elif sign == "5":
            sign = "f"
        elif sign == "6":
            sign = "g"
        elif sign == "7":
            sign = "h"
        elif sign == "8":
            sign = "i"
        elif sign == "9":
            sign = "j"
        elif sign ==".":
            dotDetected = True
            break;
        d += 1
        morf += sign
    if dotDetected:
        for j in range(d+1,len(param)):
            sign = (int(param[j])+5)%10
            morf += str(sign)
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.':
                indeks = format_string[idx:].find("h")
                final = format_string[idx+2:idx+indeks]
                if indeks == -1 or final.isdigit() == False:
                    print(format_string[idx],end="")
                else:
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
