import sys

def minion_game(self):
    vowels = 'AEIOU'
    vow = "AEIOU"
    slen = len(string)
    print(slen)
    tsub = int(slen * (slen + 1) / 2)
    print(tsub)
    k = sum(slen - i for i in range(slen) if string[i] in vow)   
    print(k)
    s = tsub - k
    print(s)
    if s > k: print(f"Stuart {s}")
    elif s < k: print(f"Kevin {k}")
    else: print("Draw")


