import ROOT
import numpy as np
import sys

# Create a canvas to display the histograms
canvas1 = ROOT.TCanvas("canvas1", "Posição X")
canvas1.Divide(2,2)
canvas2 = ROOT.TCanvas("canvas2", "Posição Y")
canvas2.Divide(2,2)

# Define a list of colors for each file
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange]

filename = sys.argv[1]
f = ROOT.TFile.Open(filename, "READ")
results_file=ROOT.TFile.Open(filename.replace("AmberTarget","results"),"RECREATE")

tree = f.Get("Hits")

#max_bin = max(arr_max)
minx = -40
maxx = 40
miny = -40
maxy = 40
nbinx = 500
nbiny = nbinx

hist={}

# Loop over the four files
for i in range(4):
	# Construct the filename and open the file

	# Get the tree and create a new histogram with a unique name
	hist[i] = ROOT.TH2D("hist_"+str(i), "Detetor "+str(i), nbinx, minx, maxx, nbiny, miny, maxy)
	# Set the histogram color
	hist[i].SetLineColor(colors[i])
	
	# Fill the histogram with data from the tree
	canvas1.cd(i+1)
	tree.Draw("particleCharge:hitPosX_cm>>hist_"+str(i), "", "COLZ") # Y, X
	#tree.Draw("")
	
	#Criar um canvas cd
	#Em cada um fazer o draw do histograma

	results_file.cd()
	hist[i].Write()

	canvas2.cd(i+1)
	tree.Draw("particleCharge:hitPosY_cm>>hist_"+str(i), "", "COLZ")
	results_file.cd()
	hist[i].Write()
