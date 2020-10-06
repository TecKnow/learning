"""
Problem  :  Dictionaries
URL      :  http://rosalind.info/problems/ini6/
Author   :  David Perkins
"""

import sys

def wc(inString):
    words = inString.strip().split()
    return {curWord : words.count(curWord) for curWord in words}
def wcPrint(wordCount):
    ret = str()
    for word, count in sorted(wordCount.items()) :
        ret += "{0} {1}\n".format(word, count)
    return ret

if __name__ == "__main__":
    print(wcPrint(wc(sys.stdin.readline())).strip())

    

