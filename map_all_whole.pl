#!/usr/bin/perl

#169265

$i=0;
while ($i<338530){
    $end=$i+3000;
    system "perl map_whole_to_whole.pl $i $end &";
    $i=$i+3000;
}

