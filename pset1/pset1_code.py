# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:42:09 2016

@author: My
"""

from collections import defaultdict

class fsa():

    def __init__(self, states, alphabet, transitions, start, accepts):

        assert start in states, \
                'Start state must be a valid state.'
        assert set(accepts).issubset(set(states)), \
                'Accept states must be a subset of states.'
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.accepts = accepts
        self.constituent = []

    def test(self, word):

        if(len(self.constituent)==0):
            current_state = self.start
            for symbol in word:
                # assert symbol in self.alphabet, \
                #         'Symbol "%s" must be in alphabet.' % symbol
                if(symbol not in self.alphabet): return False

                for i in self.transitions[current_state]:
                    if(symbol in i[0]):
                        current_state = i[1]
                        break
                assert current_state in self.states, \
                        'Current state must be a valid state.'
            return current_state in self.accepts

        else:
            for i in range(len(word)+1):
                if(self.constituent[0].test(word[0:i]) == True and self.constituent[1].test(word[i:len(word)]) == True):
                    return True
            return False


def NDRecognize(input, fsa):
    """ TODO: Implement ND-RECOGNIZE from SLP Figure 2.19, return true or false based on
    whether or not the nondeterministic fsa object accepts or rejects the input string.
    """
    return fsa.test(input)

def Concatenate(fsa1, fsa2):
    """ TODO: Implement Concatenate so that if w1 is a string that fsa1 accepts and w2 is
    a string that fsa2 accepts this function should return an fsa that accepts w1w2.
    """
    fsa3 = fsa(fsa1.states,fsa1.alphabet,fsa1.transitions,fsa1.start,fsa1.accepts)
    fsa3.constituent.append(fsa1)
    fsa3.constituent.append(fsa2)
    return fsa3



""" Below are some test cases. Include the output of this in your write-up and provide
explanations.
['0':[]
"""

def TestComponents(months, days, years, seps):
	print "\nTest Months FSA"
	for input in ["", "0", "1", "9", "10", "11", "12", "13"]:
		print "'%s'\t%s" %(input, NDRecognize(input, months))
	print "\nTest Days FSA"
	for input in ["", "0", "1", "9", "10", "11", "21", "31", "32"]:
		print "'%s'\t%s" %(input, NDRecognize(input, days))
	print "\nTest Years FSA"
	for input in ["", "1899", "1900", "1901", "1999", "2000", "2001", "2099", "2100"]:
		print "'%s'\t%s" %(input, NDRecognize(input, years))
	print "\nTest Separators FSA"
	for input in ["", ",", " ", "-", "/", "//", ":"]:
		print "'%s'\t%s" %(input, NDRecognize(input, seps))

def TestDates(dates):
	print "\nTest Date Expressions FSA"
	for input in ["", "12 31 2000", "12/31/2000", "12-31-2000", "12:31:2000",
				  "1 2 2000", "1/2/2000", "1-2-2000", "1:2:2000",
				  "00-31-2000", "12-00-2000", "12-31-0000",
				  "12-32-1987", "13-31-1987", "12-31-2150"]:
		print "'%s'\t%s" %(input, NDRecognize(input, dates))

day_states = list('01234')
day_alphabet = list('0123456789')
day_transitions = {'0':[ [list('0'),'1'], [list('3'),'2'], [list('456789'),'4'], [list('12'),'3'] ],'1':[[list('123456789'),'4']],'2':[ [list('1'),'4'] ],'3': [[list('1234567890'),'4']]}
day_start = '0'
day_accepts = list('34')

days = fsa(day_states,day_alphabet,day_transitions,day_start,day_accepts)

separator_states = list('012')
separator_alphabet = list('/- ')
separator_transitions = {'0':[ [list('/- '),'1']],'1':[ [list('/- '),'2']]}
separator_start = '0'
separator_accepts = list('1')

seps = fsa(separator_states,separator_alphabet,separator_transitions,separator_start,separator_accepts)

month_states = list('01234')
month_alphabet = list('0123456789')
months_transitions = {'0':[ [list('0'),'1'], [list('1'),'3'], [list('23456789'),'2']],'1':[[list('123456789'),'2']],'3':[ [list('012'),'2'],[list('3456789'),'4']]}
months_start = '0'
months_accepts = list('32')

months = fsa(month_states,month_alphabet,months_transitions,months_start,months_accepts)

year_states = list('012346')
year_alphabet = list('0123456789')
year_transitions = {'0':[[list('1'),'1'], [list('2'),'4']], '1':[[list('9'),'2']], '2':[[list('0123456789'),'3']], \
                    '3':[[list('0123456789'),'6']], '4':[[list('0'),'2']] }
year_start = '0'
year_accept = list('6')

years = fsa(year_states,year_alphabet,year_transitions,year_start,year_accept)
TestComponents(months, days, years, seps)

dates = Concatenate(Concatenate(Concatenate(Concatenate(months,seps),days),seps),years)
TestDates(dates)