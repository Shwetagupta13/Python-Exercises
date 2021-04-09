# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#%% TASK 1
import pandas as pd
#read the csv file using pd.read_csv
data = pd.read_csv("Destination.csv")
print("No.of rows and columns in Destination file is:")
print(data.shape)           

#%% TASK 2
#print observations from row 3 to 8
print("print observations from row 3 to 8:")
print(data.iloc[2:8])

#%% TASK 3
#Mean number of all inclusive hotels across all destinations
print("Mean number of all inclusive hotels across all destinations:")
print(data["No_of_all_inclusive_hotels"].mean())

#%% TASK 4
#lowest Scoring Destination
print("Lowest scoring destination is: ")
print(data[data['Feedback_Score'] == data["Feedback_Score"].min()]['Destination'])

#%% TASK 5
#Highest Scoring Destination
print("Highest scoring destination is: ")
print(data[data['Feedback_Score'] == data["Feedback_Score"].max()]['Destination'])

#%% TASK 6
#All the destinations where there are more than 9 all inclusive hotels.
highscore= data[data["No_of_all_inclusive_hotels"] > 9]
print(highscore)

#%% TASK 7
#Filter the data by destination and score above 8
print(data[data['Feedback_Score']>8][['Destination','Feedback_Score']])

#%% TASK 8
#Filter the data by destination and score below 2
print(data[data['Feedback_Score']<2][['Destination','Feedback_Score']])

#%% TASK 9
#Is there a correlation between number of all inclusive hotels and score?
correlation = data[['No_of_all_inclusive_hotels','Feedback_Score']].corr()
if(correlation['Feedback_Score'][0]>0.5):
    print(" Its a positive correlation")
elif (correlation['Feedback_Score'][0]> -0.5):
    print("There is no correlation")    
else:
    print("Its a negative correlation")    
    
#%% TASK 10
#Create a data visualisation diagram to show destination and highest scores?
import matplotlib.pyplot as plt
df = data[['Destination','Feedback_Score']]
df.index = data['Destination']
df.plot.bar(color = 'orange')
plt.xlabel('Destination', fontsize = 14)
plt.ylabel('Feedback score', fontsize = 14)
plt.title('Data Visualisation Diagram', fontsize = 18)