import pandas 
import os

class Csv_reader():
  'Characterizes a dataset for PyTorch'
  def __init__(self, file_path):
        'Initialization'
        self.file_path = file_path
        

  def get_column(self, Name=None, colomn_num=None):
        
        if colomn_num is not None:
            header = None
        elif Name is not None:
            header = 0
        if Name is None and colomn_num is None:
            raise ValueError("expected only one of the name or colmn-num not to be None")
        elif Name is not None and colomn_num is not None:
             raise ValueError("expected only one of the name or colmn-num")
        excel_data_df = pandas.read_excel(self.file_path, sheet_name=self.file_path.split('.')[0], header=header)


        list_adresses=excel_data_df[Name if Name is not None else colomn_num].tolist()
        # df_adresses=excel_data_df[Name if Name is not None else colomn_num]
        
        return  list_adresses


  def split_data(self,list_adresses,i):
       
        return list_adresses[i].split('/')[6].split('.pbz2')[0]+'.dcm'
