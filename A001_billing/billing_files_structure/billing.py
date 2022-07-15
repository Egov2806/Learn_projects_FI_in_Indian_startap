
# import libraries
import pandas as pd
import os
import matplotlib.pyplot as plt

# paths to files and folders
# TODO: перенести все рабочие файлы в папку datasets
folder_path='C:\\Users\\AlexanderMuntyanu\\Desktop\\ДатаФрейм Индийские Стартапы'
file_path="C:\\Users\\AlexanderMuntyanu\\Desktop\\ДатаФрейм Индийские Стартапы\\Indian Startups - Funding  Investors Data February 2022.csv"

# reading files to dataframe
startups_data = pd.DataFrame()

for file in os.listdir(folder_path):
    full_path = folder_path+"\\"+str(file)
    df = pd.read_csv(full_path, encoding='unicode_escape')
    startups_data = startups_data.append(df)

# TODO: find PyCharm short cuts and start learning them and USING!

# next analyse startups_data instead of individual files and dataframes

print(df.head(5))
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.Sector.value_counts().head(10))
print(df.Location.value_counts().head(10))

# build pie-charts showing ...
df['Sector'].value_counts().head(10).plot(kind ='pie', figsize = (6,6))
plt.show()