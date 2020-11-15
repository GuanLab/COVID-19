#!/usr/bin/perl

mkdir random_5000_split;
open FILE, "random_5000.fasta" or die;
$i=0;
while ($line=<FILE>){
    chomp $line;
    if ($line=~/^>/){
        $name=$line;
        open NEW, ">random_5000_split/${i}" or die;
        print NEW "$line\n";
        $i++;
    }else{
        print NEW "$line\n";
    }
}


