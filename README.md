## Natural Language Processing 
This repository contains all of my problem sets from NLP

#### Problem Set 1: Regular expressions and finite state automata python file
In this problem set I build a FSA that accepts all dates in the form MM[/, - or blank ]DD[/, - or blank ]YYYY from 1900 to 2099
  
[python code for pset1](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset1/pset1_code.py)
 
[pdf explanation for pset 1](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset1/WriteUpSolution.pdf)
 
 ---
#### Problem Set 2: Language Modeling python file 
In this problem set I build a Bigram LM using the Brown Corpus. These estimates are calculated using MLE probabilities and are evaluated using perplexity. Moreover, I also use Simple Linear Interpolation as a smoothing method for my model
 
[python code for pset2](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset2/pset2_code.py)
 
[pdf explanation for pset 2](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset2/WriteUpSolution.pdf)
 
 ---
#### Problem Set 3: POS Tagging with Hidden Markov models python file
In this problem set I build a Bigram HMM part-of-speech tagger. Part of speech taggers are particularly useful for word ambiguity i.e "I'll book a flight" vs "I read a book". I computed the percent of ambiguous words, implemented a Joint Probability method for computing the HMM probability of a tagged sentence and the dynamic programming Viterbi method for POS tagging. Lastly, I computed the accuracy and compared it to my basline model

[python code for pset3](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset3/pset3_code.py)

[pdf explanation for pset 3 python file](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset3/WriteUpSolution.pdf)

---
#### Problem Set 4:Statistical parsing 
In this problem set I build a Build a PCFG parser. For this assignment I use the Penn Treebank corpus to: find the most probable 10 productions for the NP nonterminal, implement the probabilistic CKY algorithm for parsing a test sentence using my learned PCFG, bucket my test set sentences into the following 5 buckets and figured out how many sentences fall in each bucket and lastly for each bucket, I unbinarized and printed my predicted trees and gold standard trees, one tree per line. (These gold and test files can be provided upon request).

[python code for pset4](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset4/pset4_code.py)

[pdf explanation for pset4 python file](https://github.com/mmoya01/Natural-Language-Processing/blob/master/pset4/WriteUpSolution.pdf)
