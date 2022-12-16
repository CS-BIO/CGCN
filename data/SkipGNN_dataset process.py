# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:13:34 2022

@author: 申聪
"""
import random

#fr = open("DGI.edgelist","r")
#
#mol1 = []
#mol2 = []
#sample_pos = []
#
#entity_list = []
#
#for line in fr:
#    arrline = line.strip().split("\t")
#    sample_pos.append(line.strip())
#    mol1.append(arrline[0])
#    mol2.append(arrline[1])
#    
#    if arrline[0] not in entity_list:
#        entity_list.append(arrline[0])
#    if arrline[1] not in entity_list:
#        entity_list.append(arrline[1])
#    
#neg_flag = 1
#sample_neg = []
#while neg_flag == 1:
#    neg_mol1_index = random.randint(0,len(mol1)-1)
#    neg_mol2_index = random.randint(0,len(mol2)-1)
#    
#    neg_mol1 = mol1[neg_mol1_index]
#    neg_mol2 = mol2[neg_mol2_index]
#
#    
#    if neg_mol1 + "\t" + neg_mol2 not in sample_pos:
#        if neg_mol1 + "\t" + neg_mol2 not in sample_neg:
#            print(neg_mol1 + "\t" + neg_mol2)
#            sample_neg.append(neg_mol1 + "\t" + neg_mol2)
#    if len(sample_neg) == len(sample_pos):
#        neg_flag = 0
#
#samples = []
#for i in range(len(sample_pos)):
#    samples.append(sample_pos[i]+"\t"+"1")
#    samples.append(sample_neg[i]+"\t"+"0")
#
#train_num = int(len(samples)*0.7)
#val_num = int(len(samples)*0.8)
#
#fw_train = open("DGI_train_sample.txt","w")
#fw_val = open("DGI_val_sample.txt","w")
#fw_test = open("DGI_test_sample.txt","w")
#
#for j in range(len(samples)):
#    if j <= train_num:
#        fw_train.writelines(samples[j])
#        fw_train.writelines("\n")
#    elif j > train_num and j <= val_num:
#        fw_val.writelines(samples[j])
#        fw_val.writelines("\n")
#    else:
#        fw_test.writelines(samples[j])
#        fw_test.writelines("\n")
#
#fw_entity = open("DGI_entity_list.txt","w")
#
#for k in range(len(entity_list)):
#    fw_entity.writelines(entity_list[k])
#    fw_entity.writelines("\n")
    





fr = open("Drugbank_DDI.edgelist","r")

mol1 = []
mol2 = []
sample_pos = []

entity_list = []

for line in fr:
    arrline = line.strip().split("\t")
    sample_pos.append(line.strip())
    mol1.append(arrline[0])
    mol2.append(arrline[1])
    
    if arrline[0] not in entity_list:
        entity_list.append(arrline[0])
    if arrline[1] not in entity_list:
        entity_list.append(arrline[1])
    
neg_flag = 1
sample_neg = []
while neg_flag == 1:
    neg_mol1_index = random.randint(0,len(entity_list)-1)
    neg_mol2_index = random.randint(0,len(entity_list)-1)
    
    neg_mol1 = entity_list[neg_mol1_index]
    neg_mol2 = entity_list[neg_mol2_index]
    
    if neg_mol1 + "\t" + neg_mol2 not in sample_pos and neg_mol1 != neg_mol2:
        if neg_mol1 + "\t" + neg_mol2 not in sample_neg:
            print(neg_mol1 + "\t" + neg_mol2)
            sample_neg.append(neg_mol1 + "\t" + neg_mol2)
    if len(sample_neg) == len(sample_pos):
        neg_flag = 0

samples = []
for i in range(len(sample_pos)):
    samples.append(sample_pos[i]+"\t"+"1")
    samples.append(sample_neg[i]+"\t"+"0")

train_num = int(len(samples)*0.7)
val_num = int(len(samples)*0.8)

fw_train = open("Drugbank_DDI_train_sample.txt","w")
fw_val = open("Drugbank_DDI_val_sample.txt","w")
fw_test = open("Drugbank_DDI_test_sample.txt","w")

for j in range(len(samples)):
    if j <= train_num:
        fw_train.writelines(samples[j])
        fw_train.writelines("\n")
    elif j > train_num and j <= val_num:
        fw_val.writelines(samples[j])
        fw_val.writelines("\n")
    else:
        fw_test.writelines(samples[j])
        fw_test.writelines("\n")

fw_entity = open("Drugbank_DDI_entity_list.txt","w")

for k in range(len(entity_list)):
    fw_entity.writelines(entity_list[k])
    fw_entity.writelines("\n")
















