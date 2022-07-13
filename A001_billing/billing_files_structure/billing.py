import pandas as pd
import os
import matplotlib.pyplot as plt
folder_path='C:\\Users\\AlexanderMuntyanu\\Desktop\\ДатаФрейм Индийские Стартапы'
file_path="C:\\Users\\AlexanderMuntyanu\\Desktop\\ДатаФрейм Индийские Стартапы\\Indian Startups - Funding  Investors Data February 2022.csv"
for file in os.listdir(folder_path):
    full_path=folder_path+"\\"+str(file)
    df=pd.read_csv(full_path, encoding='unicode_escape')
    #print(df.head(5))
    print(df.shape)
    #print(df.info())
    #print(df.isnull().sum())
    #print(df.Sector.value_counts().head(10))
    #print(df.Location.value_counts().head(10))
    #print(df['Sector'].value_counts().head(10).plot(kind ='pie', figsize = (6,6)))