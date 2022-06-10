#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 23:55:25 2022

@author: sandrapurkovic
"""

import pandas as pd
#file_name = pd.read_csv('file.csv')<--- format of read_csv
data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv',sep=';')

#summary of the data
data.info()

#working with calculations
#defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathemathical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = ProfitPerItem * NumberOfItemsPurchased
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * NumberOfItemsPurchased


#Cost per transaction column calculation = COstPerItem * NumberofItemsPurchased
#variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new column to a dataframn
data['CostPerTransaction'] = CostPerTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calcualation Sales-Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#markap = Sales-cost) /Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

#rounding Markup

roundmarkap = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#combining data fields

my_date = 'Day' +'-'+'Month'+'-'+'Year'


#change columns type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)
my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#using ilock to view specigic columns or rows
data.iloc[0] #views the row with index = 0

data.iloc[0:3]#views first 3 rows
data.iloc[0-5:]#views ast 5 rows
data.head(5)#views first 5 rows
data.iloc[:,2]#all rows and second column
data.iloc[4,2]#views 4th row and 2nd column


#using slit to split teh client's keywords
#new_var = column.str.split('sep', expand = True)
split_col = data['ClientKeywords'].str.split(',' , expand=True)
#creating new columns for the split columns in client keayword
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfClientContract'] = split_col[2]
#using te replace function to remove square brackets
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfClientContract'] = data['LengthOfClientContract'].str.replace(']','')
data['LengthOfClientContract'] = data['LengthOfClientContract'].str.replace("'",'')
data['ClientType'] = data['ClientType'].str.replace("'",'')
data['ClientAge'] = data['ClientAge'].str.replace("'",'')
#using the lower function to change Caps lock to lower case

data['ItemDescription'] = data['ItemDescription'].str.lower()


seasons = pd.read_csv('value_inc_seasons.csv',sep=';')
#merge 2 files: merge file = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns df.drop('columnName' , axis = 1)
data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)
data = data.drop('Year' , axis = 1)
data = data.drop('Month' , axis = 1)



#export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)

















