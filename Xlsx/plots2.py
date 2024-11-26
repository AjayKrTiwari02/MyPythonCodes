import xlsxwriter
wb = xlsxwriter.Workbook('plot4.xlsx')
worksheet = wb.add_worksheet()
chart1 = wb.add_chart({'type': 'column'})

# Add the worksheet data that the charts will refer to.
headings = ['Name', 'Phy', 'Maths']
data = [
   ["Jay",   30, 60],
   ["Mohan", 40, 50],
   ["Veeru", 60, 70],
]

worksheet.write_row(0,0, headings)
worksheet.write_row(1,0, data[0])
worksheet.write_row(2,0, data[1])
worksheet.write_row(3,0, data[2])

chart1.add_series({
   'name': '=Sheet1!$B$1',
   'categories': '=Sheet1!$A$2:$A$4',
   'values': '=Sheet1!$B$2:$B$4',
})

chart1.add_series({                   ####Use matrix concept
   'name': ['Sheet1', 0, 2],
   'categories': ['Sheet1', 1, 0, 3, 0],
   'values': ['Sheet1', 1, 2, 3, 2],
})

worksheet.insert_chart('B7', chart1)

wb.close()