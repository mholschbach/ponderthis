#!/usr/bin/python
# Michael Holschbach http://mh-area.de
#
# http://domino.research.ibm.com/Comm/wwwr_ponder.nsf/Challenges/February2013.html

import sys
from math import sqrt
from string import find, rfind

n=9999 # start with first occurence of 9999 in n
max=sqrt(sys.maxint) # end before overflow

max_in_dict = 999999999
squares = dict()
squares[0]=False
squares[1]=True

def is_square(square):
    if square in squares:
        return squares[square]
    x = square // 2
    seen = {x}
    while x * x != square:
        x = (x + (square // x)) // 2
        if x in seen:
            if square <= max_in_dict:
                squares[square] = False
            return False
        seen.add(x)
    if square <= max_in_dict:
        squares[square] = True
    return True

while (n<max):
    if "9999" in str(n): # found 9999 in integer representation
        square = str(n*n)
        for p in range(1,len(square)):
            if square[p] != '0': # so representation doesn't start with 0
                if p <= len(square)/2: # do sqrt test with shorter part
                    if is_square(int(square[0:p])):
                        if is_square(int(square[p:len(square)])):
                            print "z:", n, "split in", square[0:p], square[p:len(square)], "x:", int(sqrt(int(square[0:p]))), "y:", int(sqrt(int(square[p:len(square)])))
                else:
                    if is_square(int(square[p:len(square)])):
                        if is_square(int(square[0:p])):
                            print "z:", n, "split in", square[0:p], square[p:len(square)], "x:", int(sqrt(int(square[0:p]))), "y:", int(sqrt(int(square[p:len(square)])))
        n=n+1        
    elif find(str(n),'9') == -1: # no 9 at all, big step to ....9999
        n = n - n%10000 + 9999
    else:
        tmp = bytearray(str(n))        
        pos = rfind(tmp, '9', len(tmp)-5, len(tmp)-2)
        if pos != -1: # found 9 in ....????.
            tmp[pos+1]='9'
            n = int(tmp)
        else: # big step to ...?9999 with ? is not 9 
            n = n - n%10000 + 9999

    #if n%1000000 == 0:
        #print n
