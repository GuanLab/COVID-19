#!/usr/bin/perl

@all_seq=glob "whole_genome_split/*";
$start=$ARGV[0];
$end=$ARGV[1];

print "$start\t$end\n";
while ($start<$end){
    system "./ncbi-blast-2.10.1+/bin/tblastn -db whole_genome_split/${start} -query all_epitope.fasta -out epitope_split_result/${start}";

    $start++;
}
