#!/usr/bin/env bash

# untar files and move the tars into a folder
mkdir ../../data/SMARTseq/fastqs/tar
for d in ../../data/SMARTseq/fastqs/*.tar; do tar -xvf $d -C ../../data/SMARTseq/fastqs/ && mv $d ../../data/SMARTseq/fastqs/tar/ ; done
