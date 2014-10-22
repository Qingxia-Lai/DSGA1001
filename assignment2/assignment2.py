# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 13:18:53 2014

@author: LaiQX
"""
import pandas as pd

ads = pd.read_table('ads_dataset.txt')

def getDfSummary(val):
    col = val.columns
    na_num=[]
    dst_num=[]
    for i in col:
        na_n=0
        na_n=sum(pd.isnull(val[i]))
        na_num.append(na_n)
        dst_n=len(val.groupby(i))
        dst_num.append(dst_n)
    summary=val.describe()
    summary=summary.T
    summary['NaN_count']=na_num
    summary['Distinct_Values']=dst_num
    summary = summary
    return summary

a = getDfSummary(ads)
a_m = getDfSummary(ads[pd.isnull(ads["buy_freq"])])

#df = ads.columns(2)

#cor = ads.corr()

#df = pd.DataFrame(ads[col[2]],ads['buy_freq'])
