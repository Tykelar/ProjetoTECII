import ROOT
ficheiro = ROOT.TFile.Open("AmberTarget_Run_0.root","READ")

browser = ROOT.TBrowser()
tree = ficheiro.Get("Hits")

tree.Scan()
tree.Draw('particleCharge', 'particleCharge >= 0')

# hadd(final.root, *.root) -> junta todos os ficheiros em final.root
