
def getseq(filename):
    ecdnafile = open("ecDNA/Original/" + filename, "r")
    outputfile = open("ecDNA/Sequence/" + filename, "w")
    line = ecdnafile.readline()

    # store segment information into seg dict
    segdict = {}
    while len(line) != 0:
        if line[0:7] == "Segment":
            list = line.strip().split("\t")
            # print(list)
            segdict[list[0]+" "+list[1]] = list
        line = ecdnafile.readline()

    ecdnafile.seek(0)
    line = ecdnafile.readline()
    while len(line) != 0:
        if line[0:5] == "Cycle":
            list = line.strip().split(";")
            iscyclicpath = list[3].split("=")
            if iscyclicpath[1] == "True":
                outputfile.write(line)
                segments = list[5].split("=")
                segments = segments[1].split(",")
                for segment in segments:
                    num = segment[0:len(segment)-1]
                    strand = segment[-1]
                    seginfo = segdict["Segment " + num]
                    # print(seginfo)
                    # print(num)
                    # print(strand)
                    # if len(segdict["Segment " + num]) !=
                    seqlist = parseloc(seginfo, num, strand)
                    # segdict["Segment " + num].append(strand).append(seqlist[0])
                    outputfile.write(">"+"Segment "+num+", "+seginfo[2]+", "+seginfo[3]+", "+seginfo[4]+"\n")
                    outputfile.write(seqlist[0] + "\n")
                    print(filename+"("+list[0]+"): "+"segment "+num+" length "+str(seqlist[1]))
                
        line = ecdnafile.readline()


def parseloc(seginfo, num, strand):
    chrnum = seginfo[2][3:]
    refgen = open("ReferenceGenome/chromosome"+chrnum+".fna", "r")
    startloc = int(seginfo[3])
    endloc = int(seginfo[4])
    line = refgen.readline()
    sequence = ""

    # calculate start position
    linestart = startloc//80
    pointstart = startloc%80

    # calculate length
    length = endloc - startloc

    for i in range(linestart):
        line = refgen.readline()
    
    sequence += line.strip()[pointstart:]
    length -= len(sequence)
    while length > 80:
        line = refgen.readline()
        sequence += line.strip()
        length -= 80
    line = refgen.readline()
    sequence += line[0:length]
    
    if strand == "-":
        negseq = ""
        for base in sequence:
            negseq = base + negseq
        sequence = negseq

    seqlist = [sequence, len(sequence)]
    return seqlist


# getseq("ESO51_amplicon4_annotated_cycles.txt")
# getseq("FLO-1_amplicon3_annotated_cycles.txt")
# getseq("JH-EsoAd1_amplicon3_annotated_cycles.txt")
# getseq("JH-EsoAd1_amplicon4_annotated_cycles.txt")
# getseq("JH-EsoAd1_amplicon5_annotated_cycles.txt")
# getseq("OACM5.1_amplicon1_annotated_cycles.txt")
# getseq("OACP4-C_amplicon1_annotated_cycles.txt")
# getseq("OACP4-C_amplicon2_annotated_cycles.txt")
# getseq("OACP4-C_amplicon3_annotated_cycles.txt")
# getseq("OACP4-C_amplicon4_annotated_cycles.txt")
# getseq("OACP4-C_amplicon5_annotated_cycles.txt")
# getseq("OACP4-C_amplicon7_annotated_cycles.txt")
# getseq("OACP4-C_amplicon8_annotated_cycles.txt")
# getseq("OACP4-C_amplicon9_annotated_cycles.txt")
# getseq("OACP4-C_amplicon11_annotated_cycles.txt")
# getseq("OACP4-C_amplicon13_annotated_cycles.txt")
# getseq("OACP4-C_amplicon14_annotated_cycles.txt")
# getseq("OACP4-C_amplicon17_annotated_cycles.txt")
# getseq("OACP4-C_amplicon18_annotated_cycles.txt")

getseq("OACP4-C_amplicon20_annotated_cycles.txt")
getseq("OACP4-C_amplicon23_annotated_cycles.txt")
getseq("OACP4-C_amplicon24_annotated_cycles.txt")
getseq("OACP4-C_amplicon26_annotated_cycles.txt")
getseq("OACP4-C_amplicon27_annotated_cycles.txt")
getseq("OE33_amplicon1_annotated_cycles.txt")
getseq("OE33_amplicon3_annotated_cycles.txt")