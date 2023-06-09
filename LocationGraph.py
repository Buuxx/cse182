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

ChromCount('sliverinfo.txt')

# plot the results
chromosome = list(dict.keys())
count = list(dict.values())

plt.bar(range(len(dict)), count, tick_label=chromosome, color="green")
plt.ylabel("Segment Length")
plt.xlabel("Chromosome")
plt.show()
plt.savefig("ChromosomeDistribution.png")