import numpy as np
import sys
import re
start=int(sys.argv[1])
end=int(sys.argv[2])

total={}
match={}
while (start<end):
    protein_loc=np.zeros(35000)
    FILE=open('../whole_genome_split_result/'+str(start),'r')
## record all positions that are protines
    for line in FILE:
        if ('Sbjct' in line):

            line=line.strip()
            line=' '.join(line.split())
            table=line.split(' ')
#            print(table[1],table[3])
#            try:
            protein_loc[int(table[1]):(int(table[3])+1)]=1
#            print(table[1],table[3])
#            except:
#                pass
    FILE.close()

    # Sbjct  18002  AENVTGLFKDCSKVITGLHPTQAPTHLSVDTKFKTEGLCVDIPGIPKDMTYRRLISMMGF  18181
    FILE=open('../epitope_split_result/'+str(start),'r')
    for line in FILE:
        line=line.strip()
        if 'Query= Epitope ' in line:
            t=line.split('Query= Epitope ')
            epitope_name=t[1]
            if (epitope_name in total):
                total[epitope_name]=total[epitope_name]+1
            else:
                total[epitope_name]=1
            
        if '>' in line:
            t=line.split('>')
            protein_name=t[1]
            FILE.readline()
            FILE.readline()
            FILE.readline()
            FILE.readline()
            FILE.readline()
            FILE.readline()
            line=FILE.readline()
            line=line.strip()
            line=' '.join(line.split())
            t=line.split(' ')
            string1=t[2]
            FILE.readline()
            line=FILE.readline()
            line=line.strip()
            line=' '.join(line.split())
            t=line.split(' ')
            string2=t[2]
            print(string1,string2)
            pos=int(t[1])

            if ((string1==string2) and (protein_loc[pos]==1)):
                if (epitope_name in match):
                    match[epitope_name]=match[epitope_name]+1
                else:
                    match[epitope_name]=1
    FILE.close()
                

    start=start+1

SUM=open('summary.txt','w')
all_epitope=total.keys()
for epitope in all_epitope:
    SUM.write(epitope)
    SUM.write('\t')

    try:
        ratio=match[epitope]/total[epitope]
    except:
        ratio=0
    SUM.write('%.4f\n' % ratio)
SUM.close()


