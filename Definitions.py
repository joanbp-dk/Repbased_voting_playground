class Voter:

    def __init__(self, vote = None, nfts = [], hasTeaAccount = True, hasWalletConnected = True, isCandidate = False):

        # The candidate that the voter prefers.
        self.vote = vote

        # List of NFTs that this voter holds.
        self.nfts = nfts 

        # Voter has an TEA account. Must be True to participate in voting.
        self.hasTeaAccount = hasTeaAccount

        # Voter has connected their wallet. Must be true to participate in voting.
        self.hasWalletConnected = hasWalletConnected

        # Candidates are not allowed to vote (?)
        self.isCandidate = isCandidate
        
class NFT:

    FUNDA_1_v1 = 'TE FUNDAMENTALS – MODULE 1 of 5 – VERSION 1 – 2022'          # TE Fundamentals module 1
    FUNDA_1_v2 = 'TE FUNDAMENTALS – MODULE 1 of 5 – VERSION 2 – 2023'          # TE Fundamentals module 1
    FUNDA_2_v1 = 'TE FUNDAMENTALS – MODULE 2 of 5 – VERSION 1 – 2022'          # TE Fundamentals module 2
    FUNDA_2_v2 = 'TE FUNDAMENTALS – MODULE 2 of 5 – VERSION 2 – 2023'          # TE Fundamentals module 2
    FUNDA_3_v1 = 'TE FUNDAMENTALS – MODULE 3 of 5 – VERSION 1 – 2022'          # TE Fundamentals module 3
    FUNDA_3_v2 = 'TE FUNDAMENTALS – MODULE 3 of 5 – VERSION 2 – 2023'          # TE Fundamentals module 3
    FUNDA_4_v1 = 'TE FUNDAMENTALS – MODULE 4 of 5 – VERSION 1 – 2022 '         # TE Fundamentals module 4
    FUNDA_4_v2 = 'TE FUNDAMENTALS – MODULE 4 of 5 – VERSION 2 – 2023'          # TE Fundamentals module 4
    FUNDA_5_v1 = 'TE FUNDAMENTALS – MODULE 5 of 5 – VERSION 1 – 2022'          # TE Fundamentals module 5
    FUNDA_5_v2 = 'TE FUNDAMENTALS – MODULE 5 of 5 – VERSION 2 – 2023'          # TE Fundamentals module 5
    NFT_BASED_REP = 'NFT-based Reputation in Web3 – V1 – 2023'                 # TE course on NFT based reputation
    STUDY_GROUP_HOST_1 = 'TE FUNDAMENTALS STUDY GROUP HOST 2022/2023'          # Study group host
    STUDY_GROUP_HOST_2 = 'TE FUNDAMENTALS STUDY GROUP HOST C2 2022/2023'       # Study group host, two cycles
    STUDY_GROUP_HOST_3 = 'TE360 STUDY GROUP HOST 2022'                         # Study group host
    FUNDA_COURSE_AUTHOR = 'TE FUNDAMENTALS COURSE AUTHOR – LAUNCH 2022'        # TE Fundamentals course author
    FUNDA_WE_MADE_IT = 'TE Fundamentals "We made it"'                          # People who made TEA / TE Fundamentals
    ETHCC_SPEAKER_1 = 'Token Engineering @EthCC Paris 2023 – Speaker'          # Speaker at EthCC
    ETHCC_SPEAKER_2 = 'Token Engineering @EthCC Paris 2024 - Speaker'          # Speaker at EthCC
    BARCAMP_SPEAKER = 'Token Engineering Barcamp - Speaker - Paris 2023\u2028' # Speaker at Barcamp
    BARCAMP_ATTENDEE = 'Token Engineering Barcamp - Paris 2023\u2028'          # Attendee at Barcamp
    BARCAMP_VOLUNTEER = 'Token Engineering Barcamp - Team - Paris 2023\u2028'  # Volunteer at Barcamp
    STUDY_SEASON_REGISTRATION = 'Study season registration'                    # Registered to Study Season
    LIVE_TRACK_1 = 'Live track 1'                                              # Participated in Study Season live track 1
    LIVE_TRACK_2 = 'Live track 2'                                              # Participated in Study Season live track 2
    LIVE_TRACK_3 = 'Live track 3'                                              # Participated in Study Season live track 3
    LIVE_TRACK_4 = 'Live track 4'                                              # Participated in Study Season live track 4
    LIVE_TRACK_5 = 'Live track 5'                                              # Participated in Study Season live track 5 (Offered by candidate)
    LIVE_TRACK_6 = 'Live track 6'                                              # Participated in Study Season live track 6 (Offered by candidate)
    LIVE_TRACK_7 = 'Live track 7'                                              # Participated in Study Season live track 7 (Offered by candidate)
    LIVE_TRACK_8 = 'Live track 8'                                              # Participated in Study Season live track 8 (Offered by candidate)
    FELLOWSHIP_COMM = 'Fellowship committee member'                            # Fellowship Committee member
    STUDY_SEASON_SPEAKER = 'Study season speaker'                              # Study Season speaker
    FELLOWSHIP_CANDIDATE = 'Fellowship candidate'                              # Fellowship candidate
    FELLOWSHIP_WINNER = 'Fellowship winner'                                    # Fellowship winner