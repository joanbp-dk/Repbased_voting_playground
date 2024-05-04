from enum import Enum

class FellowshipCandidateEnum(Enum):

    C1 = 1,                             # Fellowship candidate 1
    C2 = 2,                             # Fellowship candidate 2
    C3 = 3,                             # Fellowship candidate 3
    C4 = 4,                             # Fellowship candidate 4

class AccomplishmentsEnum(Enum):

    FULFILLED_ALL_REQUIREMENTS = 1,     # More accomplishments could be defined and used by the voting algorithm...

class FellowshipCandidate:

    def __init__(self, id, accomplishments = []):

        if not id in iter(FellowshipCandidateEnum):
            raise Exception("Id must one of the IDs defined by the FellowshipCandidateEnum!")
        self.id = id

        # The candidate's proven accomplishments. Must refer to the Accomplishments enum. Ignore invalid accomplishments.
        self.accomplishments = [acc for acc in accomplishments if acc in iter(AccomplishmentsEnum)]

# The eligible candidates.
# For now, let's just assume that they all fulfill the requirements.
# In future, a list of a candidate's proven accomplishments could be used by a voting algorithm.
CANDIDATES = {
    "C1": FellowshipCandidate(FellowshipCandidateEnum.C1, [AccomplishmentsEnum.FULFILLED_ALL_REQUIREMENTS]),
    "C2": FellowshipCandidate(FellowshipCandidateEnum.C2, [AccomplishmentsEnum.FULFILLED_ALL_REQUIREMENTS]),
    "C3": FellowshipCandidate(FellowshipCandidateEnum.C3, [AccomplishmentsEnum.FULFILLED_ALL_REQUIREMENTS]),
    "C4": FellowshipCandidate(FellowshipCandidateEnum.C4, [AccomplishmentsEnum.FULFILLED_ALL_REQUIREMENTS]),
}

class Voter():

    def __init__(self, vote = None, nfts = [], hasTeaAccount = True, hasWalletConnected = True, isCandidate = False):

        # The candidate that the voter prefers. Must be a valid fellowship candidate.
        if vote is None or not isinstance(vote, FellowshipCandidate):
            raise Exception("Invalid vote!")        
        self.vote = vote

        # List of NFTs that this voter holds. Must refer to the NFT enum. Ignore invalid NFTs.
        self.nfts = [nft for nft in nfts if nft in iter(NFT)] 

        # Voter has an TEA account. Must be True to participate in voting.
        self.hasTeaAccount = hasTeaAccount

        # Voter has connected their wallet. Must be true to participate in voting.
        self.hasWalletConnected = hasWalletConnected

        # Candidates are not allowed to vote (?)
        self.isCandidate = isCandidate
        

class NFT(Enum):

    FUNDA_1 = 1                         # TE Fundamentals module 1
    FUNDA_2 = 2                         # TE Fundamentals module 2
    FUNDA_3 = 3                         # TE Fundamentals module 3
    FUNDA_4 = 4                         # TE Fundamentals module 4
    FUNDA_5 = 5                         # TE Fundamentals module 5
    FUNDA_LEGACY = 6                    # TE Fundamentals legacy NFT
    FELLOWSHIP_COMM = 7,                # Fellowship Committee member
    STUDY_SEASON_SPEAKER = 8,           # Study Season speaker
    ETHCC_TE_2023_BARCAMP_SPEAKER = 9,  # Speaker at EthCC TE 2023/Barcamp
    STUDY_SEASON_REGISTRATION = 10,     # Registered to Study Season
    WONDERVERSE_TOP50 = 11,             # Made it into top 50 on the Wonderverse leaderboard
    LIVE_TRACK_1 = 12,                  # Participated in Study Season live track 1
    LIVE_TRACK_2 = 13,                  # Participated in Study Season live track 2
    LIVE_TRACK_3 = 14,                  # Participated in Study Season live track 3
    LIVE_TRACK_4 = 15,                  # Participated in Study Season live track 4
    LIVE_TRACK_5 = 16,                  # Participated in Study Season live track 5 (Offered by candidate)
    LIVE_TRACK_6 = 17,                  # Participated in Study Season live track 6 (Offered by candidate)
    LIVE_TRACK_7 = 18,                  # Participated in Study Season live track 7 (Offered by candidate)
    LIVE_TRACK_8 = 19,                  # Participated in Study Season live track 8 (Offered by candidate)

