#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    paramOut = ""
    pattern = "abcdefghij"
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'b':
                paramInt = int(param)
                paramBin = bin(paramInt)[2:]
                paramRev = paramBin[::-1]
                paramStr = str(paramRev)
                for i in range(len(paramStr)):
                    if paramStr[i] == "0":
                        paramOut += "0"
                    else:
                        paramOut += pattern[i%10]
                paramFinal = paramOut[::-1]
                print(paramFinal,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
