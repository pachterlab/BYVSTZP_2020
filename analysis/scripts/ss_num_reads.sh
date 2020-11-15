#!/usr/bin/env bash
for f in ../../data/SMARTseq/fastqs/*R1.fastq.gz; do echo $f >> names.txt && zcat $f | wc -l | xargs echo "0.25*" | bc | cut -f1 -d'.' >> nr.txt; done

cat names.txt | rev | cut -f1 -d"_" --complement | rev > tmp && mv tmp names.txt

paste -d'\t' names.txt nr.txt > read_data.txt
