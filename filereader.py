from audioop import add
from os import path
import scipy.io
import torch

from General_csvreader import Csv_reader
import numpy as np
import pandas as pd


DistanceVector=np.load('distance_label.npy')
distance=np.array(DistanceVector)
print(distance[0])
print(np.array(DistanceVector).shape)
seg3=DistanceVector[:,0]
seg9=DistanceVector[:,1]
seg14=DistanceVector[:,2]
seg16=DistanceVector[:,3]
seg12=DistanceVector[:,4]
seg6=DistanceVector[:,5]

seg3_df = pd.DataFrame(seg3)
seg6_df = pd.DataFrame(seg6)
seg9_df = pd.DataFrame(seg9)
seg12_df = pd.DataFrame(seg12)
seg14_df = pd.DataFrame(seg14)
seg16_df = pd.DataFrame(seg16)


    
path = "Addresses.xlsx"
df = pd.read_excel(path)
df['seg3_ap4_dis'] = seg3_df
df['seg6_ap4_dis'] = seg6_df
df['seg9_ap4_dis'] = seg9_df
df['seg12_ap4_dis'] = seg12_df
df['seg14_ap4_dis'] = seg14_df
df['seg16_ap4_dis'] = seg16_df
df.to_excel('Addresses1.xlsx',index=False)