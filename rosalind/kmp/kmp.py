#   CAGTAAGCAGGGACTG
#   0000000123000100

##algorithm kmp_table:
def KMP_Table(searchString):

        
    
##    input:
##        an array of characters, W (the word to be analyzed)
##        an array of integers, T (the table to be filled)
##    output:
##        nothing (but during operation, it populates the table)
##
##    define variables:
##        an integer, pos ← 2 (the current position we are computing in T)
##        an integer, cnd ← 0 (the zero-based index in W of the next 
##character of the current candidate substring)
##
##    (the first few values are fixed but different from what the algorithm 
##might suggest)
##    let T[0] ← -1, T[1] ← 0
##
    pos = 2
    cnd = 0
    ##print("Size of searchString:", len(searchString))
    res = list([0] * len(searchString))

    res[0] = -1


##    while pos is less than the length of W, do:
    while pos < len(searchString):
##        (first case: the substring continues)
##        if W[pos - 1] = W[cnd],
        if searchString[pos - 1] == searchString[cnd]:
##          let cnd ← cnd + 1, T[pos] ← cnd, pos ← pos + 1
            cnd += 1
            res[pos] = cnd
            pos += 1
##
##        (second case: it doesn't, but we can fall back)
##        otherwise, if cnd > 0, let cnd ← T[cnd]
        elif cnd > 0:
            cnd = res[cnd]
##
##        (third case: we have run out of candidates.  Note cnd = 0)
##        otherwise, let T[pos] ← 0, pos ← pos + 1
        else:
            res[pos] = 0
            pos += 1
    return(res)
if __name__ == "__main__":
    with open("RosKMPin.txt") as ifile, open("RosKMPout.txt", mode="w") as ofile:
        ins = ifile.read()
        #print(*ins)
        print(*KMP_Table(ins), file = ofile)
        #print(*KMP_Table(ins)[1:])
