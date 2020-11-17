import numpy as np

MATRIX=open('blosum62.txt','r')
title=MATRIX.readline()

title=title.strip()
title=title.split('\t')

ref={}
for line in MATRIX:
    line=line.strip()
    table=line.split('\t')
    aa1=table.pop(0)
    i=0
    for aa2 in title:
#        print(aa1,aa2)
        string=aa1+'_'+aa2
        ref[string]=float(table[i])
        string=aa2+'_'+aa1
        ref[string]=float(table[i])
        i=i+1
MATRIX.close()

all_epi={}
FILE=open('all_epitope','r')
for line in FILE:
    line=line.strip()
    all_epi[line]=1

the_map={}
for epi1 in all_epi.keys():
    for epi2 in all_epi.keys():
## now we calculate the maximal similarity score:
        if (len(epi1)<len(epi2)):
            score=-10000000
            i=0
            the_sum=0
            while(i<(len(epi2)-len(epi1))):
                iii=0
                while(iii<len(epi1)):
                    string=epi1[iii]+'_'+epi2[iii+i]
                    the_sum=the_sum+ref[string]#{epi1[iii],epi2[iii+i]}
                    iii=iii+1
                if (the_sum>score):
                    score=the_sum
                i=i+1
            #calculate substring self score
            the_sum_self=0
            iii=0
            while (iii<len(epi1)):
                string=epi1[iii]+'_'+epi1[iii]
                the_sum_self=the_sum_self+ref[string]
                iii=iii+1
            if (the_sum_self==the_sum):
                print (epi1,' is a subsequence' ,epi2, score)
##  consolidate this subsequence
                the_map[epi1]=epi2
        ## consolidate if the two sequences is shifted by one
        
            #calculate substring self score

            cut=1
            while (cut<5):
                score=-1000000
                epi1_cut=epi1[cut:]
                i=0
                the_sum=0
                while(i<(len(epi2)-len(epi1_cut))):
                    iii=0
                    while(iii<len(epi1_cut)):
                        string=epi1_cut[iii]+'_'+epi2[iii+i]
                        the_sum=the_sum+ref[string]#{epi1[iii],epi2[iii+i]}
                        iii=iii+1
                    if (the_sum>score):
                        score=the_sum
                    i=i+1
                the_sum_self=0
                iii=0
                while (iii<len(epi1_cut)):
                    string=epi1_cut[iii]+'_'+epi1_cut[iii]
                    the_sum_self=the_sum_self+ref[string]
                    iii=iii+1
                if (the_sum_self==the_sum):
                    print (epi1,' is almost subsequence by ' ,cut,' to ',epi2, score)
##  consolidate this subsequence
                    the_map[epi1]=epi2
                
                score=-1000000
                epi1_cut=epi1[0:-cut]
                i=0
                the_sum=0
                while(i<(len(epi2)-len(epi1_cut))):
                    iii=0
                    while(iii<len(epi1_cut)):
                        string=epi1_cut[iii]+'_'+epi2[iii+i]
                        the_sum=the_sum+ref[string]#{epi1[iii],epi2[iii+i]}
                        iii=iii+1
                    if (the_sum>score):
                        score=the_sum
                    i=i+1
                #calculate substring self score
                the_sum_self=0
                iii=0
                while (iii<len(epi1_cut)):
                    string=epi1_cut[iii]+'_'+epi1_cut[iii]
                    the_sum_self=the_sum_self+ref[string]
                    iii=iii+1
                if (the_sum_self==the_sum):
                    print (epi1,' is almost subsequence' ,epi2, score)
##  consolidate this subsequence
                    the_map[epi1]=epi2
                
                cut=cut+1
