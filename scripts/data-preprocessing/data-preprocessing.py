#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tayssirboukrouba
"""
import os
import pandas as pd


def classify_org(country):
    opec = ["Middle-East","Algeria","Nigeria"]

    if country in opec:
        return 'OPEC'
    if country in 'G7':
        return 'G7'
    if country in 'BRICS':
        return 'BRICS'
    else:
        return 'Other'

current_directory = os.getcwd()
files = sorted(os.listdir(current_directory))
dataframes = []

codes = ['ACO2E','CO2EFC','C02IACP','CBT','CC','CP','COBT','COP','EBT','EC','EP','TEBT','TEIGDP','GBT','GC','GP','OBT','OC','OP','SETE','SREEP','SWSEP','TEC','TEP']
#names = ['Coal Cons', 'Coal Prod', 'Crude Oil Prod', 'Elect Cons',
#         'Elect Prod', 'Gas Cons', 'Gas Prod', 'Oil Cons', 'Oil Prod', 
#         'Total Ener Cons', 'Total Ener Prod']
i = 0 
for file_name in files:
    file_path = os.path.join(current_directory, file_name)
    if file_name.endswith('.xlsx'):
        df = pd.read_excel(file_path,na_values="n.a.")
        print(df.columns)
        df['Code'] = codes[i]
        dataframes.append(df)
        i = i+1  


result_df = pd.concat(dataframes,ignore_index=True)
result_df.rename(columns={'Unnamed: 0':'Countries'},inplace=True)

# Get the list of column names
columns = list(result_df.columns)

# Move the last column to the first position
columns = [columns[-1]] + columns[:-1]

# Reorder the columns in the DataFrame
result_df = result_df[columns]


df_melted = result_df.melt(id_vars=['Countries', 'Code'],value_name='Value', var_name='Year', ignore_index=False)
df_pivoted = df_melted.pivot(index=['Countries', 'Year'], columns='Code', values='Value').reset_index()

df_pivoted.fillna(0,inplace=True)

df_pivoted.set_index(["Countries","Year"],inplace=True)
print(df_pivoted)


def replace_commas(column):
    return column.str.replace(',', '.')

columns_to_exclude = ['CC','CP','GP']

object_columns = df_pivoted.select_dtypes(include='object').columns.difference(columns_to_exclude)

df_pivoted[object_columns] = df_pivoted[object_columns].apply(replace_commas)
df_pivoted = df_pivoted.apply(pd.to_numeric, errors='ignore')
df_pivoted.fillna(0,inplace=True)
df_pivoted.reset_index(inplace=True)
print(df_pivoted.info())


df_pivoted["Orgs"] = df_pivoted["Countries"].apply(classify_org)

#csv_filename = 'Energy.csv'
#df_pivoted.to_csv(csv_filename, index=False)