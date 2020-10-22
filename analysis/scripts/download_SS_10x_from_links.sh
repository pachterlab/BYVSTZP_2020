#!/usr/bin/env bash

# SMARTseq
wget --continue --quiet -P ../../data/SMARTseq/fastqs/ -i ../../reference/smart-seq_file_links.txt

# 10xv3
wget --continue --quiet -P ../../data/10xv3/fastqs/ -i ../../reference/10xv3_file_links.txt
