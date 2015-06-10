# -*- coding: utf-8 -*-
"""
Created on Wed May 20 00:50:02 2015

@author: Martin Nguyen
"""

#Generate CSV files in this file
numberOfPopulation = 1
numberOfPatients = 10000
import csv
from numpy import random
from scipy import stats 
import matplotlib.pyplot as plt 
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
        mylist.append(len(line["Asthma"]))
    #print mylist
    plt.hist(mylist)
IOP_range = (12.500,17.500,22.500,27.500,32.500)
IOP_prob = (0.004,0.256,0.529,0.175,0.027)
Group_range = (0,1,2,3,4,5)
Group_prob = (0.3938,0.0530,0.0436,0.4022,0.0626,0.0448)
Asthma_Prevalance = (0.05856,0.07726,0.03985,0.07650,0.10094,0.05206)
random_IOP = stats.rv_discrete(name = 'randomIOP', values = (IOP_range,IOP_prob))
random_Group = stats.rv_discrete(name = 'randomGroup', values = (Group_range,Group_prob))
if __name__ == "__main__":
    field_names = "IOP,Group,Asthma,PAallergy,A2allergy".split(",")
    print field_names
    
    #print my_list
    path = "Patients_list.csv"
    for j in range(numberOfPopulation):    
        
        my_list = []
        for i in range(numberOfPatients):
            IOP = float(random_IOP.rvs() + 0.5)
            Group = int(random_Group.rvs())
            #
            Asthma =  Asthma_Prevalance[Group]
            PAallergy = (random.uniform(0,1) < 0.1)
            A2allergy = (random.uniform(0,1) < 0.3)
            inner_dict = dict(zip(field_names, [IOP,Group,Asthma,PAallergy,A2allergy]))
            my_list.append(inner_dict)
        csv_dict_writer("Patients_list_{}.csv".format(j), field_names, my_list)
        with open('Patients_list_{}.csv'.format(j)) as f_obj:
            csv_dict_reader(f_obj)