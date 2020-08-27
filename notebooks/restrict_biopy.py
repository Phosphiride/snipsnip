# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 19:22:19 2020

@author: yujia
"""

import Bio
from Bio import Restriction
from Bio.Seq import Seq

class BioRestrict:
    
    def convert_IUPAC(input_seq):
        in_IUPAC = Seq(input_seq, alphabet = Bio.Alphabet.IUPAC.unambiguous_dna)
        return in_IUPAC
    
    def restrict_function(in_IUPAC):
        rb = Restriction.RestrictionBatch([], ["C", "B", "E", "I", "K", "J", "M", "O", "N", "Q", "S", "R", "V", "Y", "X"])
        
        return
