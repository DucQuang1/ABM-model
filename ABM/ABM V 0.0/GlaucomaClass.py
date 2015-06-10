# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:52:22 2015

@author: Martin Nguyen
"""
TimenoIncidence = 2
from numpy import random
from scipy import stats
Eye_lost_range = (1,2)
Eye_lost_prob = (0.75,0.25) 
random_Eye = stats.rv_discrete(name = 'randomEye', values = (Eye_lost_range, Eye_lost_prob))
class Glaucoma(object):
    def __init__(self,name,Attribute, medicalRecords):
        self.name = name
        self.Attribute = Attribute
        self.medicalRecords = medicalRecords
    def UpdateAnnual (self):
        self.medicalRecords['Years'] += 1
        if self.medicalRecords['Years'] < TimenoIncidence:
            self.medicalRecords['EyeLost'] = int(random_Eye.rvs())
            if self.medicalRecords['Asthma'] == False:
                self.medicalRecords["Asthma"] = (random.uniform(0,1) < float(self.Attribute['Asthma']))
