#!/usr/bin/perl

open FILE, "/local/disk4/mqzhou/covid19/data/1102/sequences_2020-11-02_07-27.fasta" or die;
$i=0;
while ($line=<FILE>){
    chomp $line;
    if ($line=~/^>/){
        $name=$line;
        $id[$i]=$name;
        $i++;
    }else{
        $ref{$name}.=$line;
    }
}



use List::Util qw(shuffle) ;
@id= shuffle(@id); 


open NEW, ">whole_genome.fasta" or die;
$itmp=0;
while ($itmp<scalar(@id)){
    @total=split "", $ref{$id[$itmp]};
    $n=scalar(@total);
    print "$n\n";
    if ($n>29000){
        print NEW "$id[$itmp]\n";
        print NEW "$ref{$id[$itmp]}\n";
    }

    $itmp=$itmp+1;
}
close NEW;



