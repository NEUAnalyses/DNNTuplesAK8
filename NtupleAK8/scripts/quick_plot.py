import numpy  as np
import pandas as pd
import uproot
import argparse
import matplotlib.pyplot as plt


histograms = {
    "jet_pt"  : [100, [0, 1000]],
    "alpha"   : [100, [0, 1   ]],
    "ntracks" : [ 51, [0, 50  ]]
}


def main():
    parser = argparse.ArgumentParser(description='Quick plots for DJTagger')
    parser.add_argument("rootfile", help="input root file")
    args = parser.parse_args()

    tree = uproot.open(args.rootfile)["deepntuplizer"]["tree"]
    for var, opt in histograms.items():
	print "darwing the variable : " , var, opt
	plt.figure(figsize=(5,5))
        plt.hist(tree.array(var), bins=opt[0], range=opt[1],alpha=0.5, histtype='stepfilled', normed=1)
	plt.savefig("djtagger_plot_" + var + ".pdf")
	plt.show()


if __name__ == '__main__':
    main()
    raw_input()


