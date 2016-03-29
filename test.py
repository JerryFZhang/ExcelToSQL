import pandas as pd
xl = pd.ExcelFile('data.xls')

xl.sheet_names  # see all sheet names

xl.parse(sheet_name)
print sheet_name
