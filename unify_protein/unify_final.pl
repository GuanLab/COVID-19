#!/usr/bin/perl

open FILE, "unified_protein.fasta.all" or die;
$i=0;
while ($line=<FILE>){
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

open FILE, "unified_protein.fasta.all" or die;
$i=0;
while ($line=<FILE>){
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
    $i++;
}
close FILE;

@all_protein=keys %final;

open NEW, ">unified_protein.fasta.final" or die;
foreach $ppp (@all_protein){
    print NEW "$ppp\n";
    print NEW "$final{$ppp}\n";
}
close NEW;
