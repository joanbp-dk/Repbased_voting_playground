"""PopularityContest.py

Implements a basic popularity contest. 
"""

from Testdata import *
from Definitions import *

from typing import Any, Dict

from VotingMechanism import VotingMechanism


class PopularityContest(VotingMechanism):
    """
    A voting system class that implements a popularity contest.

    Attributes:
        voters (Dict[str, Dict[str, Any]]): A dictionary where each key is a voter ID and the value
            is a dictionary of (NFT ID, boolean) pairs.
        voter_choices (Dict[str, str]): A dictionary where each key is a voter ID and the value is
            the candidate chosen by that voter.
    """
    def calculate(self, voters: Dict[str, Dict[str, Any]], 
                  voter_choices: Dict[str, str]):
        """
        Implements the popularity contest voting mechanism.

        Parameters:
        - voters: A dictionary where each key is a voter ID and the value is a dictionary 
            of (NFT, boolean) pairs to signify if the voter holds this NFT. 
        - voter_choices: A dictionary where each key is a voter ID and the value is the chosen candidate.

        Returns:
        - str: The winning candidate.
        - dict: The result for each candidate.
        """

        # Extract and convert input to internal format
        extracted_candidates = set(voter_choices.values())
        extracted_voters = []
        for v in voters:
            choice = voter_choices[v]
            nfts = [nft for nft in voters[v] if voters[v][nft]]
            extracted_voters.append(Voter(choice, nfts))
        
        # Analyze election results
        votecount = self.popularity_contest(extracted_candidates, extracted_voters)
        winner = max(votecount, key = votecount.get)
        return (winner, votecount)


    # A quick and dirty voting algorithm.
    # Counts all votes and returns the id of the candidate who got the most votes.
    # In case of a tie, the winning candidate with the lowest id will be returned.
    # This algorithm completely ignores the proven qualifications of both candidates and voters.
    def popularity_contest(self, candidates, voters):

        votecount = {}
        for c in candidates:
            votecount[c] = len([voter for voter in voters if voter.vote == c])
        
        return votecount


# Run test

(voters, voter_choices) = getSample()
mechanism = PopularityContest()
(winner, votecount) = mechanism.calculate(voters, voter_choices)
print("\nAnd the winner is: " + str(winner))
print("\nDetailed result: " + str(votecount))
