from Definitions import *

voters_1 = {

    "V1": {},
    "V2": {NFT.FELLOWSHIP_COMM: True, 
           NFT.FUNDA_1_v1: True, 
           NFT.FUNDA_2_v2: True, 
           NFT.FUNDA_3_v1: True, 
           NFT.FUNDA_4_v1: True, 
           NFT.FUNDA_4_v2: True, 
           NFT.FUNDA_5_v1: True},
    "V3": {},
    "V4": {NFT.FUNDA_1_v2: True},
    "V5": {NFT.FUNDA_1_v2: True, 
           NFT.FUNDA_2_v2: True},
    "V6": {NFT.ETHCC_SPEAKER_1: True},
    "V7": {NFT.STUDY_SEASON_REGISTRATION: True, 
           NFT.LIVE_TRACK_4: True},
    "V8": {NFT.STUDY_SEASON_REGISTRATION: True},
    "V9": {NFT.STUDY_SEASON_REGISTRATION: True, 
           NFT.LIVE_TRACK_1: True, 
           NFT.LIVE_TRACK_2: True},
    "V10": {NFT.LIVE_TRACK_4: True, 
            NFT.LIVE_TRACK_5: True},
}

voter_choices_1 = {
    
    "V1": "C4",
    "V2": "C2",
    "V3": "C2",
    "V4": "C3",
    "V5": "C4",
    "V6": "C3",
    "V7": "C1",
    "V8": "C4",
    "V9": "C2",
    "V10": "C4",
}

def getSample(sampleID = 1):

    if sampleID != 1:
        raise Exception("Only one sample available at this point. Use default sampleID = 1.")
    
    return (voters_1, voter_choices_1)


