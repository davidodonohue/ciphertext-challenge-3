import pandas as pd

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

topCapital = ord('A')
bottomCapital = ord('Z')
topLower = ord('a')
bottomLower = ord('z')
space = ord(' ')

def get_range():
    ascii_range = []
    for line in train["text"]:
        for char in line:
            asc = ord(char)
            if asc not in ascii_range:
                ascii_range.append(asc)

def strip_punctuation(st):
    rtn = ""
    for char in st:
        o = ord(char)
        if (o >= topCapital and o <= bottomCapital) or (o >= topLower and o <= bottomLower) or o == space:
            rtn+=char
    return rtn

def shift_line(st,n):
    rtn = ""
    for char in st:
        if char != ' ':
            o = ord(char)
            s = (((o-topCapital) + n) % 26) + topCapital
            rtn += chr(s)
        else:
            rtn += char
    return rtn



def check_caesar(base):
    for shift in range(26):
        testline = shift_line(base, shift)
        print(testline)
check_caesar(test['ciphertext'][0])
