import ROOT
import numpy as np
import sys

# Create a canvas to display the histograms

canvas = ROOT.TCanvas("canvas", "Canvas")

# Create an empty combined histogram
combined_hist2 = ROOT.THStack("combined_hist2", "Combined Histogram Ex2")

# Define a list of colors for each file
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange]


filename2 = sys.argv[1]
f2 = ROOT.TFile.Open(filename2, "READ")
results_file2 =ROOT.TFile.Open(filename2.replace("AmberTarget","results"),"RECREATE")

tree2 = f2.Get("tracksData")

#max_bin = max(arr_max)
min_bin = 0.00001
max_bin = 600000

hist2={}

# Loop over the four files
for i in range(4):
	# Construct the filename and open the file

	# Get the tree and create a new histogram with a unique name
	hist2[i] = ROOT.TH1D("hist2_"+str(i), "Histogram "+str(i), 500, min_bin, max_bin)
	
	# Set the histogram color
	hist2[i].SetLineColor(colors[i])

	# Fill the histogram with data from the tree
	tree2.Draw("EdepDet" + str(i)+"_keV>>hist2_"+str(i), "particlePDG==211 || particlePDG == -211 || particlePDG == 13 || particlePDG == -13 ","goff")

	# Add the histogram to the combined histogram
	combined_hist2.Add(hist2[i])
	
	#ROOT.gPad.SetLogy()
	results_file2.cd()
	hist2[i].Write()

# Draw the combined histogram on the canvas
combined_hist2.Draw("nostack")
ROOT.gPad.SetLogy()
results_file2.cd()
combined_hist2.Write()
# Update the canvas and save it to a PDF file
canvas.Update()
canvas.Print("combined_hist2.pdf")

leg = ROOT.TLegend(0.6,0.7,0.9,0.9)
leg.SetTextFont(42)
leg.SetTextSize(0.04)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.AddEntry(combined_hist2, "Deposicao de energia Piões e Muões", "combined_hist2")
leg.Draw()

