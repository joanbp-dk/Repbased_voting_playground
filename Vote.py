import Testdata
from Definitions import *

CANDIDATES = Testdata.CANDIDATES

EXPERTS_WEIGHT = 1
INTELLECTUALS_WEIGHT = 1
PARTICIPANTS_WEIGHT = 1
COMMUNITY_WEIGHT = 1

# The experts are highly qualified peers.
# They are fellowship committee members, ETHCC TE 2023 / Barcamp speakers, or TE Study Season speakers.
# They follow a principle of one person, one vote.
def ask_the_experts(sample):

    experts = set()
    for voter in sample:
        for nft in voter.nfts:
            if nft in [NFT.FELLOWSHIP_COMM, NFT.ETHCC_TE_2023_BARCAMP_SPEAKER, NFT.STUDY_SEASON_SPEAKER]:
                experts.add(voter)
    
    return ask_the_community(experts)

# The intellectuals are students who hold one or more TE Fundamentals NFT.
# The weight assigned to each vote is proportional to the number of TE Fundamentals NFTs the voter holds.
def ask_the_intellectuals(sample):
    
    cpoints = {c: 0 for c in CANDIDATES}

    for voter in sample:
        weight = 0
        for nft in voter.nfts:
            if nft in [NFT.FUNDA_1, NFT.FUNDA_2, NFT.FUNDA_3, NFT.FUNDA_4, NFT.FUNDA_5, NFT.FUNDA_LEGACY]:
                weight += 1
        cpoints[voter.vote.id] += weight

    return cpoints

# The active participants are students who have gained knowledge and experience during TE Study Season 2024.
# The weight assigned to each vote depends on the Study Season NFTs of the voter:
# Each NFT from live track 1-4 (not lead by a candidate) counts for 1.
# Each NFT from live track 5-8 (lead by a candidate) counts for 3.
# A Wonderverse top 50 NFT counts for 1.
def ask_the_active_participants(sample):

    cpoints = {c: 0 for c in CANDIDATES}

    for voter in sample:
        weight = 0
        for nft in voter.nfts:
            if nft in [NFT.LIVE_TRACK_1, NFT.LIVE_TRACK_2, NFT.LIVE_TRACK_3, NFT.LIVE_TRACK_4]:
                weight += 1
            elif nft in [NFT.LIVE_TRACK_5, NFT.LIVE_TRACK_6, NFT.LIVE_TRACK_7, NFT.LIVE_TRACK_8]:
                weight += 5
            elif nft is NFT.WONDERVERSE_TOP50:
                weight += 1
        cpoints[voter.vote.id] += weight

    return cpoints

# The community is a large and very diverse group of people.
# All voters are treated equally: One person > one vote. No weights are applied.
def ask_the_community(sample):

    votecount = {}
    for k in CANDIDATES.keys():
        votecount[k] = len([voter for voter in sample if voter.vote == CANDIDATES[k]])
    
    return votecount

def vote(sample):

    experts = normalize(ask_the_experts(sample))
    intellectuals = normalize(ask_the_intellectuals(sample))
    participants = normalize(ask_the_active_participants(sample))
    community = normalize(ask_the_community(sample))

    print("\nExperts: " + str(experts))
    print("Intellectuals: " + str(intellectuals))
    print("Participants: " + str(participants))
    print("Community: " + str(community))
    print ("\n---\n")

    aggregate = {c: 0 for c in CANDIDATES}

    for c in experts:
        aggregate[c] += (experts[c]*EXPERTS_WEIGHT)

    for c in intellectuals:
        aggregate[c] += (intellectuals[c]*INTELLECTUALS_WEIGHT)

    for c in participants:
        aggregate[c] += (participants[c]*PARTICIPANTS_WEIGHT)

    for c in community:
        aggregate[c] += (community[c]*COMMUNITY_WEIGHT)

    return normalize(aggregate)


# Converts a set of points into percentages to allow aggregation across several sets of points.
def normalize(points):

    total = sum(points.values())
    return {c: round(100 * points[c] / total) for c in points}

# NB: IN CASE OF A TIE THIS FUNCTION RETURNS THE CANDIDATE IT ENCOUNTERS FIRST IN THE INPUT!
def declare_winner(points):
    return max(points, key = points.get)

# Run the test
voters = Testdata.getSample()
aggregate_vote = vote(voters)

print(aggregate_vote)

winner = declare_winner(aggregate_vote)
print("\nAnd the winner is: " + str(winner))
