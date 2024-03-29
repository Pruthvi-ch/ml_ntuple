import ROOT as rt
import array as ar
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--inHE', dest='inHE', type=str,
                    help='infile HE')
parser.add_argument('--outHE1', dest='outHE1', type=str,
                    help='outfile HE1')

args = parser.parse_args()

print(args.inHE)
inHE = rt.TFile.Open(args.inHE, 'READ')
outfile2 = rt.TFile.Open(args.outHE1, 'RECREATE')

#inHE = rt.TFile.Open("/eos/user/p/psuryade/ml_ntuples/08_6/ml_ntuple_HEp_nn.root", "READ")
#outfile2 = rt.TFile.Open("/eos/user/p/psuryade/ml_ntuples/08_6/ml_ntupleHE1p_nn.root", "RECREATE")

nHit = ar.array('i', [0])
X_ = ar.array('f', 20000*[0.0])
Y_ = ar.array('f', 20000*[0.0])
E_ = ar.array('f', 20000*[0.0])
t_ = ar.array('f', 20000*[0.0])
adc_ = ar.array('H', 20000*[0])
thick_ = ar.array('H', 20000*[0])
mode_ = ar.array('H', 20000*[0])
zside_ = ar.array('h', 20000*[0])
intree = []
intreeB = []
outtree2 = []

#hADC_200_wi = inHE.Get('Events/hADC_200_wi').Clone()
#hE_200 = inHE.Get('Events/hE_200').Clone()

for i in range(27, 34):
    intree.append(inHE.Get("Events/layer_" + str(i)))
    outtree2.append(rt.TTree("layer_" + str(i) , "hits in layer" + str(i)))
    outtree2[-1].Branch("nHit", nHit, "nHit/I")
    outtree2[-1].Branch("X", X_, "X[nHit]/F")
    outtree2[-1].Branch("Y", Y_, "Y[nHit]/F")
    outtree2[-1].Branch("SimHitE", E_, "SimHitE[nHit]/F")
    outtree2[-1].Branch("time", t_, "time[nHit]/F")
    outtree2[-1].Branch("ADC", adc_, "ADC[nHit]/s")
    outtree2[-1].Branch("Thick", thick_, "Thick[nHit]/s")
    outtree2[-1].Branch("ADC_mode", mode_, "ADC_mode[nHit]/s")
    outtree2[-1].Branch("z_side", zside_, "z_side[nHit]/S")

n = intree[-1].GetEntriesFast()
for j in range(n):
    print(j)
    for i in range(27,34):
        intree[i-27].GetEntry(j)
        nHitsi = intree[i-27].nHit 
        nHit[0] = intree[i-27].nHit
        for ii in range(nHitsi):
            X_[ii] = intree[i-27].X[ii]
            Y_[ii] = intree[i-27].Y[ii]
            E_[ii] = intree[i-27].SimHitE[ii]
            t_[ii] = intree[i-27].time[ii]
            adc_[ii] = intree[i-27].ADC[ii]
            thick_[ii] = intree[i-27].Thick[ii]
            mode_[ii] = intree[i-27].ADC_mode[ii]
            zside_[ii] = intree[i-27].z_side[ii]
        outtree2[i-27].Fill()
        #print(nHit[0])

tdir = outfile2.mkdir("Events")
#tdir = rt.TDirectory('Events', 'Events')
tdir.cd()
#hADC_200_wi.Write()
#hE_200.Write()

for i in range(27, 34):
    outtree2[i-27].Write()
#tdir.Write()
