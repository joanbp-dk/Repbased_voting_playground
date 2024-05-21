# A playground for trying out voting algorithms

**Last updated** May 5, 2024

## Overview

This is my personal branch for experiments related to the TokenEngineering Academy's Reputation Weighted Voting course, the goal of which it is to come up with a suitable reputation based voting algorithm for electing a winner among four pre-selected fellowship candidates.

...But feel free to play around with the code on your own machine, and use it for any constructive purpose you can think of. 


## Files

* **[Concept.txt](Concept.txt)**

  Detailed explanation of the proposed voting concept.

* **[Voting.pdf](Voting.pdf)**

  A visual representation of the voting design.

* **[VotingMechanism.py](VotingMechanism.py)**

  Abstract class that represents a voting mechanism.
  By courtesy of @eightarmsninebrains / [basic-voting-calc](https://github.com/eightarmsninebrains/basic-voting-calc).

* **[GroupHug.py](GroupHug.py)**

  Implementation of the voting mechanism. This is where the action happens.

* **[Definitions.py](Definitions.py)**

  Basic structures used by the design.

* **[Testdata.py](Testdata.py)**

  A sample of votes to be used for testing the voting mechanism.


## How to use

Running *[GroupHug.py](GroupHug.py)* in a Python interpreter will cause it to fetch a sample of test votes, run the proposed voting algorithm on the data and announce a winner.
