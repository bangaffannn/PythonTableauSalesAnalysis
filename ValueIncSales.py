#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 06:13:39 2023

@author: macbook
"""

import pandas as pd

# READING CSV DATA

data = pd.read_csv("transaction2.csv")

data = pd.read_csv("transaction2.csv", sep = ';')

# SUMMARY OF THE DATA
data.info()

# DEFINING VARIABLES

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemPurchased = 6

# OPERATIONS

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemPurchased * ProfitPerItem
CostPerTransaction = NumberofItemPurchased * CostPerItem
SellingPricePerTransaction = NumberofItemPurchased * SellingPricePerItem

# CostPerTransaction COLUMN CALCULATIONS

CostPerItem = data["CostPerItem"]
NumberofItemPurchased = data["NumberOfItemsPurchased"]
CostPerTransaction = CostPerItem * NumberofItemPurchased

# adding a new column to a dataframe

data["CostPerTransaction"] = data["CostPerItem"] * data["NumberOfItemsPurchased"]

# data sales per transaction

data["SalesPerTransaction"] = data["SellingPricePerItem"] * data["NumberOfItemsPurchased"]

# profit calculation (sales-cost)

data["ProfitPerTrasaction"] = data["SalesPerTransaction"] - data["CostPerTransaction"]

# markup ((sales-cost)/cost)

data["Markup"] = (data["SalesPerTransaction"] - data["CostPerTransaction"]) / data["CostPerTransaction"]

# ROUNDING MARKUP

roundmarkup = round(data["Markup"], 2)

data["Markup"] = roundmarkup

# COMBINING DATA FIELD
# CHANGE COLUMN TYPE

day = data["Day"].astype(str)
year = data["Year"].astype(str)
date = day+"-"+data["Month"]+"-"+year

data["date"] = date

# SPLIT CLIENT KEYWORD FIELDS

split_col = data['ClientKeywords'].str.split(',', expand = True)

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

# REPLACE FUNCTION

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')

data['ItemDescription'] = data['ItemDescription'].str.lower()

# MERGE FILE AND ATTACH NEW DATASET

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# MERGING FILES

data = pd.merge(data, seasons, on = "Month")

# DROPPING COLUMNS

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

# EXPORTING TO CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)





















