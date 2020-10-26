import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
%matplotlib inline
import seaborn as sns

df = pd.read_csv("immo_data_set.csv")
pd.set_option('display.float_format', '{:.2f}'.format)

#the 5 most expensive properties by average prices for each postcode
df_gb_post_mean = df.groupby(by = "postcode").mean().sort_values(by='price',ascending=False)[:5]
df_gb_post_mean.plot(y= "price" , kind = 'bar')
plt.title ("5 most expensive postcodes")
plt.show()

#the 5 least expensive properties by average prices for each postcode
df_gb_post_mean = df.groupby(by = "postcode").mean().sort_values(by='price',ascending=True)[:5]
df_gb_post_mean.plot(y= "price" , kind = 'bar')
plt.title ("5 least expensive postcodes")
plt.show()

# to find out the prices by provinces, we used groupby function
df_gb_province_mean = df.groupby(by = "Province").mean().sort_values(by='price',ascending=False)
df_gb_province_mean

df_gb_province_mean.plot(y= "price" , kind = 'bar')
plt.title("The Average Price by Province")
plt.show()

#to see the prices according to property type we grouped the data frame by privinces and property types
df.groupby(["Province", "property_subtype"]).mean().sort_values(by='price',ascending=False)

property_t_list = df.groupby("property_subtype").count().index.to_list()

# this function is generating graphs according to provinces
def type_to_bar (type_prop):
    df_type = df.loc[df["property_subtype"] == type_prop].groupby("Province").mean().sort_values(by='price',ascending=False)
    df_type.plot(y= "price" , kind = 'bar')
    plt.title(type_prop)

# use the function for each property types
for n in property_t_list:
    type_to_bar(n)   

type_to_bar("APARTMENT")

#This graph shows the count distribution of selling properties for each provinces.
df_province_count = df.groupby("Province").count()
plot = df_province_count.plot.pie(y = "hyperlink", figsize=(5, 5), subplots=False, autopct='%1.1f%%',
                                  legend = False, fontsize=10)
plt.title("The Distribution of Sellig Properties by Provinces")

df_province_count = df.groupby("Region").count()
plot = df_province_count.plot.pie(y = "hyperlink", figsize=(5, 5), subplots=False, autopct='%1.1f%%',
                                  legend = False, fontsize=10)
plt.title("The Distribution of Sellig Properties by Region")

# the avrage price of houses and apartments by province
sns.set_style('whitegrid')
df_a_h = df[df["property_subtype"].isin(["APARTMENT", "HOUSE"])]
plt.figure(figsize=(12,8))
sns.barplot(x='Province', y= "price",hue='property_subtype',data=df_a_h)
plt.xticks(rotation=90)
plt.title ("Average price of selling houses and apartments by province")

#total number of selling houses and apartments by province
plt.figure(figsize=(12,8))
sns.countplot(x='Province',hue='property_subtype',data=df_a_h)
plt.xticks(rotation=90)
plt.title ("Number of selling houses and apartments by province")

# the avrage price of houses and apartments by region

plt.figure(figsize=(12,8))
sns.barplot(x='Region', y= "price",hue='property_subtype',data=df_a_h)
plt.xticks(rotation=90)
plt.title ("Average price of selling houses and apartments by region")

#total number of selling houses and apartments by region

plt.figure(figsize=(12,8))
sns.countplot(x='Region',hue='property_subtype',data=df_a_h)
plt.xticks(rotation=90)
plt.title ("Number of selling houses and apartments by region")

df = pd.read_csv("immo_data_set.csv")

# graphs for price per square meter by province/region and for appartments/houses

ff = df[df.area > 20]
ff_house = df[df.house_is == 1]
ff_app =df[df.house_is == 0]
ff_house['price per square meter'] = ff.price / ff.area
ff_app['price per square meter'] = ff.price / ff.area
province_house = ff_house.groupby(['Province']).mean().sort_values(by='price per square meter',ascending=False)['price per square meter']
province_app = ff_app.groupby(['Province']).mean().sort_values(by='price per square meter',ascending=False)['price per square meter']
region_house = ff_house.groupby(['Region']).mean().sort_values(by='price per square meter',ascending=False)['price per square meter']
region_app = ff_app.groupby(['Region']).mean().sort_values(by='price per square meter',ascending=False)['price per square meter']


province_app.plot(y= "price per square meter" , kind = 'bar')
plt.title('Province: Appartment average price per m²')
plt.ylabel('Price')
plt.show()
province_house.plot(y= "price per square meter" , kind = 'bar')
plt.title('Province: House average price per m²')
plt.ylabel('values')
plt.show()
region_house.plot(y= "price per square meter" , kind = 'bar')
plt.title('Regions: Appartment average price per m²')
plt.ylabel('values')
plt.show()
region_app.plot(y= "price per square meter" , kind = 'bar')
plt.title('Regions: House average price per m²')
plt.ylabel('values')
plt.show()

#linear regression line in a scatter graph for 2 badroom apartment in Brussels with out garden and terrace
import matplotlib.ticker as mtick
g = sns.lmplot(x="area", y='price', data=df.loc[(df["price"]>500)& 
                                            (df["area"]<3000) & 
                                            (df["garden"] == False)&
                                            (df["terrace"]==False)&
                                            (df["Province"] == "Brussels")&
                                            (df["rooms_number"] == 2)&
                                            (df["property_subtype"] == "APARTMENT")])
plt.title("2-badroom-apartments w/o terrace and gareden in Brussels")

