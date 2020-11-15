#!/usr/bin/perl

perl select_whole_genome.pl
perl random_selection.pl


### this is the subtyping line


### blast all epitopes to proteins
## build blastdb
./ncbi-blast-2.10.1+/bin/makeblastdb -in whole_genome.fasta -parse_seqids -blastdb_version 5 -title "wholegenome" -dbtype nucl -max_hsps 50000


## create epitope fasta
perl create_epitope_fasta.pl
./ncbi-blast-2.10.1+/bin/tblastn -db whole_genome.fasta -query all_epitope.fasta  -out epitope.results.out

## build blastdb
./ncbi-blast-2.10.1+/bin/makeblastdb -in random_5000.fasta -parse_seqids -blastdb_version 5 -title "random_5000" -dbtype nucl -max_hsps 50000




## uniform all protein sequences by names /local/disk4/mqzhou/covid19/data/1102/allprot1102.fasta
perl uniform_protein.pl



## uniform and combine all epitopes
python consolidate_all_epitope_simple.py


perl map_all_protein.pl
perl map_all_epitope.pl

perl split_random_5000.pl

perl map_all_5000_whole.pl


## randomly select 100000 proteins
perl random_selection_protein.pl

## build protein database

./ncbi-blast-2.10.1+/bin/makeblastdb -in unified_protein.fasta.final -parse_seqids -blastdb_version 5 -title "unified_protein.fasta.final"  -dbtype prot

## map epitopes to proteins
./ncbi-blast-2.10.1+/bin/blastp  -db unify_protein/unified_protein.fasta.final -query all_epitope.fasta  -out epitope.results.out.protein

###
perl map_protein_5000.pl

## constract protein-containing fastas
perl construct_protein_containing_fasta.pl
