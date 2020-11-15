#!/usr/bin/perl

open FILE, "/local/disk4/mqzhou/covid19/data/1102/allprot1102.fasta" or die;
$start=$ARGV[0];
$end=$ARGV[1];
$i=0;
while ($line=<FILE>){
    if (($i>=$start) && ($i<$end)){
    chomp $line;
    if ($line=~/>/){
        $lll=length($seq);
        $length{$name}.="\t$lll";
        @t=split '\|', $line;
        $name=$t[0];
        $seq='';
    }else{
        $seq.=$line;
    }
    }
    $i++;
}
close FILE;
@all_protein=keys %length;
foreach $ppp (@all_protein){
    @val=split "\t", $length{$ppp};
    @val=sort{$a<=>$b}@val;
    $vvv=$val[int(scalar(@val)/2)];
    $median{$ppp}=$vvv;
}

open FILE, "/local/disk4/mqzhou/covid19/data/1102/allprot1102.fasta" or die;
$start=$ARGV[0];
$end=$ARGV[1];
$i=0;
while ($line=<FILE>){
    if (($i>=$start) && ($i<$end)){
    chomp $line;
    if ($line=~/>/){
        $lll=length($seq);
        if ($lll == $median{$name}){
            $final{$name}=$seq;
        }
        @t=split '\|', $line;
        $name=$t[0];
        $seq='';
    }else{
        $seq.=$line;
    }
    }
    $i++;
}
close FILE;

@all_protein=keys %final;

open NEW, ">unified_protein.fasta.${start}" or die;
foreach $ppp (@all_protein){
    print NEW "$ppp\n";
    print NEW "$final{$ppp}\n";
}
close NEW;
