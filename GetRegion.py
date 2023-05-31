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

print(GetRegion(11,93278730,93279265, "+"))