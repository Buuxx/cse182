sliver_info = open('sliverinfo.txt')
lines = sliver_info.readlines()
SliverFasta = open('SliverFasta_2.fa', 'w')

name = ""
for line in lines: 
    line = line.strip()
    if line[-3:] == 'txt':
        name = line 
        # print(name)
    elif line[:7] == 'Segment':
        seg = line.split(",")
        header = name + ' ' + seg[0]
        SliverFasta.write('>' + header + '\n')
    else:
        SliverFasta.write(line + '\n')
