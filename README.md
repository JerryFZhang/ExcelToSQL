# ExcelToSQL
This a program written in python that take an xls file as a input, generate csv code for each sheet stored, and generate SQL insertion code.
Some of the cool features including 

- checking if the file exist or not and then create or wipe the file if necessary
- check the datatype and parse string and int differently

# How to use
- There are three ways to download the file:
  1. Download the repo as a zip.
  2. Download the <code>run.py</code> file only.
  3. Or clone the repo by typing the following command into your terminal:


```  
git clone https://github.com/zhang96/ExcelToSQL
```
Install the require modules including: 

- xlrd
- pandas

Put the spreadsheet file in the folder and name it as data.xls, make sure it ends with xls not xlsx.

- There are two ways to run the file:
  1. Run the file IDLE or other IDEs.
  2. Set the directory in the terminal and then type the following command into the terminal
```
python run.py
```
#Author
zhang96

#License
MIT, see LICENSE.txt.
