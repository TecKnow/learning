"""
Problem  :  Complementing a Strand of DNA
URL      :  http://rosalind.info/problems/revc/
Author   :  David Perkins
"""

import sys
str = sys.stdin.readline()
str = str[::-1]
str = str.replace("A","1")
str = str.replace("T","2")
str = str.replace("C","3")
str = str.replace("G","4")
str = str.replace("1","T")
str = str.replace("2","A")
str = str.replace("3","G")
str = str.replace("4","C")
print(str)
