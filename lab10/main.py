#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    # F=int((O*2)/N)
    shouldDo=True
    paramInt = int(param)
    N = len(str(paramInt))
    O = paramInt
    F = int((O*2)/N)
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'a':
                print(F,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")
    #print("Liczba cyfr : "+str(N))
    
data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
