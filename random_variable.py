#!/usr/local/bin/python3

'''
this script should generate random number
just thought that hash should give unique output for unique number
use timestamp as unique unput and xor + ord to get number from hash output
devide to 255 as encoding is utf-8 to get number in (0,1)
'''

import hashlib
import time

if __name__ == "__main__":

    rndm = 0
    tme = str(time.time()).encode('utf-8')
    for char in hashlib.md5(tme).hexdigest():
        rndm = rndm ^ ord(char)
    print(rndm/255)
