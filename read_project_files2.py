import ROOT

# Create a canvas to display the histograms
canvas = ROOT.TCanvas("canvas", "Canvas")

# Create an empty combined histogram
combined_hist = ROOT.TH1D("combined_hist", "Combined Histogram", 100, 0, 100)

# Define a list of colors for each file
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange]

# Loop over the four files
for i in range(4):
    # Construct the filename and open the file
    filename = "AmberTarget_Run_" + str(i) + ".root"
    f = ROOT.TFile.Open(filename, "READ")
    
    # Get the tree and create a new histogram with a unique name
    tree = f.Get("edep_Per_Event")
    hist = ROOT.TH1D("hist_"+str(i), "Histogram "+str(i), 100, 0, 100)
    
    # Set the histogram color
    hist.SetLineColor(colors[i])
    
    # Fill the histogram with data from the tree
    tree.Draw("detector3>>hist_"+str(i), "detector3 > 0")
    
    # Add the histogram to the combined histogram
    combined_hist.Add(hist)

# Draw the combined histogram on the canvas
combined_hist.Draw()

# Update the canvas and save it to a PDF file
canvas.Update()
canvas.Print("combined_histogram.pdf")

