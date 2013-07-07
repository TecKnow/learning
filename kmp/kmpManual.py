#   CAGTAAGCAGGGACTG
#   0000000123000100

##algorithm kmp_table:
def KMP_Table(searchString):
    T = list()

    pos = 1
    cnd = 0
    T.append(0)

    while pos < len(searchString):
        if searchString[pos] == searchString[cnd]:
           cnd += 1
           T.append(cnd)
           pos += 1
        elif cnd > 0:
           cnd = T[cnd-1]
        else:
           T.append(0)
           pos += 1
    return T
if __name__ == "__main__":
    with open("RosKMPin.txt") as ifile, open("RosKMPout.txt", mode="w") as ofile:
        ins = ifile.read()
        #print(*ins)
        print(*KMP_Table(ins), end = '', file = ofile)
        #print(*KMP_Table(ins)[1:])
