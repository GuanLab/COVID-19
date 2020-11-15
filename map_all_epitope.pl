#!/usr/bin/perl

#169265

$i=0;
while ($i<169265){
    $end=$i+50000;
    system "perl map_epitope.pl $i $end &";
    $i=$i+5000;
}

