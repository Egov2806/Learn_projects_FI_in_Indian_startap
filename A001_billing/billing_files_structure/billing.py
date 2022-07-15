
# import libraries
import pandas as pd
import os
import matplotlib.pyplot as plt

# paths to files and folders
# TODO: перенести все рабочие файлы в папку datasets
folder_path="C:\\Users\\AlexanderMuntyanu\\PycharmProjects\\Learn_projects_FI_in_Indian_startap\\A001_billing\\dataset"

# reading files to dataframe
startups_data = pd.DataFrame()
for file in os.listdir(folder_path):
    full_path = folder_path+"\\"+str(file)
    df = pd.read_csv(full_path, encoding='unicode_escape')
    startups_data = startups_data.append(df)

# TODO: find PyCharm short cuts and start learning them and USING!

# next analyse startups_data instead of individual files and dataframes
# print(startups_data.head(5))
# print(startups_data.shape)
# print(startups_data.info())

#caculate count null value in data frame
count_null=pd.DataFrame(startups_data.isnull().sum())
#unique count for collumn
cv_sector=pd.DataFrame(startups_data.Sector.value_counts().head())
cv_location=pd.DataFrame(startups_data.Location.value_counts().head())
discribe_data=pd.DataFrame(startups_data.Amount.describe())
#save analyse date in new excel file and new sheet
writer=pd.ExcelWriter('example.xlsx', engine='xlsxwriter')
count_null.to_excel(writer, 'count_null')
cv_sector.to_excel(writer, 'counts_value_col_sector')
cv_location.to_excel(writer, 'counts_value_location')
discribe_data.to_excel(writer, 'discribe data')
writer.save()

# build pie-charts showing ...
# df['Sector'].value_counts().head(10).plot(kind ='pie', figsize = (6,6))
# plt.show()
