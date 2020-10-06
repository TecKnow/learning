class FASTA:

    @staticmethod
    def fromFormatString(FASTAString):
        lines = FASTAString.splitlines()
        #print(lines)
        if not lines[0].startswith(">"):
            raise FASTAFormatError("FASTA format violated, first line doesn't begin with a '>'")
        descParts = lines[0][1:].split()
        name = None
        description = None
        if len(descParts) >= 1:
            name = descParts[0]
        if len(descParts) >= 2:
            description = descParts[1]
        if len(descParts) >= 3:
            raise FASTAFormatError("FASTA format violated, first line has too many parts")
        value = ''.join(lines[1:])
        return FASTA(value, name, description)            

    @staticmethod
    def fromList(FASTAStrings):
        FASTAs = FASTAStrings.split('>')
        FASTAs = [">" + x for x in FASTAs if len(x) > 0]
        #print("FASTAs", FASTAs)
        return list(map(FASTA.fromFormatString, FASTAs))

    def __init__ (self, value, name = None, description = None):
        self.name = name
        self.value = value
        self.description = description
    def __repr__ (self):
        return (self.name, self.description, self.value).__repr__()

class FASTAFormatError(Exception):
    pass

if __name__ == "__main__":
    import sys
    print(FASTA.fromList(sys.stdin.readline()))
