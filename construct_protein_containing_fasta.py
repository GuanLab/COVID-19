import numpy as np
import sys
import os

os.system('rm -rf random_5000_protein_selectregion')
os.system('mkdir random_5000_protein_selectregion')

i=0
while (i<5000):
    try:
        FILE=open(('/local/disk2/gyuanfan/COVID/code/random_5000_split_result/'+str(i)),'r')
        protein_loc=np.zeros(10000000)
        for line in FILE:
            line=line.strip()
            if ('Sbjct' in line):
                line=' '.join(line.split())
                table=line.split(' ')
                protein_loc[int(table[1]):(int(table[3])+1)]=1
        FILE.close()

        FILE=open(('/local/disk2/gyuanfan/COVID/code/random_5000_split/'+str(i)),'r')
        NEW=open(('random_5000_protein_selectregion/'+str(i)),'w')
        line=FILE.readline()
        NEW.write(line)
        line=FILE.readline()
        line=line.strip()
        iii=0
        newline=''
        for a in line:
            if (protein_loc[iii]==1):
                newline=newline+a
            iii=iii+1
        NEW.write(newline)
        NEW.write('\n')
        NEW.close()
        FILE.close()
    except:
        pass
    i=i+1
