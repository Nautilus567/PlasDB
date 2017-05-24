"""
PlasDB Plasmid Module:

This file includes the plasmid class and several functions to keep track of annotations ans insertions

"""
# import os   ##For further testing

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

# Dictionary of enzymatic restriction sites

enzimeDic = {'EcoR1': 'GAATTC',
             'Xhol': 'CTCGAG',
             'SmaI': 'CCCGGG'}


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
        else:
            raise TypeError

    def __repr__(self):
        return "Plasmid {0}".format(self.name)

    def __str__(self):
        if len(self.sequence) > 50:
            seq = self.sequence[:20] + "[...]" + self.sequence[-21:]
        else:
            seq = self.sequence
        return "Plasmid entry: \nName: {0} \nID: {1} \nInsert: {2} \nAntibiotic Resistance: {3} \nSequence: {4}\n ".format(
            self.name, self.id, self.insert, self.resistance, seq)

    def restriction_cuts(self, tryout):
        query = str(self.sequence)
        if type(tryout) == list:
            for i in tryout:
                if i != enzimeDic.keys():
                    raise ValueError('No restriction site template found for {0}'.format(i))
        elif type(tryout) == str:
            if tryout != enzimeDic.keys():
                raise ValueError('No restriction site template found')
        else:
            raise ValueError("Unable to understand what restriction site you ask for")
        query.upper()







        # if enz not in cut.keys():
        #     raise ValueError("I don't have the cut site of that enzime")
        # result = []
        # sector = ''
        # print("I'm going to use %s that has the following cut site: %s" % (enz, cut[enz]))
        # for i in range(len(seq)):
        #     j = i + len(cut[enz])
        #     if j > len(seq):
        #         break
        #     sector = seq[i:j]
        #     if sector == cut[enz]:
        #         result.append((i, j))
        # print("I found %s cut sites of the selected enzime" % (len(result)))
        # return result


# Test of working

Plas = Plasmid('Test Plasmid', 'pTest', 'NA', 'Amp',
               'ggggaattgtgagcggataacaattcccctctagaattcataattttgtttaactcgagttaagaaggagatatacccgggatgggcagca')

print(Plas)
