# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:22:46 2015

@author: kbaumer
"""

from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

SAFECEN_STOP_WORDS = frozenset([
    "member", "svm", "mishap", "sailor"])

class SafecenStopWords():


    def __init__(self):
        self._english = ENGLISH_STOP_WORDS
        self._safecen = ENGLISH_STOP_WORDS.union(SAFECEN_STOP_WORDS)
        

    @property
    def english(self):
        return self._english
        
    @property
    def safecen(self):
        return self._safecen
        
    @property
    def three(self):
        return '3';