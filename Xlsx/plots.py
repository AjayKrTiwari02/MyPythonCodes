import xlsxwriter
wb = xlsxwriter.Workbook('plot3.xlsx')
worksheet = wb.add_worksheet()
chart = wb.add_chart({'type': 'column'})

data = [
   [10, 20, 30,  40,  50],
   [20, 40, 60,  80, 100],
   [30, 60, 90, 120, 150],
]
worksheet.write_column('A1', data[0])
worksheet.write_column('B1', data[1])
worksheet.write_column('C1', data[2])

chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
chart.add_series({'values': '=Sheet1!$C$1:$C$5'})

worksheet.insert_chart('B7', chart)

wb.close()