import numpy as np


all_epi={}
FILE=open('all_epitope','r')
for line in FILE:
    line=line.strip()
    all_epi[line]=1

the_connection={}
for epi1 in all_epi.keys():
    for epi2 in all_epi.keys():
## now we calculate the maximal similarity score:
        if (len(epi1)<len(epi2)):
            if (epi1 in epi2):
                string=epi1+'_'+epi2
                the_connection[string]=1
                string=epi2+'_'+epi1
                the_connection[string]=1
            cut=1
            while (cut<5):
                epi1_cut=epi1[cut:]
                if (len(epi1_cut)>5):
                    if (epi1_cut==epi2[0:len(epi1_cut)]):
                        string=epi1+'_'+epi2
                        the_connection[string]=1
                        string=epi2+'_'+epi1
                        the_connection[string]=1

                epi1_cut=epi1[:-cut]
                if (len(epi1_cut)>5):
                    if (epi1_cut == epi2[(len(epi2)-len(epi1_cut)):]):
                        string=epi1+'_'+epi2
                        the_connection[string]=1
                        string=epi2+'_'+epi1
                        the_connection[string]=1

                cut=cut+1

visited={}
group=1
for epi in all_epi.keys():
    if (epi in visited):
        pass
    else:
        ch=0
        for epi_ref in visited.keys():
            string=epi_ref+'_'+epi
            if (string in the_connection):
                value=visited[epi_ref]
                ch=1
        if (ch==1):
            visited[epi]=value
        if (ch==0):
            visited[epi]=group
            group=group+1


ggg=1
while (ggg<group):
    member=[]
    for epi in all_epi.keys():
        if (visited[epi]==ggg):
            member.append(epi)
    print('Group '+str(ggg),member)
    ggg=ggg+1

