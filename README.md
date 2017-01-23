## Natural Language Processing 
This repository contains all of my problem sets from NLP. Each folder contains the instructions for the assignment instructions and a write up that explains the solutions. Click the link for my python code for each problem set

* [Problem Set 1: Regular expressions and finite state automata](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset1/pset1_code.py)
  * In this problem set I build a FSA that accepts all dates in the form MM[/, - or blank ]DD[/, - or blank ]YYYY from 1900 to 2099
* [Problem Set 2: Language Modeling](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset2/pset2_code.py)
  * In this problem set I build a Bigram LM using the Brown Corpus. These estimates are calculated using MLE probabilities and are evaluated using perplexity. Moreover, I also use Simple Linear Interpolation as a smoothing method for my model
* [Problem Set 3: POS Tagging with Hidden Markov models](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset3/pset3_code.py)
  * In this problem set I build a Bigram HMM part-of-speech tagger. Part of speech taggers are particularly useful for word ambiguity i.e "I'll book a flight" vs "I read a book". I computed the percent of ambiguous words, implemented a Joint Probability method for computing the HMM
probability of a tagged sentence and the dynamic programming Viterbi method for POS tagging. Lastly, I computed the accuracy and compared it to my basline model
* [Problem Set 4:Statistical parsing](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset4/pset4_code.py)
  * In this problem set I build a Build a PCFG parser. For this assignment I use the Penn Treebank corpus to: find the most probable 10 productions for the NP nonterminal, implement the probabilistic CKY algorithm for parsing a test sentence using
my learned PCFG, bucket my test set sentences into the following 5 buckets and figured out how many sentences fall in each bucket and lastly for each bucket, I unbinarized and printed my predicted trees and gold standard
trees, one tree per line. (These gold and test files can be provided upon request).
