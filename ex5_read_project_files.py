import ROOT
import numpy as np
import sys

# Create a canvas to display the histograms
canvas = ROOT.TCanvas("canvas", "Canvas")

# Define a list of colors for each file
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange]

filename = sys.argv[1]
f = ROOT.TFile.Open(filename, "READ")
results_file=ROOT.TFile.Open(filename.replace("AmberTarget","results"),"RECREATE")

tree = f.Get("Hits")
#tree.Scan("*", "IsPrimary==1")

#arr_max = np.zeros(2)
#d = {"0": "X", "1": "Y"}
#values_list = list(d.values())
#for j in range(2):
#	arr_max[j] = tree.GetMaximum("hitPos" + values_list[j] + "_cm")

#max_bin = max(arr_max)
minx = -40
maxx = 40
miny = -40
maxy = 40
nbinx = 500
nbiny = nbinx

canvas.Divide(2,2)

hist={}
# Loop over the four files
for i in range(4):
	# Construct the filename and open the file

	# Get the tree and create a new histogram with a unique name
	hist[i] = ROOT.TH2D("hist_"+str(i), "Histogram "+str(i), nbinx, minx, maxx, nbiny, miny, maxy)
	# Set the histogram color
	hist[i].SetLineColor(colors[i])
	
	# Fill the histogram with data from the tree
	canvas.cd(i+1)
	tree.Draw("hitPosY_cm:hitPosX_cm>>hist_"+str(i), "", "COLZ") # Y, X
	
	#Criar um canvas cd
	#Em cada um fazer o draw do histograma

	results_file.cd()
	hist[i].Write()
