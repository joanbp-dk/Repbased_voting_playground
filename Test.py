from Definitions import NFT
from GroupHug import GroupHug

sample_voters = {"voter_1":  {NFT.FELLOWSHIP_COMM: True}, 
                 "voter_2":  {NFT.FUNDA_1_v1: True},
                 "voter_3":  {NFT.FUNDA_1_v1: True, NFT.FUNDA_2_v1: True},
                 "voter_4":  {NFT.LIVE_TRACK_4: True}
                 }

sample_choices = {"voter_1": "candidate_A",
                  "voter_2": "candidate_A",
                  "voter_3": "candidate_B",
                  "voter_4": "candidate_B"}

mechanism = GroupHug()

winner, candidate_scores = mechanism.calculate(sample_voters, sample_choices)

print(f"The winner is {winner}.")

print(f"Results can be seen here: {candidate_scores}.")

