# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:54:43 2015

@author: Martin Nguyen
"""
from __future__ import division
import simpy
import csv
#from MonitorClass import Monitor
from PatientClass import Patient
simulationTime = 100
class SimulationSystem(object):
    def __init__ (self,size,file_name):
        self.size = size
        self.file_name = file_name
        self.list_IOP = []
        self.list_Group = []
        self.list_Asthma = []
        self.list_PAallergy = []
        self.list_A2allergy = []
        self.patientlist = []
        #self.monitor = Monitor (self.size)
    def csv_dict_reader(self,file_obj):
        reader = csv.DictReader(file_obj, delimiter=',')
        for line in reader:
            self.list_IOP.append(float(line["IOP"]))
            self.list_Group.append(float(line["Group"]))
            self.list_Asthma.append(float(line["Asthma"]))
            self.list_PAallergy.append(line["PAallergy"])
            self.list_A2allergy.append(line["A2allergy"])
    def final_cost_calculate(self):
        i = 0
        for obj in self.patientlist:
#            obj.CostAttribute['TotalCost'] += (obj.medicalRecords['NumberTrabeculectomy'] * 1214 + obj.medicalRecords['PatientVisits'] * (6+2+65))
#            obj.CostAttribute['TotalCost'] += (obj.CostAttribute['Below-15']*325 + obj.CostAttribute['ProductiveLoss']*3029)  
#            obj.CostAttribute['TotalCost'] += (obj.medicalRecords['NumberVF'] *150)
            #self.monitor.finalCostPatient(i,obj.medicalRecords['NumberTrabeculectomy'],obj.medicalRecords['PatientVisits'],obj.medicalRecords['NumberVF'])
            i += 1
    def SystemSimulation (self):
        
        with open(self.file_name) as f_obj:
            self.csv_dict_reader(f_obj)
        env = simpy.Environment()   
        
        for i in range(self.size):
            #self.monitor,
            self.patientlist.append( Patient(env,i,{'IOP':self.list_IOP[i],'Group': self.list_Group[i],'Asthma':self.list_Asthma[i],'PAallergy': self.list_PAallergy[i],'A2allergy': self.list_A2allergy[i],'Progression':False,  'Age': 50}))
        env.run(until = simulationTime)
        self.final_cost_calculate ()

