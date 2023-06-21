import ROOT
import numpy as np
import sys

# Create a canvas to display the histograms

canvas = ROOT.TCanvas("canvas", "Canvas")

# Create an empty combined histogram
combined_hist = ROOT.THStack("combined_hist", "Deposicao de energia em cada detetor")

# Define a list of colors for each file
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange]


filename = sys.argv[1]
f = ROOT.TFile.Open(filename, "READ")
results_file=ROOT.TFile.Open(filename.replace("AmberTarget","results"),"RECREATE")

tree = f.Get("edep_Per_Event")

arr_max = np.zeros(4)
for j in range(4):
	arr_max[j] = tree.GetMaximum("detector" + str(j))

#max_bin = max(arr_max)
min_bin = 0
max_bin = 600000

# Loop over the four files
for i in range(4):
	# Construct the filename and open the file

	# Get the tree and create a new histogram with a unique name
	hist = ROOT.TH1D("hist_"+str(i), "Histogram "+str(i), 500, min_bin, max_bin)

	# Set the histogram color
	hist.SetLineColor(colors[i])

	# Fill the histogram with data from the tree
	tree.Draw("detector"+str(i)+ ">>hist_"+str(i), "detector"+str(i)+" > 0")

	# Add the histogram to the combined histogram
	combined_hist.Add(hist)

	ROOT.gPad.SetLogy()
	results_file.cd()
	hist.Write()

# Draw the combined histogram on the canvas
combined_hist.Draw("nostack")
results_file.cd()
combined_hist.Write()
# Update the canvas and save it to a PDF file
canvas.Update()
canvas.Print("HistogramaEx1.pdf")

leg = ROOT.TLegend(0.6,0.7,0.9,0.9)
leg.SetTextFont(42)
leg.SetTextSize(0.04)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.AddEntry(combined_hist, "Deposicao de energia", "combined_hist")

hist.GetXaxis().SetTitle("Comprimento")
hist.GetYaxis().SetTitle("Deposição de energia")
hist.Draw()

leg.Draw()

# array em numpy
# ver max e min
