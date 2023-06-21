import ROOT
import numpy as np
import sys

# Create a canvas to display the histograms
canvas = ROOT.TCanvas("canvas", "Canvas", 800, 600)

# Divide the canvas into two pads
canvas.Divide(1, 3)


# Create an empty combined histogram for each particle
combined_hist = {211: ROOT.THStack("combined_hist_211", "PDG 211 - Deposicao de energia dos pioes nos 4 detetores"), 
                 13: ROOT.THStack("combined_hist_13", "PDG 13 - Deposicao de energia dos muoes nos 4 detetores"),
                 "other": ROOT.THStack("combined_hist_other", "Deposicao de energia das restantes particulas nos 4 detetores")}


# Define a list of colors for each detector
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange]

filename = sys.argv[1]
f = ROOT.TFile.Open(filename, "READ")
results_file = ROOT.TFile.Open(filename.replace("AmberTarget", "results"), "RECREATE")

tree = f.Get("tracksData")

min_bin = 0.00001
max_bin = 60000

hist = {}

# Loop over the detectors and particle types
for i in range(4):
    for pdg in [211, 13, "other"]:
        if pdg == "other":
            selection = f"particlePDG != 211 && particlePDG != -211 && particlePDG != 13 && particlePDG != -13"
        else:
            selection = f"particlePDG == {pdg} || particlePDG == -{pdg}"
        
        # Create a new histogram with a unique name
        hist[i, pdg] = ROOT.TH1D(f"hist_{i}_{pdg}", f"Detector {i+1} - Particle PDG {pdg}", 500, min_bin, max_bin)
        
        # Set the histogram color
        hist[i, pdg].SetLineColor(colors[i])

        # Fill the histogram with data from the tree for the specific particle PDG in the current detector
        #tree.Draw(f"EdepDet{i}_keV>>hist_{i}_{pdg}", f"particlePDG == {pdg} || particlePDG == -{pdg}", "goff")
        tree.Draw(f"EdepDet{i}_keV>>hist_{i}_{pdg}", selection, "goff")

        # Add the histogram to the combined histogram for the specific particle PDG
        combined_hist[pdg].Add(hist[i, pdg])

        # Write the histogram to the output file
        results_file.cd()
        hist[i, pdg].Write()

for i, pdg in enumerate([211, 13, "other"]):
    canvas.cd(i+1)  # Select the i-th pad on the canvas
    combined_hist[pdg].Draw("nostack")
    ROOT.gPad.SetLogy()
    results_file.cd()
    combined_hist[pdg].Write()

canvas.Update()
canvas.Print("combined_hist.pdf")

# Close the files
f.Close()
results_file.Close()
