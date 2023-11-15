import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # standard
import csv
import seaborn as sns
from  itertools import groupby

stress = pd.read_csv("StressLevelDataset.csv")
stress['academic_performance'].describe()
stress

# Assuming you have a pandas DataFrame called 'data' with a column 'academic_performance'
x_values = stress.groupby('academic_performance').size().index
y_values = stress.groupby('academic_performance').size()

# Create a bar plot
plt.bar(x_values, y_values, color='blue')

# Set labels and title
plt.xlabel('Academic Performance')
plt.ylabel('Count')
plt.title('Count of Academic Performance')

# Display the plot
plt.show()


#Creating a group by for average academic preformance for the filtered data
summary_data = stress.groupby('anxiety_level')['academic_performance'].mean().reset_index()


plt.figure(figsize=(8, 6))
#making a bar chart to show the data in a presentation
plt.plot(summary_data['anxiety_level'], summary_data['academic_performance'], color='red')

plt.title("Bar Plot of Average Academic Performance by Anxiety_level")
plt.xlabel("anxeity level fitler out with high depression")
plt.ylabel("Mean Academic Performance")

plt.show()

#Creating a filter for depresion
summary_data = stress[stress["depression"] > 19]
#Creating a group by for average academic preformance for the filtered data
summary_data = stress.groupby('anxiety_level')['academic_performance'].mean().reset_index()


plt.figure(figsize=(8, 6))
#making a bar chart to show the data in a presentation
plt.plot(summary_data['anxiety_level'], summary_data['academic_performance'], color='red')

plt.title("Bar Plot of Average Academic Performance by Anxiety_level")
plt.xlabel("anxeity level fitler out with high depression")
plt.ylabel("Mean Academic Performance")

plt.show()


#Creating a filter for depresion
summary_data = stress[stress["depression"] > 19]
#Creating a second filter for anxiety level 
summary_data = summary_data[summary_data["anxiety_level"] > 19]
#Creating a group by for self esteem level average academic preformance for the filtered data
summary_data = stress.groupby('self_esteem')['academic_performance'].mean().reset_index()


plt.figure(figsize=(8, 6))
#making a bar chart to show the data in a presentation
plt.plot(summary_data['self_esteem'], summary_data['academic_performance'], color='red')

plt.title("Bar Plot of Average Academic Performance by self esteem")
plt.xlabel("Self esteem fitler out with high depression and anxiety")
plt.ylabel("Mean Academic Performance")

plt.show()

#Creating a filter for sleep quality
summary_data = stress[stress["sleep_quality"] < 3]
#Creating a second filter for anxiety level 
summary_data = summary_data[summary_data["anxiety_level"] > 19]
#Creating a group by for self esteem level average academic preformance for the filtered data
summary_data = stress.groupby('self_esteem')['academic_performance'].mean().reset_index()


plt.figure(figsize=(8, 6))
#making a bar chart to show the data in a presentation
plt.plot(summary_data['self_esteem'], summary_data['academic_performance'], color='red')

plt.title("Bar Plot of Average Academic Performance by self esteem")
plt.xlabel("Self esteem fitler out with high sleep quality and anxiety")
plt.ylabel("Mean Academic Performance")

plt.show()

#creating a list of all correlations of academic performance
stress.corr()['academic_performance']

#Creating a filter for sleep quality
summary_data = stress[stress["sleep_quality"] > 3]
#Creating a second filter for anxiety level 
summary_data = summary_data[summary_data["basic_needs"] > 3]
#Creating a group by for self esteem level average academic preformance for the filtered data
summary_data = stress.groupby('self_esteem')['academic_performance'].mean().reset_index()


plt.figure(figsize=(8, 6))
#making a bar chart to show the data in a presentation
plt.plot(summary_data['self_esteem'], summary_data['academic_performance'], color='red')

plt.title("Bar Plot of Average Academic Performance by self esteem")
plt.xlabel("Self esteem fitler out with high sleep quality and basic needs")
plt.ylabel("Mean Academic Performance")

plt.show()

summary_data = stress.groupby(['depression', 'mental_health_history'])['academic_performance'].mean().reset_index()

# Create a scatter plot
plt.figure(figsize=(8, 6))
sns.lmplot(data=summary_data, x='depression', y='academic_performance', hue='mental_health_history', palette='Dark2')
plt.title("Scatter Plot of Average Academic Performance by depression")
plt.xlabel("depression")
plt.ylabel("Mean Academic Performance")
plt.show()

summary_data = stress.groupby(['anxiety_level', 'mental_health_history'])['academic_performance'].mean().reset_index()

# Create a scatter plot
plt.figure(figsize=(8, 6))
sns.lmplot(data=summary_data, x='anxiety_level', y='academic_performance', hue='mental_health_history', palette='Dark2')
plt.title("Scatter Plot of Average Academic Performance by depression")
plt.xlabel("depression")
plt.ylabel("Mean Academic Performance")
plt.show()

#Creating a filter for sleep quality
summary_data = stress[stress["sleep_quality"] < 2]

summary_data = summary_data.groupby(['anxiety_level', 'mental_health_history'])['academic_performance'].mean().reset_index()

# Create a scatter plot
plt.figure(figsize=(8, 6))
sns.lmplot(data=summary_data, x='anxiety_level', y='academic_performance', hue='mental_health_history', palette='Dark2')
plt.title("Scatter Plot of Average Academic Performance by depression")
plt.xlabel("depression")
plt.ylabel("Mean Academic Performance")
plt.show()

# Assuming 'mental_health_history' is a column in your dataframe
mental_health_counts = stress['mental_health_history'].value_counts()

plt.figure(figsize=(8, 6))

plt.bar(mental_health_counts.index, mental_health_counts, color='blue')

plt.title("Count of Mental Health History")
plt.xlabel("Mental Health History")
plt.ylabel("Count")

plt.show()

stress_counts = stress['stress_level'].value_counts()

plt.figure(figsize=(8, 6))

plt.bar(stress_counts.index, stress_counts, color='blue')

plt.title("Count of Stress Levels")
plt.xlabel("Stress Levels")
plt.ylabel("Count")

plt.show()

# Assuming you have a pandas DataFrame called 'data' with a column 'academic_performance'
x_values = stress.groupby('basic_needs').size().index
y_values = stress.groupby('basic_needs').size()

# Create a bar plot
plt.bar(x_values, y_values, color='blue')

# Set labels and title
plt.xlabel('Academic Performance')
plt.ylabel('Count')
plt.title('Count of Basic Needs')

# Display the plot
plt.show()

