import torch
import pandas 
import os
import numpy as np
import pandas as pd
file_path= "RWMA_quality4Christina.xlsx"



df_main = pandas.read_excel('RWMA_quality4Christina.xlsx', sheet_name='RWMA_quality4Christina', usecols=['index','seg1','seg2','seg3','seg4','seg5','seg6','seg7','seg8','seg9','seg10','seg11','seg12','seg13','seg14','seg15','seg16','ap2_quals','ap4_quals','plax_quals','ap3_quals','ap2_paths','ap4_paths','plax_paths','ap3_paths'])
df_half = pandas.read_excel('184.xlsx', sheet_name='Sheet1', usecols=['index','seg1','seg2','seg3','seg4','seg5','seg6','seg7','seg8','seg9','seg10','seg11','seg12','seg13','seg14','seg15','seg16','ap2_quals','ap4_quals','plax_quals','ap3_quals','ap2_paths','ap4_paths','plax_paths','ap3_paths'])
##########################################
index_main=df_main.loc[:,'index']
index_main_value=index_main.values
print('index_main_value',index_main_value)
#########################################
index_half=df_half.loc[:,'index']
index_half_value=index_half.values
print('index_half_value',len(index_half_value))
##########################################
print(len(df_half['index'].unique()))
print(len(set(df_main['index']).intersection(set(df_half['index']))))

#########
#get uncommon rows
print(pd.concat([df_main,df_half]).drop_duplicates(keep=False))

(pd.concat([df_main,df_half]).drop_duplicates(keep=False)).to_excel('restofdata.xlsx',index=False)