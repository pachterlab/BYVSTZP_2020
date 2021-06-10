from .utils import nd

import numpy as np
import matplotlib.pyplot as plt

def volcano(x, y, ax, alpha=0.01, fc=2):
    ymask = y < -np.log(alpha)
    xmask = np.abs(x) < np.log(fc)

    mask = np.logical_or(xmask, ymask)

    xx = x[mask]
    yy = y[mask] 
    ax.scatter(xx,yy, color="grey")

    xx = x[~mask]
    yy = y[~mask]
    ax.scatter(xx,yy, color="black")

    ax.axhline(y=-np.log(alpha), color="red", linestyle="--")
    ax.axvline(x=np.log(fc), color="red", linestyle="--")
    ax.axvline(x=-np.log(fc), color="red", linestyle="--")
    ax.set(**{
        "xscale": "symlog",
        "yscale": "symlog",
        "xlabel": "Fold change",
        "ylabel": "-log(p-value)",
        "ylim": (0, np.max(y)*1.5),
        "xlim": (-np.max(np.abs(x))*1.5, np.max(np.abs(x))*1.5)
    })
    return ax
def violinplot(data, ax, **kwd): 
    xticklabels = kwd.get("xticklabels", [])
    xticks = kwd.get("xticks", [])
    selected = kwd.get("selected", None)
    color = kwd.get("color", "grey")
    
    if  len(xticks)==0: xticks = np.arange(len(data))+1;
    if  len(xticklabels)==0: xticklabels = np.arange(len(data))+1;
    assert(len(xticks) == len(xticklabels))
        
    violins = ax.violinplot(data, positions=xticks, showmeans=False, showmedians=False, showextrema=False)
    
    for vidx, v in enumerate(violins['bodies']):
        v.set_facecolor(color)
        v.set_edgecolor('black')
        v.set_alpha(1)
        if selected == vidx:
            v.set_facecolor("#D43F3A")

            
    
    for didx, d in enumerate(data):
        x = xticks[didx]
        xx = np.random.normal(x, 0.04, size=len(d))
        
        # actual points
        ax.scatter(xx, d, s = 5, color="white", edgecolor="black", linewidth=1)
        
        # mean and error bars
        mean = np.mean(d)
        stdev = np.sqrt(np.var(d))
        ax.scatter(x, mean, color="lightgrey", edgecolor="black", linewidth=1, zorder=10)    
        ax.vlines(x, mean - stdev, mean+stdev, color='lightgrey', linestyle='-', lw=2, zorder=9)
        
    ax.set(**{"xticks": xticks, "xticklabels":xticklabels})

    
    return ax

