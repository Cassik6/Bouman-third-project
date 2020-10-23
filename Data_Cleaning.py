## found a way to remove white spances in columnsqq

import pandas as pd 
import numpy as np
import re

# defining null values so we can replace them easely with fillna() method
missing_values = ['','nan', 'None','Notspecified']

df = pd.read_csv("unique_ids.csv", na_values= missing_values)

# removing the spaces at the end and begining of the column name
for i in df.columns:
    df.rename(columns={i: i.strip()}, inplace=True)

# removes dataset from group 2
df = df.drop(df[df.source == 2].index)

# removing dolar signs, commas and euro signs in the price column
# df['price'] = df['price'].replace({'$': '', ',': '',"€":""}, regex=True)


del df['Unnamed: 0']

# area :
# making sure we have only numeric values
# null values are replaced by -1
# making sure there are no numbers after commas



df['area'] = df['area'].astype(str)
# removing m² and white spaces
df['area'] = df['area'].replace({'m': '', ' ': '',"²":""}, regex=True)
# changing all row with Notspecified to NaN
df.loc[df.area == "Notspecified"] = np.nan
df.loc[df.area == "nan"] = np.nan
# remove numbers after the comma
df['area'] = df['area'].str.replace('.0','')
# deal with empty strings
df.loc[df['area'] == '', 'area'] = '-1'
# replace all null values with -1
df.area.fillna('-1', inplace=True)
# deal with 0 as an int
df.loc[df['area'] == 0, 'area'] = '-1'
# deal with 0 as a string
df.loc[df['area'] == '0', 'area'] = '-1'
# tranform everyting in numeric value
df["area"] = pd.to_numeric(df["area"])
print(df.area.isnull().sum())


df['property_subtype'] = df['property_subtype'].astype(str)
df['property_subtype'] = df['property_subtype'].apply(lambda x : x.upper())

def float_price(price):
    if None == price:
        return -1
    if type(price) == str:

        match  = re.match('[0-9.,]+', price)
        if match :
            matchPrice = re.search('[0-9.,]+', price).group(0)
            matchPrice = matchPrice.replace(',','.')
            return float(matchPrice)
        else :
            return -1
    else :
        return float(price)

df.price = df.price.apply(lambda x : float_price(x))
df.price = df.price.fillna(-1)


#we need to delete the duplicates. We have in hyperlink column the immoweb id's and the urls. 
#We cut the missing id's from the urls with regex.

# the fuction of getting id's
def find_id(x):
    if type(x) is str and "immoweb" in x:
        for n in re.findall("([0-9]+)",x):
            if len(n) == 7:

                return int (n)
    else: 
        return x

df.hyperlink = df.hyperlink.apply(find_id)

#check the null values
df.hyperlink.isnull().sum()

#change the type
df.hyperlink = pd.to_numeric(df['hyperlink'],errors='coerce')
#check the null values after changing the type: no mising value
df.hyperlink.isnull().sum()


#see the duplicated id's
duplicateRowsDF = df[df.duplicated(["hyperlink"])]
duplicateRowsDF

#drop the empty id's
df = df[df['hyperlink'].notna()]

#drop the duplicated id's
df = df.drop_duplicates(subset=['hyperlink'])

#the id's are unique
df.hyperlink.is_unique

#save the file
df.to_csv('unique_ids.csv')


#number of rooms
#the missing parts of rooms_number column fixed as "-1" to convert the type
df[df.rooms_number==""] = np.NaN
df['rooms_number'] = df['rooms_number'].fillna(-1)
df.loc[df['rooms_number'] == '', 'rooms_number'] = '-1'
df.loc[df['rooms_number'] == 'None', 'rooms_number'] = '-1'

df["rooms_number"] = pd.to_numeric(df["rooms_number"])

df['terrace_area'] = df.terrace_area.fillna(df.terrace)

def booleanClean(boolean):
        if str == type(boolean):
            if 'TRUE' == boolean.upper():
                return True
            if 'FALSE' == boolean.upper():
                return False
            try :
                float(boolean)
                return True
            except :
                return boolean

        if float == type(boolean):
            if np.isnan(boolean):
                return boolean
            else :
                return True
        else :
            return boolean      
    

df.terrace = df.terrace.apply(lambda x: booleanClean(x))

# cleaning terrace area
def clean_terrace_area(data):
    if str == type(data):
        if 'TRUE' == data.upper() or 'FALSE' == data.upper():
            return 0
        return data
    else :
        return data
        
df.terrace_area = df.terrace_area.apply(lambda x: clean_terrace_area(x))

#defining boolean clean method
def booleanClean(boolean):
        if str == type(boolean):
            if 'TRUE' == boolean.upper():
                return True
            if 'FALSE' == boolean.upper():
                return False
            try :
                float(boolean)
                return True
            except :
                return boolean

        if float == type(boolean):
            if np.isnan(boolean):
                return boolean
            else :
                return True
        else :
            return boolean

# cleaning garden area and garden
df['garden_area'] = df.garden_area.fillna(df.garden)

df.garden = df.garden.apply(lambda x: booleanClean(x))

def clean_garden_area(data):
        if str == type(data):
            if 'TRUE' == data.upper() or 'FALSE' == data.upper():
                return np.nan
            else :
                return data
        else:
            return data

df.garden_area = df.garden_area.apply(lambda x: clean_garden_area(x))


#cleaning building state
def clean_building_state(state):
    if str == type(state):
        state = state.replace(' ','_')
        state = state.upper()
        return state
    else :
        return state

df.building_state = df.building_state.apply(lambda x: clean_building_state(x))

print(len(df.building_state.unique()))
df.building_state.unique()

df.building_state = df.building_state.replace('0', np.nan)

