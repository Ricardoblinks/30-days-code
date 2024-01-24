#import libraries needed basically pandas
import pandas as pd

# pass your data to a variable
"""
note 
if you have the raw file obj, just use the pandas.dataframe function on it so you can be able to manipulate it with pandas
else
if your data is stored in a csv file use .read_csv
if stored in an excel file use .excel 
in general check if padas can read your file extension by basically typing pandas.read_ then check if the extension is available

the above was tested with vs code
"""
data = pd.read_csv("day_3-data_processing\\taxreturn.csv")

# for information about the data
info = data.info()
print(info)

# to handle missing data or values 
fixed_missing = data.dropna()
print(fixed_missing)

# to remove all duplicates 
remove_duplicate = data.drop_duplicates()
print(remove_duplicate)

# to delete a particular column
"""
get the exact name of the column, and paste it at the columns array. If you want to delete more just indicate it there
"""
delete_column = data.drop(columns=['TaxPayerid'], axis=0)
print(delete_column)

# to describe the data you want to manipulate

"""
note that this function will indicate to you the dependent and also get you the 
count, mean, std, min, percentages, and max of your data
""" 
describe = data.describe()
print(describe)


