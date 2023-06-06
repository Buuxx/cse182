import matplotlib.pyplot as plt

class sliverhisto:
    lenlist = []
    weightlist = []

def getseq(filename):
    ecdnafile = open("ecDNA/Original/" + filename, "r")
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
            
            # check if cycle is cyclic
            iscyclicpath = list[3].split("=")
            if iscyclicpath[1] == "True":

                # get weight (number of copy)
                copy_count = float(list[1].split("=")[1])

                segments = list[5].split("=")
                segments = segments[1].split(",")
                print(list)
                for segment in segments:
                    num = segment[0:len(segment)-1]
                    seginfo = segdict["Segment " + num]
                    length = int(seginfo[4]) - int(seginfo[3])
                    sliverhisto.lenlist.append(length)
                    sliverhisto.weightlist.append(copy_count)
                    print(seginfo)
                
        line = ecdnafile.readline()

getseq("ESO51_amplicon4_annotated_cycles.txt")
getseq("FLO-1_amplicon3_annotated_cycles.txt")
getseq("JH-EsoAd1_amplicon3_annotated_cycles.txt")
getseq("JH-EsoAd1_amplicon4_annotated_cycles.txt")
getseq("JH-EsoAd1_amplicon5_annotated_cycles.txt")
getseq("OACM5.1_amplicon1_annotated_cycles.txt")
getseq("OACP4-C_amplicon1_annotated_cycles.txt")
getseq("OACP4-C_amplicon2_annotated_cycles.txt")
getseq("OACP4-C_amplicon3_annotated_cycles.txt")
getseq("OACP4-C_amplicon4_annotated_cycles.txt")
getseq("OACP4-C_amplicon5_annotated_cycles.txt")
getseq("OACP4-C_amplicon7_annotated_cycles.txt")
getseq("OACP4-C_amplicon8_annotated_cycles.txt")
getseq("OACP4-C_amplicon9_annotated_cycles.txt")
getseq("OACP4-C_amplicon11_annotated_cycles.txt")
getseq("OACP4-C_amplicon13_annotated_cycles.txt")
getseq("OACP4-C_amplicon14_annotated_cycles.txt")
getseq("OACP4-C_amplicon17_annotated_cycles.txt")
getseq("OACP4-C_amplicon18_annotated_cycles.txt")
getseq("OACP4-C_amplicon20_annotated_cycles.txt")
getseq("OACP4-C_amplicon23_annotated_cycles.txt")
getseq("OACP4-C_amplicon24_annotated_cycles.txt")
getseq("OACP4-C_amplicon26_annotated_cycles.txt")
getseq("OACP4-C_amplicon27_annotated_cycles.txt")
getseq("OE33_amplicon1_annotated_cycles.txt")
getseq("OE33_amplicon3_annotated_cycles.txt")


fig, ax = plt.subplots()
ax.hist(sliverhisto.lenlist, 50, range=[0,100000], weights=sliverhisto.weightlist, color="palevioletred")
plt.xlabel("Segment Length")
plt.ylabel("Number of Copies")
plt.show()