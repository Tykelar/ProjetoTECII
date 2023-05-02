import ROOT
ficheiro0=ROOT.TFile.Open("AmberTarget_Run_0.root","READ")
browser0 = ROOT.TBrowser()

tree0 = ficheiro0.Get('edep_Per_Event')
tree0.Scan()
tree0.Draw('detector3', 'detector3>0')


TFile(filename_analise)
