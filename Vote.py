import Testdata
from Definitions import *

CANDIDATES = Testdata.CANDIDATES

# A quick and dirty voting algorithm.
# Counts all votes and returns the id of the candidate who got the most votes.
# In case of a tie, the winning candidate with the lowest id will be returned.
# This algorithm completely ignores the proven qualifications of both candidates and voters.
def popularity_contest(sample):

    votecount = {}
    for k in CANDIDATES.keys():
        votecount[k] = len([voter for voter in sample if voter.vote == CANDIDATES[k]])
    
    return votecount

def ask_the_dictator(sample):

    (dictator, dictator_points) = (None, 0)

    # Assign expertise points based on voters' NFTs and appoint the voter with most points as dictator
    for voter in sample:
        points = 0
        for nft in voter.nfts:
            if nft in [NFT.FELLOWSHIP_COMM]: points += 50
            elif nft in [NFT.ETHCC_TE_2023_BARCAMP_SPEAKER, NFT.STUDY_SEASON_SPEAKER]: points += 10
            elif nft in iter(NFT): points += 1

        if points > dictator_points:
            dictator = voter
            dictator_points = points

    cpoints = {c: 0 for c in CANDIDATES}
    cpoints[dictator.vote.id] = 100

    return cpoints

def ask_the_experts(sample):

    experts = set()
    for voter in sample:
        for nft in voter.nfts:
            if nft in [NFT.FELLOWSHIP_COMM, NFT.ETHCC_TE_2023_BARCAMP_SPEAKER, NFT.STUDY_SEASON_SPEAKER]:
                experts.add(voter)
    
    print(experts)
    
    return popularity_contest(experts)

def ask_the_theoreticians(sample):
    
    cpoints = {c: 0 for c in CANDIDATES}

    for voter in sample:
        weight = 0
        for nft in voter.nfts:
            if nft in [NFT.FELLOWSHIP_COMM, NFT.ETHCC_TE_2023_BARCAMP_SPEAKER, NFT.STUDY_SEASON_SPEAKER, 
                       NFT.FUNDA_1, NFT.FUNDA_2, NFT.FUNDA_3, NFT.FUNDA_4, NFT.FUNDA_5, NFT.FUNDA_LEGACY]:
                weight += 1
        cpoints[voter.vote.id] += weight

    return cpoints

def ask_the_participants(sample):

    cpoints = {c: 0 for c in CANDIDATES}

    for voter in sample:
        weight = 0
        for nft in voter.nfts:
            if nft in [NFT.LIVE_TRACK_1, NFT.LIVE_TRACK_2, NFT.LIVE_TRACK_3, NFT.LIVE_TRACK_4]:
                weight += 1
            elif nft in [NFT.LIVE_TRACK_5, NFT.LIVE_TRACK_6, NFT.LIVE_TRACK_7, NFT.LIVE_TRACK_8]:
                weight += 5
        cpoints[voter.vote.id] += weight

    return cpoints

def points_to_percentages(cpoints):

    total = sum(cpoints.values())
    return {c: round(100 * cpoints[c] / total) for c in cpoints}


# Run the test
votes = Testdata.getSample()            # Fetch the list of votes - ie. voters with preferred candidates and personal qualifications

dictator = points_to_percentages(ask_the_dictator(votes))
experts = points_to_percentages(ask_the_experts(votes))
theos = points_to_percentages(ask_the_theoreticians(votes))
participants = points_to_percentages(ask_the_participants(votes))
pop = points_to_percentages(popularity_contest(votes))

print("Dictator: " + str(dictator))
print("Experts: " + str(experts))
print("Theoreticians: " + str(theos))
print("Participants: " + str(participants))
print("---")
print("Everyone (popularity contest): " + str(pop))

