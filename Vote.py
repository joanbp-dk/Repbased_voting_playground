import Definitions
import Testdata

CANDIDATES = Definitions.CANDIDATES

# A quick and dirty voting algorithm.
# Counts all votes and returns the id of the candidate who got the most votes.
# In case of a tie, the winning candidate with the lowest id will be returned.
# This algorithm completely ignores the proven qualifications of both candidates and voters.
def popularity_contest(sample):

    votecount = {}
    for k in CANDIDATES.keys():
        votecount[k] = len([voter for voter in sample if voter.vote is CANDIDATES[k]])
    
    return max(votecount, key = votecount.get)


# Run the test
voters = Testdata.getSample()   # Returns a list of voters, with votes and proven qualifications
winner = popularity_contest(voters)           # Run the voting algorithm
print(winner)                   # Print the id of the winner

