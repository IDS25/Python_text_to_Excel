#step one: Open and read file 'file01.txt'

import openpyxl as op

read_this = open('file01.txt', 'r')
content = read_this.read()

print(content)

#step 2: write content variable to excel file

excel_file = "test3.xlsx"

wb = op.load_workbook(excel_file)

sh = wb.active

cell_a1 = sh.cell(row=1,column=1)

cell_a1.value = content

print(cell_a1.value)

wb.save(excel_file)
read_this.close()

