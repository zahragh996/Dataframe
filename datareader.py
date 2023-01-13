import torch
import pandas 
import os
import numpy as np

file_path= "369.xls"



excel_data_df = pandas.read_excel('369.xlsx', sheet_name='369', usecols=['seg1','seg2','seg3','seg4','seg5','seg6','seg7','seg8','seg9','seg10','seg11','seg12','seg13','seg14','seg15','seg16','ap2_quals','ap4_quals','plax_quals','ap3_quals','ap2_paths','ap4_paths','plax_paths','ap3_paths'])

#########################################################
ap2_quals_list=excel_data_df.loc[:,'ap2_quals']
ap2_quals=ap2_quals_list.values
ap2_qmylist=[]
for i in range(len(ap2_quals)):
    ap2_qmylist.append(np.array(ap2_quals[i][1:-1].split(',')).astype(float))
# print(ap2_qmylist)


#######################################################
ap3_quals_list=excel_data_df.loc[:,'ap3_quals']
ap3_quals=ap3_quals_list.values
# print(ap3_quals)
ap3_qmylist=[]
for i in range(len(ap3_quals)):
    ap3_qmylist.append(np.array(ap3_quals[i][1:-1].split(',')).astype(float))



########################################################
ap4_quals_list=excel_data_df.loc[:,'ap4_quals']
ap4_quals=ap4_quals_list.values
ap4_qmylist=[]
for i in range(len(ap4_quals)):
    ap4_qmylist.append(np.array(ap4_quals[i][1:-1].split(',')).astype(float))
# print(ap4_qmylist)



######################################################
plax_quals_list=excel_data_df.loc[:,'plax_quals']
plax_quals=plax_quals_list.values
# print(plax_quals)
plax_qmylist=[]
for i in range(len(plax_quals)):
    plax_qmylist.append(np.array(plax_quals[i][1:-1].split(',')).astype(float))
# print(plax_qmylist)
######################################################## Path

ap2_paths_list=excel_data_df.loc[:,'ap2_paths']
ap2_paths=ap2_paths_list.values
# print(ap2_quals)
# print(ap2_paths[0][1:-1].split(',')[0])

#########################################################
ap3_paths_list=excel_data_df.loc[:,'ap3_paths']
ap3_paths=ap3_paths_list.values
# print(ap3_quals)
###########################################################

ap4_paths_list=excel_data_df.loc[:,'ap4_paths']
ap4_paths=ap4_paths_list.values
# print(ap4_quals)
#############################################
plax_paths_list=excel_data_df.loc[:,'plax_paths']
plax_paths=plax_paths_list.values
# print(plax_paths)
#################################################
print(ap4_paths[174])
address=[]
index=[]
for i in range(len(ap2_quals)):
    print('i',i)
    print(ap2_qmylist[i])
    print(np.argmax(ap2_qmylist[i]))
    print(ap2_paths[i][1:-1].split(',')[np.argmax(ap2_qmylist[i])])
    address.append(ap2_paths[i][1:-1].split(',')[np.argmax(ap2_qmylist[i])])
    index.append(0)


    print(ap3_qmylist[i])
    print(np.argmax(ap3_qmylist[i]))
    print(ap3_paths[i][1:-1].split(',')[np.argmax(ap3_qmylist[i])])
    address.append(ap3_paths[i][1:-1].split(',')[np.argmax(ap3_qmylist[i])])
    index.append(1)


    print(ap4_qmylist[i])
    print(np.argmax(ap4_qmylist[i]))
    print(ap4_paths[i][1:-1].split(',')[np.argmax(ap4_qmylist[i])])
    address.append(ap4_paths[i][1:-1].split(',')[np.argmax(ap4_qmylist[i])])
    index.append(2)
    
    print(plax_qmylist[i])
    print(np.argmax(plax_qmylist[i]))
    print(plax_paths[i][1:-1].split(',')[np.argmax(plax_qmylist[i])])
    address.append(plax_paths[i][1:-1].split(',')[np.argmax(plax_qmylist[i])])
    index.append(3)
print(address)

df=pandas.read_excel('address1.xlsx')
df['address'] = pandas.DataFrame(address) 
df['index'] = pandas.DataFrame(index)  
df.to_excel('adress369.xlsx',index=False)




seg1_list=excel_data_df.loc[:,'seg1']
seg1=seg1_list.values
# print(seg1)



seg2_list=excel_data_df.loc[:,'seg2']
seg2=seg2_list.values
# print(seg2)

seg3_list=excel_data_df.loc[:,'seg3']
seg3=seg3_list.values
# print(seg3)


seg4_list=excel_data_df.loc[:,'seg4']
seg4=seg4_list.values
# print(seg4)



seg5_list=excel_data_df.loc[:,'seg5']
seg5=seg5_list.values
# print(seg5)

seg6_list=excel_data_df.loc[:,'seg6']
seg6=seg6_list.values
# print(seg6)


seg7_list=excel_data_df.loc[:,'seg7']
seg7=seg7_list.values
# print(seg7)

seg8_list=excel_data_df.loc[:,'seg8']
seg8=seg8_list.values
# print(seg8)


seg9_list=excel_data_df.loc[:,'seg9']
seg9=seg9_list.values
# print(seg9)


seg10_list=excel_data_df.loc[:,'seg10']
seg10=seg10_list.values
# print(seg10)

seg11_list=excel_data_df.loc[:,'seg11']
seg11=seg11_list.values
# print(seg11)


seg12_list=excel_data_df.loc[:,'seg12']
seg12=seg12_list.values
# print(seg12)

seg13_list=excel_data_df.loc[:,'seg13']
seg13=seg13_list.values
# print(seg13)


seg14_list=excel_data_df.loc[:,'seg14']
seg14=seg14_list.values
# print(seg14)

seg15_list=excel_data_df.loc[:,'seg15']
seg15=seg15_list.values
# print(seg15)

seg16_list=excel_data_df.loc[:,'seg16']
seg16=seg16_list.values
# print(seg16)


Sum_segs=seg1 + seg2 + seg3 + seg4 + seg5 + seg6 + seg7 + seg8 + seg9 + seg10 + seg11 + seg12 + seg13 + seg14 + seg15 + seg16
# print(Sum_segs)










# for i in range(len(ap2_paths)):


# GWMA=[]
# for i in range(len(Sum_segs)):
#     if Sum_segs[i]==32 and seg1[i]==2 and seg2[i]==2 and seg3[i]==2 and seg4[i]==2 and seg5[i]==2 and seg6[i]==2 and seg7[i]==2 and seg8[i]==2 and seg9[i]==2 and seg10[i]==2 and seg11[i]==2 and seg12[i]==2 and seg13[i]==2 and seg14[i]==2 and seg15[i]==2 and seg16[i]==2:
#         GWMA.append(1)
#     else:
#         GWMA.append(0)
# GWMA1=[]
# for i in range(len(Sum_segs)):
#     if Sum_segs[i]==32:
#         GWMA1.append(1)
#     else:
#         GWMA1.append(0)



# index, = np.where(np.array(GWMA)!=np.array(GWMA1))
# print('different indexes',index)
# w=np.sum(np.array(GWMA),axis=0)
# print(len(GWMA),w)
# # print(GWMA)

# excel_data_df = pandas.read_excel('RWMA_v1.xlsx', sheet_name='RWMA_v1')

# excel_data_df ["GWMA"] = GWMA
# excel_data_df.to_excel("RWMA_V2.xlsx",index=False)