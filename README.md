# A playground for trying out voting algorithms

**Last updated** May 5, 2024

## Overview

This is my personal branch for experiments related to the TokenEngineering Academy's Reputation Weighted Voting course, the goal of which it is to come up with a suitable reputation based voting algorithm for electing a winner among four pre-selected fellowship candidates.

...But feel free to play around with the code on your own machine, and use it for any constructive purpose you can think of. 

## Files

* **[Definitions.py](Definitions.py)**
  
  Class definitions for voters, candidates and NFTs that prove a voter's qualifications.
  The list of available NFTs is taken from [this presentation](https://docs.google.com/presentation/d/1fqsmqvMTWeL61E2OMZIbWVfufKEIKJCkYOp6sth6K_Q/edit#slide=id.g1ff3e012012_0_0).
  
  In future, certain accomplishments may also be attributed to each candidate. A basic structure for this is hinted at, but not yet fully built out in the code.

  The idea is that the final voting mechanism (yet to be designed) may use knowledge of voters' NFTs and candidates' accomplishments to find the most 'reputable' candidate.

* **[Testdata.py](Testdata.py)**

  A sample of votes to be used for testing the voting mechanism.
  In this context, a 'vote' is simply a voter who has a preferred candidate and a list of personal NFTs.

* **[Vote.py](Vote.py)**

  This is where the action happens.

* **[Concept.txt](Concept.txt)**

  This file explains my voting concept.

* **[Voting.pdf](Voting.pdf)**

  A visual representation of the voting design.


## How to use

Running *Vote.py* in a Python interpreter will cause it to fetch a sample of test votes, run my voting algorithm on the data and announce a winner.
