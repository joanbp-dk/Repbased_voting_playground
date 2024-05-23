# A playground for trying out voting algorithms

## Overview

This is a playground for experiments related to the TokenEngineering Academy's Reputation Weighted Voting course, the goal of which it is to come up with a suitable reputation based voting algorithm for electing a winner among four pre-selected fellowship candidates.

I'm currently using it to work on my own design proposal, the GroupHug voting mechanism.

...But feel free to play around with the code on your own machine, and use it for any constructive purpose you can think of.

## Files

* **[Concept.txt](Concept.txt)**

  Detailed explanation of the proposed voting concept.

* **[Voting.pdf](Voting.pdf)**

  A visual overview of the voting design.

* **[VotingMechanism.py](VotingMechanism.py)**

  Abstract class that represents a voting mechanism.
  By courtesy of @eightarmsninebrains / [basic-voting-calc](https://github.com/eightarmsninebrains/basic-voting-calc).

* **[GroupHug.py](GroupHug.py)**

  Implementation of the voting mechanism. This is where the actual action happens.

* **[Definitions.py](Definitions.py)**

  Basic structures used by the design.

* **[Testdata.py](Testdata.py)**

  A sample of votes to be used for testing the voting mechanism.

* **[Test.py](Test.py)**

  A small example test to show how to use the mechanism.

* **[Proofs.txt](Proofs.txt)**

  Arguments for the soundness of the design. More may be added when good questions come up.


## How to use

Running *[Test.py](Test.py)* in a Python interpreter will cause it to fetch a sample of test votes, run the GroupHug algorithm on the data and announce a winner.

