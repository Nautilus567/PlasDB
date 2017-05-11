"""
PlasDB Plasmid Module:

This file includes the plasmid class and several functions to keep track of annotations ans insertions

"""
#import os   ##For further testing

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

class Plasmid:
    """
    Plasmid object class
    """
    def __init__(self, name, id, insert, resistance, sequence):

        self.name = name
        self.id = id
        self.insert = insert
        self.resistance = resistance
        if type(sequence) == Seq:
            self.sequence = sequence
        elif type(sequence) == str:
            self.sequence = Seq(sequence, generic_dna)
    def __repr__(self):
        return "Plasmid {0}".format(self.name)
    def __str__(self):
        if len(self.sequence) > 50:
            seq = self.sequence[:20] + "[...]" + self.sequence[-21:]
        else:
            seq = self.sequence
        return "Plasmid entry: \nName: {0} \nID: {1} \nInsert: {2} \nAntibiotic Resistance: {3} \nSequence: {4}\n ".format(self.name, self.id, self.insert, self.resistance, seq)
    def restriction_cuts(self, Enzimes):
        query = str(self.sequence)








#Test of working

Plas = Plasmid('Test Plasmid', 'pTest','NA' , 'Amp','ggggaattgtgagcggataacaattcccctctagaaataattttgtttaactttaagaaggagatataccatgggcagca')

print(Plas)

