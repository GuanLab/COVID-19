#!/usr/bin/perl

$i=0;
while ($i<9500000){
    $v=$i+100000;
    print "perl uniform_protein.pl $i $v &\n";
    $i=$i+100000;
}


