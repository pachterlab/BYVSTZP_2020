#!/usr/bin/env bash
zcat ../../reference/transcriptome.fa.gz | grep "chr:Y" | tr -d ">" | sed  s/gene_id\://g | sed s/gene_name\://g | sed s/transcript_name\://g > chry.txt
