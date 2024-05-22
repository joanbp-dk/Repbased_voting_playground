# A playground for trying out voting algorithms

**Last updated** May 5, 2024

## Overview

This project is intended to be used as part of the TokenEngineering Academy's Reputation Weighted Voting course, 
the goal of which it is to come up with a suitable reputation based voting algorithm for electing a winner among four pre-selected fellowship candidates.

...But feel free to play around with the code on your own machine, and use it for any constructive purpose you can think of. 

In case you would like to come and see the specific voting design that I have been working on, you can find the most recent version in [this branch](https://github.com/joanbp-dk/Repbased_voting_playground/tree/Jbp_algorithms).


## Files

* **[VotingMechanism.py](VotingMechanism.py)**

  Abstract class that represents a voting mechanism. 
  By courtesy of @eightarmsninebrains / basic-voting-calc.

* **[PopularityContest.py](PopularityContest.py)**

  This is where the action happens.

  In this basic version, only one voting algorithm has been implemented:
  A quick-and-dirty popularity contest which ignores any notion of reputation.

* **[Definitions.py](Definitions.py)**
  
  Basic structures used by the design.

* **[Testdata.py](Testdata.py)**

  A sample of votes to be used for testing the voting mechanism.


## How to use

Running *Vote.py* in a Python interpreter will cause it to fetch a sample of test votes, perform a mock popularity contest and announce a winner.
