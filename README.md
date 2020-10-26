# Data Analysis Project

## Mission

The main tasks for this project is to complete an analysis and interpretation of our main dataset.
Those tasks are done in order to have everything required to achieve the goal of this project : predict prices on Belgium's Real Estate sales.
As a optional goal, based on our work, we had to estimate which machine learning model would be the most suited to solve our problematic. 

## Participants

- Mikael Dominguez (Project manager)
- Selma Esen
- Opap's Ditudidi
- Christophe Giets

## Our process

The three following task in order to setup our team with necessary tools were tackled pretty quickly by reparting the work between the members.
- Create a Trello (https://trello.com/invite/b/KPxOlDhV/4d82988031b544b4148e1eef8787ad01/data-project)
- Create the Github (https://github.com/Cassik6/Bouman-third-project)
- Collect the data (See task 0 here under)

### 0. Collect and Join the datasets

Our first given task was to collect the datasets delivered by each group from the first project ("Immoliza").
After all the datasets were collected, we had to join them in one main dataset.
Once each group had a complete dataset, the project leaders had to meet in order to decide which common dataset would be used by all the groups as a base to really start to work on the project.


### 1. Data Cleaning

The Data Cleaning was definitely the biggest challenge for this project. And to accomplish the other steps and reach our final goal, we had to make sure we had a proper dataset to work on. Therefore, the Project Manager allocated most of the workforce to this single task.

We decided to remove the "source 2" from the dataset as most of those datas were inconsistant. With many properties from cities out of Belgium.

We devided the data cleaning in three main parts :

#### a) Suppressing duplicates :
As our main dataset was composed of small datasets really similar, we had a lot of overlapping data's. In other words, duplicates.

- As all the datasets centralized were from Immoweb, our strategy to get rid of most of the duplicates, was to use the Immoweb ID of the properties. When there was an URL, we extracted the ID from the URL itself so we had consistant values in our "ID" column. After which, we deleted all the rows without any ID.
- Afterwwards, we used the dropduplicate function in Pandas to make sure all our id's were unique.
- We noticed that even after this we had some duplicates, we then used a grouped primary key to delete those (price, estate type, province, postcode, number of rooms , garden, surface, land surface). We are aware we might have lost some data in the process, but it is largely minimized compared to the impact the real duplicates would have had.

#### b) Adjusting formats : 
Once we cleared as many duplicates as possible, we had to make sure the format of our values in a single column were all similar to be able to use them correctly later on in the project.
For most columns, we had values of different types (string, boolean, numerical). For each column, we made sure we had only one type left and all formatted in the same way (integers or float, lower case or capital letters, etc).
Another challenge was to identify null values as every dataset had different ways to express them. Finally we managed to isolate them and threat them accordingly.

#### c) Trimming : 
After the first two tasks, we could still notice many data's that would not make sense or that after some research would reveal some duplicates left in the dataset.
As most of the cleaning was already done and this task is really time consuming we decided to keep this task for the end of the project if we had some time left.
Here is a summary of what we did for each columns :
- Prices : We removed all prices under 10 000 euros. As all the really low values were most likely wrong and would misleead our results.
- Sale : As more then 90% of the values were missing and the column wouldn't really add value, we decided to delete the column
- Source : Once we deleted all data's coming from the second source, we decided this colum was no longer useful.
- Locality : As many values were missing in localities and the format were too differents to be treated, we decided that it would be sufficient to keep the postcode column withoout localities.
- Surface : since this will be part of an important metric we needed to make sure that this data was accurate. When using the surface we decided to ignore rows with less than 20 m² as surface value.
- All data without with unexploitable values and that could impact results of our analysis were discarded. 
 
### 2. Data Analysis

This part really required a clean dataset to be performed. So we couldn't get any further before step one was over. 
To make a clear answer to the following questions we made a distinction between three  different type of variables :

- Measurable variables : Such as number of rooms or area
- Address variables : The variables related to the address of the property (Locality, Postcode, Province)
- Binary variables : Where the variable is simply a True/False. (e.g: Is there a pool in the house)

Questions:

- Which variable is the target ? The price is the key element in our analysis as we had to predict prices we had to analysis its variation depending on the different variables
- How many rows and columns ? 23807 rows and 22 Columns
- What is the correlation between variable/target ? (Why?) There is a minor correlation between the target and variables. We see two main variables having a higher correlation : Rooms Number & Area
- What is the correlation between the variables/variables ? (Why?) In general, we can observe that the correlation between variables is really low.
- Which variables have the greatest influence on the target ? Number of rooms
- Which variables have the least influence on the target ? Terace area
- How many qualitative and quantitative variable is there ? How would you transform these values into numerical values ?

- Percentage of missing values per column ?

  - area :				19%
  - open_fire :			4%
  - terrace :				7%
  - terrace_area :		7%
  - garden :				6%
  - garden_area :			25%
  - land_surface :		29%
  - land_plot_surface :	13%
  - facades_number :		8%
  - swimming_pool_has :	4%
  - building_state :		43%

### 3. Data Interpretation

We have looked in:
- The 5 most expensive properties by average prices for each postcode
- The 5 least expensive properties by average prices for each postcode
- The average price by province
- The average price /m² by province
- The average price /m² by region
- The average price by each types for each provinces
- The count distribution of selling properties for each provinces
- The distribution of sellig properties by region
- The avrage price of houses and apartments by province
- Total number of selling houses and apartments by province
- The avrage price of houses and apartments by region
- Total number of selling houses and apartments by region



### 4. AI Modeling

As we have try to understand what conditions are effective on the prices of properties we suggest a sort of combination of Decision Making Tree and Linear Regression models. We eliminated the conditions like number of rooms, terace and garden existance, province and the type of the property of the inputs with DMT modeling. After that, the LRM is suitable to see the relationships between the area and price. For other relationships between different components of the inputs should examine independently. Other AI models would suitable for them.

### Used Libraries
- import pandas as pd
- import numpy as np
- import matplotlib.pyplot as plt
- from collections import Counter
- %matplotlib inline
- import seaborn as sns


