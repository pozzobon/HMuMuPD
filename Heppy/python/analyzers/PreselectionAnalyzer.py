# -*- coding: utf-8 -*-
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.utils.deltar import deltaR2, deltaPhi
import math
import ROOT
import sys

class PreselectionAnalyzer( Analyzer ):
  """ Preselect the events
  """

  def beginLoop( self, setup ) :
    """ Prepare tactical counters
    """
    super( PreselectionAnalyzer, self ).beginLoop( setup )
    if "outputfile" in setup.services:
      setup.services["outputfile"].file.cd()
      self.inputCounter = ROOT.TH1F( "Counter", "Counter", 20, 0, 20 )
      self.inputCounter.GetXaxis().SetBinLabel( 1, "All events" )
      self.inputCounter.GetXaxis().SetBinLabel( 2, "Trigger" )
      """ Room for extra steps to monitor the efficiency
	  of each selection step
      """

  def selectDiMuon( self, event ) :
    """ Two muons in the event
    """
    if not len( event.selectedMuons ) >= 2 :
      return False

    """ Default if passing selection
	with optional assignment of chosen object
	to the event as itself
    """
    #event.Muon1 = event.selectedMuons[0]
    #event.Muon2 = event.selectedMuons[1]
    return True

  def selectTwoBJets( self, event ) :
    """ Two b-jets to tag the ttbar pair
    """
    if not len( event.cleanJets ) >= 2 :
      return False

    if not event.cleanJets[0].btag('combinedInclusiveSecondaryVertexV2BJetTags') > self.cfg_ana.jet1_bTag :
      return False

    if not event.cleanJets[1].btag('combinedInclusiveSecondaryVertexV2BJetTags') > self.cfg_ana.jet2_bTag :
      return False

    """ Default if passing selection
	with optional assignment of chosen object
	to the event as itself
    """
    event.Jet1 = event.cleanJets[0]
    event.Jet2 = event.cleanJets[1]
    return True

  def process( self, event ) :
    """ What this filter does
    """

    event.Category = 0
    event.Jet1 = None
    event.Jet2 = None

    # All events
    self.inputCounter.Fill(0)

    # Trigger
    self.inputCounter.Fill(1)

    # DiMuon
    if self.selectDiMuon( event ) :
      # do something
      print("ok")
    else :
      return False

    # Check if there is at least one jet
    if len( event.cleanJets ) < 1:
      return False

    # Two b-Jets
    if self.selectTwoBJets( event ) :
      # do something
      print("ok")
    else :
      return False

    """ Default if passing selection
    """
    return True

