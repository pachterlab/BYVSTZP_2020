#!/usr/bin/env bash
time kallisto pseudo --quant -i reference/index.idx -o ./mop_SMARTseq/out/ -b smart-seq_batch.txt -t 16
