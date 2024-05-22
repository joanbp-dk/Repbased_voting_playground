"""GroupHug.py

Implements a group based calculation method, where each stakeholder group has 
a weight and rules by which points are distributed. 
"""

from Testdata import *
from Definitions import *

from typing import Any, Dict

from VotingMechanism import VotingMechanism


EXPERTS_WEIGHT = 1
INTELLECTUALS_WEIGHT = 1
PARTICIPANTS_WEIGHT = 1
COMMUNITY_WEIGHT = 1

class GroupHug(VotingMechanism):
    """
    A voting system class that implements a stakeholder group based voting mechanism.

    Attributes:
        voters (Dict[str, Dict[str, Any]]): A dictionary where each key is a voter ID and the value
            is a dictionary of (NFT ID, boolean) pairs.
        voter_choices (Dict[str, str]): A dictionary where each key is a voter ID and the value is
            the candidate chosen by that voter.
    """
    def calculate(self, voters: Dict[str, Dict[str, Any]], 
                  voter_choices: Dict[str, str]):
        """
        Implements the group hug voting mechanism.

        Parameters:
        - voters: A dictionary where each key is a voter ID and the value is a dictionary 
            of (NFT, boolean) pairs to signify if the voter holds this NFT. 
        - voter_choices: A dictionary where each key is a voter ID and the value is the chosen candidate.

        Returns:
        - str: The winning candidate.
        """

        # Extract and convert input to internal format
        extracted_candidates = set(voter_choices.values())
        extracted_voters = []
        for v in voters:
            choice = voter_choices[v]
            nfts = [nft for nft in voters[v] if voters[v][nft]]
            extracted_voters.append(Voter(choice, nfts))
        
        # Analyze election results
        aggregate_vote = self.vote(extracted_candidates, extracted_voters)
        winner = self.declare_winner(aggregate_vote)

        return (winner, aggregate_vote)


    # The experts are highly qualified peers.
    # They are fellowship committee members, TE Fundamentals course authors, 
    # or TE Study Season / ETHCC / Barcamp speakers.
    # They follow a principle of one person, one vote.
    def ask_the_experts(self, candidates, voters):

        def is_expert(voter):
            for nft in voter.nfts:
                if nft in [NFT.FELLOWSHIP_COMM, 
                        NFT.FUNDA_COURSE_AUTHOR,
                        NFT.STUDY_SEASON_SPEAKER, 
                        NFT.ETHCC_SPEAKER_1, NFT.ETHCC_SPEAKER_2,
                        NFT.BARCAMP_SPEAKER]:
                    return True

        experts = set([voter for voter in voters if is_expert(voter)])
                    
        return self.ask_the_community(candidates, experts)


    # The intellectuals are students who hold one or more NFTs as proof-of-knowledge,
    # either from TE Fundamentals, the NFT-based reputation course, or Barcamp.
    # Each passed TE Fundamentals module counts for 3.
    # Barcamp attendance counts for 2.
    # Having passed the exam of the NFT-based reputation course counts for 1.
    def ask_the_intellectuals(self, candidates, voters):

        def weight(voter):

            w = 0 
            nfts = voter.nfts
            if NFT.FUNDA_1_v1 in nfts or NFT.FUNDA_1_v2 in nfts: w += 3
            if NFT.FUNDA_2_v1 in nfts or NFT.FUNDA_2_v2 in nfts: w += 3
            if NFT.FUNDA_3_v1 in nfts or NFT.FUNDA_3_v2 in nfts: w += 3
            if NFT.FUNDA_4_v1 in nfts or NFT.FUNDA_4_v2 in nfts: w += 3
            if NFT.FUNDA_5_v1 in nfts or NFT.FUNDA_5_v2 in nfts: w += 3
            if NFT.BARCAMP_ATTENDEE in nfts: w += 2
            if NFT.NFT_BASED_REP in nfts: w += 1

            return w
        
        cpoints = {c: 0 for c in candidates}

        for voter in voters:
            cpoints[voter.vote] += weight(voter)

        return cpoints

    # The active participants are either students who have gained knowledge and experience 
    # during TE Study Season 2024, or study group hosts who have supported others in learning successfully,
    # or people who have helped in making TEA and TE Fundamentals a reality.
    # The weight assigned to each vote depends on the NFTs of the voter:
    # Each proof of contribution to making TEA/TEF a reality counts for 1.
    # Each study group host NFT counts for 1.
    # Each NFT from live track 1-4 (not lead by a candidate) counts for 1.
    # Each NFT from live track 5-8 (lead by a candidate) counts for 3.
    def ask_the_active_participants(self, candidates, voters):

        def weight(voter):

            w = 0
            for nft in voter.nfts:
                if nft in [NFT.FUNDA_WE_MADE_IT]:
                    w += 1
                elif nft in [NFT.STUDY_GROUP_HOST_1, NFT.STUDY_GROUP_HOST_2, NFT.STUDY_GROUP_HOST_3]:
                    w += 1
                elif nft in [NFT.LIVE_TRACK_1, NFT.LIVE_TRACK_2, NFT.LIVE_TRACK_3, NFT.LIVE_TRACK_4]:
                    w += 1
                elif nft in [NFT.LIVE_TRACK_5, NFT.LIVE_TRACK_6, NFT.LIVE_TRACK_7, NFT.LIVE_TRACK_8]:
                    w += 3

            return w

        cpoints = {c: 0 for c in candidates}

        for voter in voters:
            cpoints[voter.vote] += weight(voter)

        return cpoints

    # The community is a large and very diverse group of people.
    # All voters are treated equally: One person > one vote. No weights are applied.
    def ask_the_community(self, candidates, voters):

        votecount = {}
        for c in candidates:
            votecount[c] = len([voter for voter in voters if voter.vote == c])
        
        return votecount


    def vote(self, candidates, voters):

        # Converts a set of points into percentages to allow aggregation across several sets of points.
        def normalize(points):

            total = sum(points.values())

            if total == 0: return {c: 0 for c in points}
            else: return {c: round(100 * points[c] / total) for c in points}


        eligible = [v for v in voters if not v.isCandidate]   # Candidates are not allowed to vote!

        experts = normalize(self.ask_the_experts(candidates, eligible))
        intellectuals = normalize(self.ask_the_intellectuals(candidates, eligible))
        participants = normalize(self.ask_the_active_participants(candidates, eligible))
        community = normalize(self.ask_the_community(candidates, eligible))

        def str_dict(d):
            return str(dict(sorted(d.items())))

        print("\nExperts: " + str_dict(experts))
        print("Intellectuals: " + str_dict(intellectuals))
        print("Participants: " + str_dict(participants))
        print("Community: " + str_dict(community))
        print ("\n---\n")

        aggregate = {c: 0 for c in candidates}

        for c in experts:
            aggregate[c] += (experts[c]*EXPERTS_WEIGHT)

        for c in intellectuals:
            aggregate[c] += (intellectuals[c]*INTELLECTUALS_WEIGHT)

        for c in participants:
            aggregate[c] += (participants[c]*PARTICIPANTS_WEIGHT)

        for c in community:
            aggregate[c] += (community[c]*COMMUNITY_WEIGHT)

        result = normalize(aggregate)

        return result


    # NB: IN CASE OF A TIE THIS FUNCTION RETURNS THE CANDIDATE IT ENCOUNTERS FIRST IN THE INPUT!
    def declare_winner(self, points):
        return max(points, key = points.get)

