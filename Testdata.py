import copy
from Definitions import *

# Sample voter data.
# Each voter has voted for a specific candidate. Different voters have different proven qualifications.
# One voter in the sample is a fellowship candidate. Should they be allowed to vote?
voter_sample_1 = [
    Voter(CANDIDATES["C1"], []),
    Voter(CANDIDATES["C1"], [NFT.FELLOWSHIP_COMM, NFT.FUNDA_1, NFT.FUNDA_2, NFT.FUNDA_3, NFT.FUNDA_4, NFT.FUNDA_4, NFT.FUNDA_5, NFT.FUNDA_LEGACY]),
    Voter(CANDIDATES["C2"], [], isCandidate = True),
    Voter(CANDIDATES["C3"], [NFT.FUNDA_1]),
    Voter(CANDIDATES["C4"], [NFT.FUNDA_1, NFT.FUNDA_2]),
    Voter(CANDIDATES["C3"], [NFT.ETHCC_TE_2023_BARCAMP_SPEAKER]),
    Voter(CANDIDATES["C1"], [NFT.STUDY_SEASON_REGISTRATION, NFT.LIVE_TRACK_4, NFT.WONDERVERSE_TOP50]),
    Voter(CANDIDATES["C4"], [NFT.STUDY_SEASON_REGISTRATION]),
    Voter(CANDIDATES["C2"], [NFT.STUDY_SEASON_REGISTRATION, NFT.LIVE_TRACK_1, NFT.LIVE_TRACK_2]),
    Voter(CANDIDATES["C4"], []),
]

def getSample(sampleID = 1):

    if sampleID != 1:
        raise Exception("Only one sample available at this point. Use default sampleID = 1.")
    
    return copy.deepcopy(voter_sample_1)


