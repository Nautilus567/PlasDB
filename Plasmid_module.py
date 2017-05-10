"""
PlasDB Plasmid Module:

This file includes the plasmid class and several functions to keep track of annotations ans insertions

"""
#import os   ##For further testing

class Plasmid:
    def __init__(self, name, id, insert, resistance, sequence):
        self.name = name
        self.id = id
        self.insert = insert
        self.resistance = resistance
        self.sequence = sequence
    def __repr__(self):
        return "Plasmid {0}".format(self.name)
    def __str__(self):
        if len(self.sequence) > 50:
            seq = self.sequence[:20] + "[...]" + self.sequence[-21:]
        else:
            seq = self.sequence
        return "Plasmid entry: \nName: {0} \nID: {1} \nInsert: {2} \nAntibiotic Resistance: {3} \nSequence: {4}\n ".format(self.name, self.id, self.insert, self.resistance, seq)
    def restrictioncuts(self, Enzimes):
        pass






#Test of working

Plas = Plasmid('Test Plasmid', 'pTest','NA' , 'Amp','ggggaattgtgagcggataacaattcccctctagaaataattttgtttaactttaagaaggagatataccatgggcagca')

print(Plas)

