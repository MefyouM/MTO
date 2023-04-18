#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    morf = ""
    for i in range(len(param)):
        liczba = int(param[i])
        liczba = liczba*9
        liczba = liczba+1
        liczba = liczba%10
        cyfra = str(liczba)
        morf += cyfra
    morf = str(morf)
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'g':
                print(morf,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
