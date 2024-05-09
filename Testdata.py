import copy
from Definitions import *

# The eligible candidates.
# For now, let's just assume that they all fulfill the requirements.
# In future, a list of a candidate's proven accomplishments could be used by a voting algorithm.
CANDIDATES = {
    "C1": FellowshipCandidate("C1", [Accomplishments.FULFILLED_ALL_REQUIREMENTS]),
    "C2": FellowshipCandidate("C2", [Accomplishments.FULFILLED_ALL_REQUIREMENTS]),
    "C3": FellowshipCandidate("C3", [Accomplishments.FULFILLED_ALL_REQUIREMENTS]),
    "C4": FellowshipCandidate("C4", [Accomplishments.FULFILLED_ALL_REQUIREMENTS]),
}

# Sample voter data.
# Each voter has voted for a specific candidate. Different voters have different proven qualifications.
# One voter in the sample is a fellowship candidate. Should they be allowed to vote?
voter_sample_1 = [
    Voter(CANDIDATES["C4"], []),
    Voter(CANDIDATES["C2"], [NFT.FELLOWSHIP_COMM, NFT.FUNDA_1, NFT.FUNDA_2, NFT.FUNDA_3, NFT.FUNDA_4, NFT.FUNDA_4, NFT.FUNDA_5, NFT.FUNDA_LEGACY]),
    Voter(CANDIDATES["C2"], [], isCandidate = True),
    Voter(CANDIDATES["C3"], [NFT.FUNDA_1]),
    Voter(CANDIDATES["C4"], [NFT.FUNDA_1, NFT.FUNDA_2]),
    Voter(CANDIDATES["C3"], [NFT.ETHCC_TE_2023_BARCAMP_SPEAKER]),
    Voter(CANDIDATES["C1"], [NFT.STUDY_SEASON_REGISTRATION, NFT.LIVE_TRACK_4, NFT.WONDERVERSE_TOP50]),
    Voter(CANDIDATES["C4"], [NFT.STUDY_SEASON_REGISTRATION]),
    Voter(CANDIDATES["C2"], [NFT.STUDY_SEASON_REGISTRATION, NFT.LIVE_TRACK_1, NFT.LIVE_TRACK_2]),
    Voter(CANDIDATES["C4"], [NFT.LIVE_TRACK_4, NFT.LIVE_TRACK_5]),
]

def getSample(sampleID = 1):

    if sampleID != 1:
        raise Exception("Only one sample available at this point. Use default sampleID = 1.")
    
    return copy.deepcopy(voter_sample_1)


