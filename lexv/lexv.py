import sys
import itertools

class DNAString:
    Alphabet = tuple()

    
    def __init__(self, textString):
        self.textString = textString
    def __repr__(self):
        return self.textString
    #COMPARISON BLOCK
    def __cmp__(self, other):
        for x in range(min(len(self.textString), len(other.textString))):
            if DNAString.Alphabet.index(self.textString[x]) < DNAString.Alphabet.index(other.textString[x]):
                return -1
            elif DNAString.Alphabet.index(self.textString[x]) > DNAString.Alphabet.index(other.textString[x]):
                return 1
        else:
            if len(self.textString) < len(other.textString):
                return -1
            elif len(self.textString) > len(other.textString):
                     return 1
            else:
                return 0
    def __lt__(self,other):
        if DNAString.__cmp__(self, other) == -1:
            return True
        else:
            return False
    def __le__(self, other):
        if DNAString.__cmp__(self, other) <= 0:
            return True
        else:
            return False
    def __eq__(self, other):
        if DNAString.__cmp__(self, other) == 0:
            return True
        else:
            return False
    def __ne__(self, other):
        if DNAString.__cmp__(self, other)!= 0:
            return True
        else:
            return False
    def __gt__(self,other):
        if DNAString.__cmp__(self, other) == 1:
            return True
        else:
            return False
    def __ge__(self, other):
        if DNAString.__cmp__(self, other) >= 0:
            return True
        else:
            return False
    #END COMPARISON BLOCK
    #@classmethod
    def generateLanguage(alphabet, maxLength):
        DNAString.Alphabet = alphabet
        Language = list()
        while maxLength:
            Language.extend(itertools.product(DNAString.Alphabet, repeat=maxLength))
            maxLength -= 1
        Language = list(map(''.join, Language))
        Language = (DNAString(x) for x in Language)
        return(sorted(Language))
#END CLASS
if __name__=="__main__":
    with open('RosLEXVout.txt', mode='w') as outfile:
        print("Enter the alphabet:")
        alphabet = sys.stdin.readline().strip().split()
        print("Enter the max length of a word:")
        maxLength = int(sys.stdin.readline().strip())
        language = DNAString.generateLanguage(alphabet, maxLength)
        print(*language, sep='\n', end='', file=outfile)
