#!/usr/bin/perl

@all_seq=glob "random_5000_split/*";
$start=$ARGV[0];
$end=$ARGV[1];

mkdir random_5000_split_result;
$i=0;
foreach $seq (@all_seq){

    if (($i>=$start) && ($i<$end)){
        @t=split '/', $seq;
        system "./ncbi-blast-2.10.1+/bin/makeblastdb -in $seq -parse_seqids -blastdb_version 5  -dbtype nucl";
        system "./ncbi-blast-2.10.1+/bin/tblastn -db $seq -query unify_protein/unified_protein.fasta.final -out random_5000_split_result/$t[-1]";

    }
    $i++;
}
