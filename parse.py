import pandas as pd

def parse():
    filename = open("filelist.txt", "r")
    filelist = filename.readlines()

    output = open("ecDNAinfo.txt", "w")
    for i in filelist:
        output.write(i)
        ampliconfile = open("../resultsl/other_files/ccle_hg38_ac/"
                         + "ccle_hg38_annotated_cycles_files/" 
                         + i.strip(), "r")
        segments = {}
        ampliconlist = ampliconfile.readlines()
        for i in ampliconlist:
            # create segments dict by segments number
            # [chr#, start_loc, end_loc]
            if i[0:7]=="Segment":
                segment = i.split("\t")
                segments[segment[1]] = [segment[2][3:], int(segment[3]), int(segment[4].strip())]
        for i in ampliconlist:
            if "IsCyclicPath=True" in i:
                output.write(i)
                cyclelist = i.split(";")
                segmentlist = cyclelist[5].strip().split("=")[1].split(",")
                for j in segmentlist:
                    seg = j[0:len(j)-1]
                    strand = j[-1]
                    if segments[seg][2] - segments[seg][1] <= 1000:
                        output.write("Segment" + seg + "," + str(segments[seg][0]) 
                                     + "," + str(segments[seg][1]) + "," 
                                     + str(segments[seg][2]) + "," + strand + "\n")

def cleanseg1():
    infile = open("ecDNAinfo.txt", "r")
    outfile = open("segfile0.txt", "w")
    for line in infile:
        if line[-5:-1] == ".txt":
            outfile.write(line)
        if line[0:7] == "Segment":
            outfile.write(line)

def cleanseg2():
    infile = open("segfile0.txt", "r")
    outfile = open("segfile.txt", "w")
    linelist = infile.readlines()
    for i in range(len(linelist)):
        if linelist[i][-5:-1] == ".txt" and linelist[i+1][-5:-1] == ".txt":
            continue
        outfile.write(linelist[i])

def GetRegion(chromosome, start, end, strand):
    RGFile = open("../ReferenceGenome/chromosome" + str(chromosome) + ".fna")
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

def sequencing():
    input = open("segfile.txt", "r")
    sliverinfo = open("sliverinfo.txt", "w")
    sliverseqs = open("sliverseqs.txt", "w")

    i = 1
    for line in input:
        if line[0:7] == "Segment":
            segi = line.split(",")
            seq = GetRegion(segi[1], int(segi[2]), int(segi[3]), segi[4].strip())
            sliverinfo.write(line)
            sliverinfo.write(seq + "\n")
            sliverseqs.write(seq + "\n")
            print("finished " + str(i))
            i += 1
        else:
            sliverinfo.write(line)

def table():
    # headers: [filename,segment#,chr#,startloc,endloc,strand,length,#GC,%GC,seq]
    sliverinfo = open("sliverinfo.txt", "r").readlines()
    filename = ""
    sliverdat = []
    for lnum in range(len(sliverinfo)):
        line = sliverinfo[lnum].strip()
        if line[-4:] == ".txt":
            filename = line
        elif line[0:7] == "Segment":
            seq = sliverinfo[lnum+1].strip()
            # list: [seg#,chr#,startloc,endloc,strand]
            list = line.split(",")
            segnum = list[0]
            chrnum = list[1]
            startloc = int(list[2])
            endloc = int(list[3])
            strand = list[4]
            length = endloc - startloc
            print(length)
            gc_c = 0
            gc = ["G", "g", "C", "c"]
            if length == 0:
                break
            for char in seq:
                if char in gc:
                    gc_c += 1
            gc_p = (gc_c/length)*100
            
            sliverlist = [filename,segnum,chrnum,startloc,endloc,strand,length,gc_c,gc_p,seq]
            sliverdat.append(sliverlist)
    df = pd.DataFrame(sliverdat, columns=["filename","segment#","chr#","startloc","endloc","strand","length","#GC","%GC","seq"])
    df.to_csv('sliverdat.csv', index=False)

# parse()
# cleanseg1()
# cleanseg2()
# sequencing()
# table()