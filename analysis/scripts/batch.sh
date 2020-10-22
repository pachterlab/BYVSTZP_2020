#!/usr/bin/env bash

# make batch.txt file
ls ../../data/SMARTseq/fastqs/*.tar | sort | awk '{cell=substr($1,0,length($1)-10); print cell, cell"_R1.fastq.gz ", cell"_R2.fastq.gz" }' OFS="\t" > ../../data/SMARTseq/smart-seq_batch.txt

