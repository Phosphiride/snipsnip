# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:16:11 2020

@author: yujia
"""

import pandas as pd
import Bio
from Bio.Seq import Seq
from Bio import SeqUtils
import re
import lark as lk

class Restriction:
    
    data = pd.read_csv("C:\\Users\\yujia\\projects\\snipsnip\\data_files\\restrict_data_2.csv", sep=";")
    
    def convert_IUPAC():
        rec_seq_all = Restriction.data["recognition sequence"]
        abc_list = []
        for rec_seq in rec_seq_all:
            temp_seq = Seq(rec_seq, alphabet = Bio.Alphabet.IUPAC.ambiguous_dna)
            abc_list.append(temp_seq)
        Restriction.data["IUPAC sequence"] = abc_list
        return 

    def find_enzyme(input_seq):
        in_IUPAC = Seq(input_seq, alphabet = Bio.Alphabet.IUPAC.unambiguous_dna)
        for rec_seq in Restriction.data["IUPAC sequence"]:
            SeqUtils.nt_search(in_IUPAC, rec_seq)
        return

def main(input_seq):
    Restriction.convert_IUPAC()
    Restriction.find_enzyme(input_seq)
    return

main("AAAAATATGGGGCCGCTATACGCCAAA")