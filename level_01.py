"""Python challenge level 1: What about making trans

Solution: ocr

General tips:
*  Use the hints.  They are helpful, most of the times.
*  Investigate the data given to you.
*  Avoid looking for spoilers.

Forums: http://www.pythonchallenge.com/forums

Body text translated:

i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is
inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply
on the url.
"""
from string import ascii_lowercase

URL = "http://www.pythonchallenge.com/pc/def/map.html"

BODY_TEXT = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq
glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw
ml rfc spj.
"""


ROT_3 = ascii_lowercase[2:] + ascii_lowercase[:2]
trans_table = str.maketrans(ascii_lowercase, ROT_3)

if __name__ == "__main__":
    print(BODY_TEXT.translate(trans_table))
