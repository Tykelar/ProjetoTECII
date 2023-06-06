import ROOT
import numpy as np
import sys

# Create a canvas to display the histograms
canvas7 = ROOT.TCanvas("canvas7", "Canvas 7")

# Create an empty combined histogram
combined_hist7 = ROOT.THStack("combined_hist7", "Distribuicao temporal dos hits por detetor")

# Define a list of colors for each file
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange]

filename7 = sys.argv[1]
f7 = ROOT.TFile.Open(filename7, "READ")
results_file7 = ROOT.TFile.Open(filename7.replace("AmberTarget","results"),"RECREATE") 

tree7 = f7.Get("Hits")

#m definir os bins
nbiny = 500
nbinx = nbiny 
minx = 0.0001
maxx = 20000
miny = 0
maxy = 600000
hist7={}

# Loop over the four files
for i in range(4):
	# Construct the filename and open the file

	# Get the tree and create a new histogram with a unique name
	hist7[i] = ROOT.TH1D("hist7_"+str(i), "Histogram 7 "+str(i), nbinx, minx, maxx)

	# Set the histogram color
	#hist7[i].SetLineColor(colors[i])


	# Fill the histogram with data from the tree
	tree7.Draw("particleHitTime_ns>>hist7_"+str(i),"")

	
	# Add the histogram to the combined histogram
	combined_hist7.Add(hist7[i])

	#ROOT.gPad.SetLogy()
	results_file7.cd()
	hist7[i].Write()

# Draw the combined histogram on the canvas


combined_hist7.Draw("nostack")
ROOT.gPad.SetLogy()
results_file7.cd()
combined_hist7.Write()

# Update the canvas and save it to a PDF file
canvas7.Update()
canvas7.Print("combined_histogram7.pdf")

leg = ROOT.TLegend(0.6,0.7,0.9,0.9)
leg.SetTextFont(42)
leg.SetTextSize(0.04)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.AddEntry(combined_hist7, "Distribuicao temporal dos hits por detetor", "combined_hist7")
leg.Draw()
