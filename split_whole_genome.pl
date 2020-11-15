#!/usr/bin/perl

mkdir whole_genome_split;
open FILE, "whole_genome.fasta" or die;
$i=0;
while ($line=<FILE>){
    chomp $line;
    if ($line=~/^>/){
        $name=$line;
        open NEW, ">whole_genome_split/${i}" or die;
        print NEW "$line\n";
        $i++;
    }else{
        print NEW "$line\n";
    }
}


