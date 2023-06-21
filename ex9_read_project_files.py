import ROOT
import numpy as np
import sys

# Create a canvas to display the histograms
canvas = ROOT.TCanvas("canvas", "Canvas", 800, 600)

# Divide the canvas into two pads
canvas.Divide(1, 2)

# Create an empty combined histogram for each particle
combined_hist = {"primary": ROOT.THStack("combined_hist_primary", "Histograma de distribuicao de momento na componente Z de pioes primarios"), 
                 "secondary": ROOT.THStack("combined_hist_secondary", "Histograma de distribuicao de momento na componente Z de pioes secundarios")}

# Define a list of colors for each detector
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange]

filename = sys.argv[1]
f = ROOT.TFile.Open(filename, "READ")
results_file = ROOT.TFile.Open(filename.replace("AmberTarget", "results"), "RECREATE")

tree = f.Get("tracksData")

min_bin = 0.00001
max_bin = 200

hist = {}

# Loop over the detectors and particle types
for i in range(4):
    for origin in ["primary", "secondary"]:
        if origin == "primary":
            selection = f"(particlePDG == 211 || particlePDG == -211) && IsPrimary == 1"
        else:
            selection = f"(particlePDG == 211 || particlePDG == -211) && IsPrimary == 0"

        # Create a new histogram with a unique name
        hist[i, origin] = ROOT.TH1D(f"hist_{i}_{origin}", f"Detector {i+1} - Particle {origin}", 500, min_bin, max_bin)

        # Set the histogram color
        hist[i, origin].SetLineColor(colors[i])

        # Fill the histogram with data from the tree for the specific particle PDG in the current detector
        tree.Draw(f"pZ_GeV>>hist_{i}_{origin}", selection, "goff")

        # Add the histogram to the combined histogram for the specific particle PDG
        combined_hist[origin].Add(hist[i, origin])

        # Write the histogram to the output file
        results_file.cd()
        hist[i, origin].Write()

# Loop over the particle types and draw the combined histograms on the canvas
for i, origin in enumerate(["primary", "secondary"]):
    canvas.cd(i+1)  # Select the i-th pad on the canvas
    combined_hist[origin].Draw("nostack")
    ROOT.gPad.SetLogy()
    results_file.cd()
    combined_hist[origin].Write()

canvas.Update()
canvas.Print("combined_hist9.pdf")

# Close the files
f.Close()
results_file.Close()
