import ROOT
ficheiro = ROOT.TFile.Open("AmberTarget_Run_0.root","READ")

browser = ROOT.TBrowser()
tree = ficheiro.Get("edep_Per_Event")

tree.Scan()
tree.Draw('detector3', 'detector3 > 0')

# hadd(final.root, *.root) -> junta todos os ficheiros em final.root
