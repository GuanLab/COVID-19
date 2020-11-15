import numpy as np


all_epi={}
FILE=open('/local/disk4/mqzhou/covid19/results/epitope/all_epitopes','r')
for line in FILE:
    line=line.strip()
    all_epi[line]=1

the_map={}
for epi1 in all_epi.keys():
    for epi2 in all_epi.keys():
## now we calculate the maximal similarity score:
        if (len(epi1)<len(epi2)):
            if (epi1 in epi2):
                print (epi1,' is a subsequence' ,epi2)
                if (epi1 in the_map):
                    the_map[epi1]=the_map[epi1]+'\t'+epi2
                else:
                    the_map[epi1]=epi2
                if (epi2 in the_map):
                    the_map[epi2]=the_map[epi2]+'\t'+epi1
                else:
                    the_map[epi2]=epi1
            cut=1
            while (cut<5):
                epi1_cut=epi1[cut:]
                if (len(epi1_cut)>5):
                    if (epi1_cut==epi2[0:len(epi1_cut)]):
                        print (epi1,' is almost subsequence by ' ,cut,' to ',epi2)
                        if (epi1 in the_map):
                            the_map[epi1]=the_map[epi1]+'\t'+epi2
                        else:
                            the_map[epi1]=epi2
                        if (epi2 in the_map):
                            the_map[epi2]=the_map[epi2]+'\t'+epi1
                        else:
                            the_map[epi2]=epi1

                epi1_cut=epi1[:-cut]
                if (len(epi1_cut)>5):
                    if (epi1_cut == epi2[(len(epi2)-len(epi1_cut)):]):
                        print (epi1,' is almost subsequence by ' ,cut,' to ',epi2)
                        if (epi1 in the_map):
                            the_map[epi1]=the_map[epi1]+'\t'+epi2
                        else:
                            the_map[epi1]=epi2
                        if (epi2 in the_map):
                            the_map[epi2]=the_map[epi2]+'\t'+epi1
                        else:
                            the_map[epi2]=epi1

                cut=cut+1

group={}
for epi in all_epi.keys():
    if (epi in the_map):
        the_group=the_map[epi].split('\t')
        uniq_group={}
        for ggg in the_group:
            uniq_group[ggg]=1
        uniq_group[epi]=1
        the_member=[]
        for k in sorted(uniq_group, key=len, reverse=False):
            the_member.append(k)
        string=the_member.pop(0)
        k=1
        for mmm in the_member:
            string=string+'|'
            string=string+mmm
            k=k+1
        while(k<9):
            string=string+'|'
            k=k+1

        group[string]=1
    else:

        string=epi
        k=1
        while(k<9):
            string=string+'|'
            k=k+1
        group[string]=1

NEW=open('consolidate_simple.txt','w')
g_i=1
for uniq_group in sorted(group.keys()):
    string='|'+str(g_i)+'|'+uniq_group+'|'
    NEW.write(string)
    NEW.write('\n')
    g_i=g_i+1
