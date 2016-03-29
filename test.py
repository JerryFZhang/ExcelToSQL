import pandas
xl = pandas.ExcelFile('data.xls')

names = xl.sheet_names  # see all sheet names
file_names  = []
for item in names:
    file_names.append(item)
