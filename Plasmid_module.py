"""
PlasDB Plasmid Module:

This file includes the plasmid class and several functions to keep track of annotations ans insertions

"""


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
            seq = self.sequence[:20] + "[...]" + self.sequence[-21:-1]
        else:
            seq = self.sequence
        return "Plasmid entry: \nName: {0} \nId: {1} \nInsert: {2} \n Antibiotic Resistance: {3} \nSequence: {4}\n ".format(self.name, self.id, self.insert, self.resistance, seq)
    def restrictioncuts(self, Enzimes):
        pass