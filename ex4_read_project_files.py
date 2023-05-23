#TH2D('nome', 'finto', nbinx, minx, maxx, nbiny, miny, maxy)
# colocar 'colz' para cores





import ROOT
import numpy as np
import sys

# Create a canvas to display the histograms

canvas4 = ROOT.TCanvas("canvas4", "Canvas 4")

# Create an empty combined histogram
combined_hist4 = ROOT.THStack("combined_hist4", "Combined Histogram 4")

# Define a list of colors for each file
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange]


filename4 = sys.argv[1]
f4 = ROOT.TFile.Open(filename4, "READ")
results_file4=ROOT.TFile.Open(filename4.replace("AmberTarget","results"),"RECREATE") 
#results_file4 = ROOT.TFile.Open(filename4.replace("AmberTarget", "results4"), "CREATE")


tree4 = f4.Get("hadronicVertex")




#m definir os bins
nbiny = 500
nbinx = nbiny 
minx = -400
maxx = 0
miny = 0
maxy = 600000

# Loop over the four files
for i in range(4):
	# Construct the filename and open the file

	# Get the tree and create a new histogram with a unique name
	hist4 = ROOT.TH1D("hist4_"+str(i), "Histogram 4 "+str(i), nbinx, minx, maxx)

	# Set the histogram color
	hist4.SetLineColor(colors[i])

	# Fill the histogram with data from the tree
	#tree4.Draw("detector"+str(i)+ ">>hist4_"+str(i), "detector"+str(i)+" > 0") 
	tree4.Draw("vertexPosZ_cm>>hist4_"+str(i), "IsPrimary==1")

	# Add the histogram to the combined histogram
	combined_hist4.Add(hist4)

	ROOT.gPad.SetLogy()
	results_file4.cd()
	hist4.Write()

# Draw the combined histogram on the canvas
combined_hist4.Draw("nostack")
results_file4.cd()
combined_hist4.Write()
# Update the canvas and save it to a PDF file
canvas4.Update()
canvas4.Print("combined_histogram4.pdf")

leg = ROOT.TLegend(0.6,0.7,0.9,0.9)
leg.SetTextFont(42)
leg.SetTextSize(0.04)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.AddEntry(combined_hist4, "vertex hadrónico primários e secundários em função de Z", "combined_hist4")
leg.Draw()

# array em numpy
# ver max e min

