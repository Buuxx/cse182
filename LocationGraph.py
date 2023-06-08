import matplotlib.pyplot as plt 

dict = {}
for i in range (1, 23):
    dict[str(i)] = 0
dict["X"] = 0
dict["Y"] = 0

def ChromCount(filename):
    file = open(filename)
    lines = file.readlines()
    total = 0
    for row in lines:
        if row[:7] == 'Segment':
            cols = row.split(',')
            dict[cols[1]] += 1
            total += 1
    # print(total)

    # # assuming the same header as right now, will adjust accordingly 
    # chromosome_num = lines[1].split(',')[1][4:]
    # dict[chromosome_num] += 1

# ChromCount("ESO51_amplicon4_annotated_cycles.txt")
# ChromCount("FLO-1_amplicon3_annotated_cycles.txt")
# ChromCount("JH-EsoAd1_amplicon3_annotated_cycles.txt")
# ChromCount("JH-EsoAd1_amplicon4_annotated_cycles.txt")
# ChromCount("JH-EsoAd1_amplicon5_annotated_cycles.txt")
# ChromCount("OACM5.1_amplicon1_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon1_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon2_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon3_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon4_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon5_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon7_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon8_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon9_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon11_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon13_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon14_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon17_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon18_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon20_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon23_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon24_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon26_annotated_cycles.txt")
# ChromCount("OACP4-C_amplicon27_annotated_cycles.txt")
# ChromCount("OE33_amplicon1_annotated_cycles.txt")
# ChromCount("OE33_amplicon3_annotated_cycles.txt")
# # print(dict)

ChromCount('segfile.txt')

# plot the results
chromosome = list(dict.keys())
count = list(dict.values())

plt.bar(range(len(dict)), count, tick_label=chromosome, color="green")
plt.ylabel("Segment Length")
plt.xlabel("Chromosome")
plt.show()
plt.savefig("ChromosomeDistribution.png")