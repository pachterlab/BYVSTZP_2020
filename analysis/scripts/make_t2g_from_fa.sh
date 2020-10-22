#!/usr/bin/env bash
awk '/^>/' transcriptome.fa | tr -d ">" | tr ":" " " | awk '{print $1, $3, $5}' OFS="\t" > t2g_from_fa.txt
