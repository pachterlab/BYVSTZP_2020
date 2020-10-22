#!/usr/bin/env python3
import sys
import numpy as np
from scipy.io import mmread
import anndata
import pandas as pd
import argparse

def main(matrix, cells, transcripts):
    COOmatrix = mmread(matrix)
    CSRmatrix = COOmatrix.tocsr()
    rows = pd.read_csv(cells, header=None, names=["cell_id"])
    cols = pd.read_csv(transcripts, header=None, names=["transcript_id", "gene_id", "gene_name"], sep="\t")
    adata = anndata.AnnData(X=CSRmatrix, obs=rows, var=cols)

    return adata

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Converts kallisto pseudo --quant for SMARTseq to adata.h5ad")
    p.add_argument('-m', action="store", dest="matrix", help="matrix abundance file" )
    p.add_argument('-c', action="store", dest="cells", help="cells file" )
    p.add_argument('-t', action="store", dest="transcripts", help="transcripts file" )

    p.add_argument("--outdir", help="path to save adata.h5ad", default="./")

    args = p.parse_args()

    adata = main(args.matrix, args.cells, args.transcripts)
    adata.write(args.outdir + "adata.h5ad")

