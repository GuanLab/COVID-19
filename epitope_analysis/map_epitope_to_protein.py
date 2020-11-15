
the_map={}
FILE=open('../epitope.results.out.protein','r')
for line in FILE:
    line=line.strip()
    if ('Query= Epitope ' in line):
        t=line.split('Query= Epitope ')
        name=t[1]
        line=FILE.readline()
        line=FILE.readline()
        line=FILE.readline()
        line=FILE.readline()
        line=FILE.readline()
        line=FILE.readline()
        line=line.strip()
        t=line.split(' ')
        protein=t[0]
        the_map[name]=protein
FILE.close()

the_seq={}
FILE=open('../all_epitope.fasta','r')
for line in FILE:
    line=line.strip()
    if ('>' in line):
        t=line.split(' ')
        name=t[1]
        line=FILE.readline()
        line=line.strip()
        the_seq[name]=line
FILE.close()
OLD=open('summary.txt','r')
NEW=open('summary.txt.mapped','w')
for line in OLD:
    line=line.strip()
    table=line.split('\t')
    NEW.write('Epitope_'+table[0]+'\t'+the_seq[table[0]]+'\t'+the_map[table[0]]+'\t'+table[1]+'\n')
OLD.close()
NEW.close()




