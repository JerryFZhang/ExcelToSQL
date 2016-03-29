import csv,os,xlrd,pandas
def sheets_names():
    xl = pandas.ExcelFile(excel)
    names = xl.sheet_names
    for item in names:
        file_names.append(item)
    print 'Sheets names were being parsed'

def csv_from_excel():
    wb = xlrd.open_workbook(excel)
    for item in file_names:
        file_names_str = str(item)
        sh = wb.sheet_by_name(file_names_str)
        current_csv = open(file_names_str+'.csv', 'wb')
        wr = csv.writer(current_csv, quoting = csv.QUOTE_ALL)

        for rownum in xrange(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        current_csv.close()
    print 'CSV files were created.'

def check_int(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def listToStringWithoutBrackets(list1):
    return str(list1).replace('[','').replace(']','')

def populate():
    # File should be first emptied before inserting sql code.
    open(item_name+'.sql', 'w').close()
    print'File %s.sql is empty.' % item_name

    output_file = open(item_name + '.sql', 'w')
    next(input_file)
    reader = csv.reader(input_file,delimiter=',')
    for row in reader:
        temp = []
        for item in row:
            if check_int(item):
                temp.append(int(float(item)))
            else:
                temp.append(str(item))
        output_file.write( 'INSERT INTO  %s \nVALUES (%s);\n' %(item_name,listToStringWithoutBrackets(temp)))
    print'File %s.sql is populated.' % item_name

excel = 'data.xls'
file_names  = []

sheets_names()
csv_from_excel()
for item in file_names:
    item_name = str(item)
    with open(item_name + '.csv', 'rb') as input_file:
        if not os.path.isfile(item_name + '.sql'):
            populate()
        else:
            if not os.stat(item_name+'.sql').st_size == 0:
                input = (raw_input('There is some data in %s.sql, are you sure to delete your existing data in %s.sql? (y/n)' % (item_name,item_name)))
                if not input =='y' and not input == 'Y':
                    print 'Program teminated, user refuse to delete data in %s.sql' % item_name
                    break
                else:
                    populate()
            else:
                populate()
print '********Execution Complete********'
