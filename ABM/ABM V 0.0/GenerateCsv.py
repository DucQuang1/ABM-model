# -*- coding: utf-8 -*-
"""
Created on Wed May 20 00:50:02 2015

@author: Martin Nguyen
"""

#Generate CSV files in this file
numberOfPatients  = 3000
import csv
from numpy import random
from scipy import stats 
def csv_dict_writer(path, fieldnames, data):
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    mylist = []
    for line in reader:
        mylist.append(line["IOP"])
        #print(line["last_name"])
    #print mylist
IOP_range = (12.5,17.5,22.5,27.5,32.5)
IOP_prob = (0.004,0.256,0.529,0.175,0.027)
custm = stats.rv_discrete(name = 'custm', values = (IOP_range,IOP_prob))
if __name__ == "__main__":
    field_names = "IOP,MD,MDR,Age".split(",")
    print field_names
    my_list = []
    for i in range(numberOfPatients):
        IOP = custm.rvs(size = 1)
        MD = -random.gamma(2,2.5)
        while MD > -3:
            MD = - random.gamma(2,2.5)
        MDR = random.gamma(2,0.014)
        Age = random.normal(68,5)    
        inner_dict = dict(zip(field_names, [IOP,MD,MDR,Age]))
        my_list.append(inner_dict)
    #print my_list
    path = "Patients_list.csv"
    csv_dict_writer(path, field_names, my_list)
    with open("Patients_list.csv") as f_obj:
        csv_dict_reader(f_obj)
#==============================================================================
# def initializationAttributes(self):
#         self.Attribute['IOP'] = random.normal(28,3) # need to do truncation later
#         while self.Attribute['IOP'] < 22:
#             self.Attribute['IOP'] = random.normal(28,3)
#         self.Attribute['MD'] = -random.gamma(2,2.5) # need to do truncation later
#         while self.Attribute['MD'] > -3:
#             self.Attribute['MD'] = -random.gamma(2,2.5)
#         self.Attribute['MDR'] = random.gamma(2,0.014)
#         self.Attribute['Age'] = random.normal(68,5)
#==============================================================================