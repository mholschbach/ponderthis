#!/usr/bin/python
# Michael Holschbach http://mh-area.de
#
# http://domino.research.ibm.com/Comm/wwwr_ponder.nsf/Challenges/February2013.html

import sys
from math import sqrt

n=9999 # start with first occurence of 9999 in n
max=sqrt(sys.maxint) # end before overflow

def is_square(square):
    if square == 0:
        return False
    if square == 1:
        return True
    x = square // 2
    seen = {x}
    while x * x != square:
        x = (x + (square // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


while (n<max):
    if "9999" in str(n):
        square = str(n*n)
        for p in range(1,len(square)):
            if square[p] != '0':
                if is_square(int(square[0:p])):
                    if is_square(int(square[p:len(square)])):
                        print "z:", n, "split in", square[0:p], square[p:len(square)], "x:", int(sqrt(int(square[0:p]))), "y:", int(sqrt(int(square[p:len(square)])))

    #if n%1000000 == 0:
        #print n
    n=n+1
