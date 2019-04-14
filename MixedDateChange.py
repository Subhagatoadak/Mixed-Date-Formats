# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 23:09:33 2019

@author: Subhagato Adak
Many times there are files with mixed date formats, this causes a lot of problem while
processing the data. this module helps simple methods to convert and export date formats 
in a required format.
"""
import pandas as pd

class MixedDateformats:
    """
    Enter the path of the file in the class to read the dataframe.
    """
    def __init__(self,pathname):
        self.datafrm = pd.read_csv(pathname)
    """
    Enter the input_columnname, format, required format, output column name and output file name 
    to run the method and get the fixed date format types.
    """
    def dateformatchange_export(self,inpt_clmnname,frmt,req_frmt,otpt_clmnname,output_filename):
        self.datafrm[otpt_clmnname]=pd.to_datetime(self.datafrm[inpt_clmnname], format=frmt, errors='coerce').dt.strftime(req_frmt)
        self.datafrm.to_csv(output_filename,index=False)
       
    def dateformatchange(self,inpt_clmnname,frmt,req_frmt,otpt_clmnname):
        self.datafrm[otpt_clmnname]=pd.to_datetime(self.datafrm[inpt_clmnname], format=frmt, errors='coerce').dt.strftime(req_frmt)
        return self.datafrm
       
        
        

