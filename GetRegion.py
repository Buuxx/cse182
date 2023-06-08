def GetRegion(chromosome, start, end, strand):
    RGFile = open("ReferenceGenome/chromosome" + str(chromosome) + ".fna")
    RGLines = RGFile.readlines()
    RefGen = ""
    for i in range(1, len(RGLines)):
        RefGen = RefGen + RGLines[i].strip()
    seq = RefGen[int(start) - 1 : int(end)]
    seq_reverse = ""
    if strand == "-":
        for i in range(len(seq)):
            seq_reverse = seq[i] + seq_reverse
        seq = seq_reverse
    return seq

# change this to specific chromosome, start point, end
# point, and strand you are looking at, and it will print
# out the exact sequence

print(GetRegion(5,846641,847074,"+"))