#!/usr/bin/perl

@all_seq=glob "random_5000_split/*";
$start=$ARGV[0];
$end=$ARGV[1];

mkdir random_5000_split_result_whole;
$i=0;
foreach $seq (@all_seq){
    %len=();
    %num=();

    if (($i>=$start) && ($i<$end)){
        @t=split '/', $seq;
        system "./ncbi-blast-2.10.1+/bin/makeblastdb -in $seq -parse_seqids -blastdb_version 5  -dbtype nucl";
        system "./ncbi-blast-2.10.1+/bin/blastn -db $seq -query random_5000.fasta -out random_5000_split_result_whole/$t[-1]";

        open FILE, "random_5000_split_result_whole/$t[-1]" or die;
        $file=$t[-1];
        while ($line=<FILE>){
            if ($line=~/Query=/){
                chomp $line;
                @t=split " ", $line;
                $name1=$t[1];
                <FILE>;
                $line=<FILE>;
                chomp $line;
                @t=split 'Length=', $line;
                $len{$name1}=$t[1];
            }
            if ($line=~/>/){
                chomp $line;
                @t=split '>', $line;
                $name2=$t[1];

                $line=<FILE>;
                chomp $line;
                @t=split 'Length=', $line;
                $len{$name2}=$t[1];
            }
            if ($line=~/Score =/){
                $line=<FILE>;
                @t=split "Identities = ", $line;
                @t=split '/', $t[1];
                $num{$name1,$name2}+=$t[0];
            }
        }
        close FILE;

        open NEW, ">random_5000_split_result_whole/${file}.result" or die;
        @names=keys %len;
        foreach $nnn1 (@names){
            foreach $nnn2 (@names){
                if (exists $num{$nnn1,$nnn2}){
                    $ratio=2*$num{$nnn1,$nnn2}/($len{$nnn1}+$len{$nnn2});
                    print NEW "$nnn1\t$nnn2\t$ratio\n";
                }
            }
        }
        close NEW;
        system "rm random_5000_split_result_whole/$file";
    }
    $i++;
}
