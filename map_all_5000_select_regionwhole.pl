#!/usr/bin/perl

#169265

$i=0;
while ($i<5100){
    $end=$i+100;
    system "perl map_5000_whole_to_5000_whole_select_region.pl $i $end &";
    $i=$i+100;
}

