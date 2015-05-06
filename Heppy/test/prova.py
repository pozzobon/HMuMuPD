#! /usr/bin/env python
# -*- coding: utf-8 -*-
import ROOT
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer import *
from HMuMuPD.Heppy.analyzers.ttHMuMuObjectsFormat import *

cfg.Analyzer.nosubdir=True

#######################
### TRIGGERANALYZER ###
#######################
from PhysicsTools.Heppy.analyzers.core.TriggerBitAnalyzer import TriggerBitAnalyzer
triggerAnalyzer = cfg.Analyzer(
  verbose = False,
  class_object = TriggerBitAnalyzer,
  # grouping several paths into a single flag
  # v* can be used to ignore the version of a path
  triggerBits = {
    'MET':['HLT_PFHT350_PFMET120_NoiseCleaned_v1','HLT_PFMET170_NoiseCleaned_v1','HLT_PFMET120_NoiseCleaned_BTagCSV07_v1'],
    'JET':['HLT_PFJet260_v1'],
  },
  # processName = 'HLT',
  # outprefix = 'HLT'
  # setting 'unrollbits' to true will not only store the OR for each set of trigger bits but also the individual bits
  # caveat: this does not unroll the version numbers
  unrollbits = True,
)



######################
### PILEUPANALYZER ###
######################
from PhysicsTools.Heppy.analyzers.core.PileUpAnalyzer import PileUpAnalyzer
pileupAnalyzer = PileUpAnalyzer.defaultConfig



######################
### VERTEXANALYZER ###
######################
from PhysicsTools.Heppy.analyzers.objects.VertexAnalyzer import VertexAnalyzer
vertexAnalyzer = VertexAnalyzer.defaultConfig



######################
### LEPTONANALYZER ###
######################
from PhysicsTools.Heppy.analyzers.objects.LeptonAnalyzer import LeptonAnalyzer
leptonAnalyzer = cfg.Analyzer(
  # Cloned default values for practical purposes...
  # If changed, please leave the default in a comment
  class_object = LeptonAnalyzer,

  ########################
  ### Lepton - General ###
  ########################
  doMuScleFitCorrections = False, # "rereco"
  doRochesterCorrections = False,
  doElectronScaleCorrections = False, # "embedded" in 5.18 for regression
  doSegmentBasedMuonCleaning = False,
  # minimum deltaR between a loose electron and a loose muon (on overlaps, discard the electron)
  min_dr_electron_muon = 0.02,
  # do MC matching
  do_mc_match = True, # note: it will in any case try it only on MC, not on data
  match_inclusiveLeptons = False, # match to all inclusive leptons

  ##########################
  ### Electron - General ###
  ##########################
  electrons = 'slimmedElectrons',
  rhoElectron = 'fixedGridRhoFastjetAll',

  ele_isoCorr = "rhoArea",
  el_effectiveAreas = "Phys14_25ns_v1", #(can be 'Data2012' or 'Phys14_25ns_v1')
  ele_tightId = "Cuts_2012",

  ### Electron selection - First step
  inclusive_electron_id = "POG_Cuts_ID_CSA14_25ns_v1_Veto", # default is "",
  inclusive_electron_pt = 5,
  inclusive_electron_eta = 2.5,
  inclusive_electron_dxy = 0.5,
  inclusive_electron_dz = 1.0,
  inclusive_electron_lostHits = 1.0,

  ### Electron selection - Second step
  loose_electron_id = "POG_Cuts_ID_CSA14_25ns_v1_Veto",
  loose_electron_pt = 7,
  loose_electron_eta = 2.4,
  loose_electron_dxy = 0.05,
  loose_electron_dz = 0.2,
  loose_electron_lostHits = 1.0,
  loose_electron_relIso = 0.4,

  ######################
  ### Muon - General ###
  ######################
  muons = 'slimmedMuons',
  rhoMuon = 'fixedGridRhoFastjetAll',

  mu_isoCorr = "deltaBeta" ,
  mu_effectiveAreas = "Phys14_25ns_v1", #(can be 'Data2012' or 'Phys14_25ns_v1')

  ### Muon selection - First step
  inclusive_muon_id = "POG_ID_Loose",
  inclusive_muon_pt = 3,
  inclusive_muon_eta = 2.4,
  inclusive_muon_dxy = 0.5,
  inclusive_muon_dz = 1.0,

  ### Muon selection - Second step
  loose_muon_id = "POG_ID_Loose",
  loose_muon_pt = 5,
  loose_muon_eta = 2.4,
  loose_muon_dxy = 0.05,
  loose_muon_dz = 0.2,
  loose_muon_relIso = 0.4
)



###################
### JETANALYZER ###
###################
from PhysicsTools.Heppy.analyzers.objects.JetAnalyzer import JetAnalyzer
jetAnalyzer = cfg.Analyzer(
  # Cloned default values for practical purposes...
  # If changed, please leave the default in a comment
  class_object = JetAnalyzer,

  #####################
  ### Jet - General ###
  #####################
  jetCol = 'slimmedJets',

  jetPt = 25.,
  jetEta = 4.7,
  jetEtaCentral = 2.4,
  jetLepDR = 0.4,
  jetLepArbitration = (lambda jet,lepton : jet), # you can decide which to keep in case of overlaps -> keeping the jet
  minLepPt = 10,
  relaxJetId = False,
  doPuId = False, # Not commissioned in 7.0.X
  doQG = False,
  recalibrateJets = False,
  shiftJEC = 0, # set to +1 or -1 to get +/-1 sigma shifts
  smearJets = True,
  shiftJER = 0, # set to +1 or -1 to get +/-1 sigma shifts
  cleanJetsFromFirstPhoton = False,
  cleanJetsFromTaus = False,
  cleanJetsFromIsoTracks = False,
  jecPath = ""
)



###################
### TAUANALYZER ###
###################
from PhysicsTools.Heppy.analyzers.objects.TauAnalyzer import TauAnalyzer
tauAnalyzer = cfg.Analyzer(
  # Cloned default values for practical purposes...
  # If changed, please leave the default in a comment
  class_object = TauAnalyzer,

  #####################
  ### Tau - General ###
  #####################
  ptMin = 20.,
  etaMax = 9999.,
  dxyMax = 1000.,
  dzMax = 0.2,
  vetoLeptons = True,
  leptonVetoDR = 0.4,
  decayModeID = "decayModeFindingNewDMs", # ignored if not set or ""
  tauID = "byLooseCombinedIsolationDeltaBetaCorr3Hits",
  vetoLeptonsPOG = False, # If True, the following two IDs are required
  tauAntiMuonID = "againstMuonLoose3",
  tauAntiElectronID = "againstElectronLooseMVA5",
  tauLooseID = "decayModeFinding",
)



######################
### PHOTONANALYZER ###
######################
from PhysicsTools.Heppy.analyzers.objects.PhotonAnalyzer import PhotonAnalyzer
photonAnalyzer = cfg.Analyzer(
  # Cloned default values for practical purposes...
  # If changed, please leave the default in a comment
  class_object = PhotonAnalyzer,

  ########################
  ### Photon - General ###
  ########################
  photons = 'slimmedPhotons',

  ptMin = 20,
  etaMax = 2.5,
  gammaID = "PhotonCutBasedIDLoose",
  do_mc_match = True,
)



###################
### METANALYZER ###
###################
from PhysicsTools.Heppy.analyzers.objects.METAnalyzer import METAnalyzer
METAnalyzer = METAnalyzer.defaultConfig



#######################
### HMuMu ANALYZERS ###
#######################

### GLOBAL CUTS
met_pt_cut = 100. # met or fakemet
jet_met_deltaphi_cut = 0. # wrt met or fakemet

from HMuMuPD.Heppy.analyzers.PreselectionAnalyzer import PreselectionAnalyzer
PreselectionAnalyzer = cfg.Analyzer(
  # Here it is the place to put all thresholds etc.
  # to be used in the preselection
  verbose = False,
  class_object = PreselectionAnalyzer,

  jet1_bTag = -99.,
  jet2_bTag = -99.,
)

### GLOBAL INFORMATION TO BE STORED
### AT THE TOP OF THE NTUPLE
globalVariables = [
  #NTupleVariable("isSR", lambda x: x.isSR, int, help="Signal Region flag"),
  #NTupleVariable("isZCR", lambda x: x.isZCR, int, help="Z+jets Control Region flag"),
  #NTupleVariable("isWCR", lambda x: x.isWCR, int, help="W+jets Control Region flag"),
  #NTupleVariable("isGCR", lambda x: x.isGCR, int, help="Gamma+jets Control Region flag"),
  #NTupleVariable("Cat", lambda x: x.Category, int, help="Signal Region Category 1/2/3"),
  #NTupleVariable("nMuons", lambda x: len(x.selectedMuons), int, help="Number of selected muons"),
  #NTupleVariable("nElectrons", lambda x: len(x.selectedElectrons), int, help="Number of selected electrons"),
  #NTupleVariable("nTaus", lambda x: len(x.selectedTaus), int, help="Number of selected taus"),
  #NTupleVariable("nPhoton", lambda x: len(x.selectedPhotons), int, help="Number of selected photons"),
  NTupleVariable("nJets", lambda x: len(x.cleanJets), int, help="Number of cleaned jets"),
]



##############################
### SIGNAL REGION TREE ###
##############################
TreeProducer = cfg.Analyzer(
  class_object = AutoFillTreeProducer,
  name='TreeProducer',
  treename='Events',
  #filter = lambda x: x.isSR,
  verbose = False,
  vectorTree = True,
  globalVariables = globalVariables,
  globalObjects = {
    "met" : NTupleObject("met", metType, help="PF E_{T}^{miss}, after default type 1 corrections"),
  },
  collections = {
    "selectedMuons" : NTupleCollection("muons", muonType, 3, help="Muons after the preselection"),
    "selectedElectrons" : NTupleCollection("electrons", electronType, 3, help="Electrons after the preselection"),
    "selectedTaus" : NTupleCollection("taus", tauType, 3, help="Taus after the preselection"),
    #"selectedPhotons" : NTupleCollection("photons", photonType, 3, help="Photons after the preselection"),
    "cleanJets" : NTupleCollection("jets", jetType, 4, help="Jets after the preselection"),
  }
)



##########################
### SEQUENCE TO BE RUN ###
##########################
sequence = [
  #Object selection first
  triggerAnalyzer,
  pileupAnalyzer,
  vertexAnalyzer,
  leptonAnalyzer,
  jetAnalyzer,
  tauAnalyzer,
  photonAnalyzer,
  METAnalyzer,

  # Preselection
  PreselectionAnalyzer,

  # Analysis-like selection
  # e.g. signal vs. control region etc.

  # Fill the trees
  TreeProducer,
]

####################
### TFILESERVICE ###
####################
from PhysicsTools.HeppyCore.framework.services.tfile import TFileService
output_service = cfg.Service(
  TFileService,
  'outputfile',
  name="outputfile",
  fname='tree.root',
  option='recreate'
)

##############################
### INPUT ###
##############################
from PhysicsTools.Heppy.utils.miniAodFiles import miniAodFiles
#from DMPD.Heppy.samples.Phys14.fileLists import samples

sampleTest = cfg.Component(
  files = ["file:/lustre/cmswork/zucchett/CMSSW_7_2_0_patch1/src/MINIAODSIM.root"],
  name="Test",
  isMC=True,
  isEmbed=False,
  splitFactor=1
)

##############
### FWLITE ###
##############
from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
preprocessor = CmsswPreprocessor("tagFatJets.py")

from PhysicsTools.HeppyCore.framework.eventsfwlite import Events

""" Define filelist for local test
"""
selectedComponents = [sampleTest]

""" Put everything together
"""
config = cfg.Config(
  components = selectedComponents,
  sequence = sequence,
  services = [output_service],
  #preprocessor = preprocessor,
  events_class = Events
)

##############
### LOOPER ###
##############
if __name__ == '__main__':
  """ This allows to run as a python executable
      i.e. >$ python thisFile.py
  """
  from PhysicsTools.HeppyCore.framework.looper import Looper
  looper = Looper(
    'ttHmumu',
    config,
    nPrint = 0,
    nEvents=1000,
  )
  looper.loop()
  looper.write()


