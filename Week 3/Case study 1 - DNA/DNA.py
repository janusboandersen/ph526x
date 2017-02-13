#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:02:34 2017

@author: janusboandersen
"""

#inputfile = "dna.txt"
#f = open(inputfile, "r")
#seq = f.read()

inputfile = "dna.txt"


def read_seq(inputfile, cds_start=0, cds_stop=0, mod_crop=1):
    """
    Reads and returns the input sequence with special characters removed.
    Arguments:
        cds_start=integer: the CDS range starting position
        cds_stop=integer: the CDS range stopping position
        mod_crop=integer: crops the length of the sequence to fit codons as multiples of the specified length.
            Cropping occurs before extraction of CDS sequence.
    """
    
    with open(inputfile, "r") as f:
        seq = f.read()

    #remove newline (n) and carriage return (r)
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")

    #Remove any last hanging characters
    crop = len(seq) % mod_crop
    seq = seq[0:len(seq)-crop]
    
    #Extract the CDS sequence
    if cds_start > 0 and cds_stop > cds_start:
        #convert to 0-indexed
        cds_start -= 1
        #cds_stop stays the same -1 for zero-index, +1 to ensure the last char is included.
        
        #extract the sequence
        seq = seq[cds_start:cds_stop]
    
    #Return the sequence
    return seq;
        
    
    
def translate(seq):
    """
    Translate a string containing a nucleotide sequence 
    into a string containing the corresponding sequence 
    of amino acids . Nucleotides are translated in triplets 
    using the table dictionary; each amino acid 4 is encoded 
    with a string of length 1. 
    """
    
    #translation table of codons to amino acids
    # _ underscores are nature's stop codons.
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    #The protein is a sequence of amino acids
    protein = ""
        
    # Check that the length of the string is divisible by 3
    if len(seq) % 3 == 0:
        # Valid sequence - proceed
        # Loop over the sequence
        for i in range(0, len(seq), 3):
    
            # Extract a single codon (3-letter string)
            codon = seq[i:i+3]
    
            # Look up each codon (3-letter string) and store the result
            # Concatenating to generate an amino acid sequence
            protein += table[codon]
    else:
        pass
    

    return protein;
    
#### end of function translate ####


NM207618_2 = read_seq(inputfile, cds_start=21, cds_stop=938)
translated_protein = translate(NM207618_2)

#remove the stop codon
if translated_protein[-1] == "_":
    NM207618_2 = NM207618_2[0:len(NM207618_2)-3]
    translated_protein = translate(NM207618_2)

#load comparison protein
prt = read_seq("protein.txt")    
    
print("Comparison of translated sequence and downloaded sequence: ", translated_protein == prt)

    
