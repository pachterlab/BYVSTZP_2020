#!/usr/bin/env bash

# make batch.txt file
ls mop_SMARTseq/fastqs/*.tar | sort | awk '{cell=substr($1,0,length($1)-10); print cell, cell"_R1.fastq.gz ", cell"_R2.fastq.gz" }' OFS="\t" > smart-seq_batch.txt

