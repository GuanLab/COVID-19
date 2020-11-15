#!/usr/bin/perl

open FILE, "/local/disk4/mqzhou/covid19/results/epitope/all_epitopes" or die;
open NEW, ">all_epitope.fasta" or die;
$i=1;
while ($line=<FILE>){
    chomp $line;
    print NEW ">Epitope $i\n";
    print NEW "$line\n";
    $i++;
}


