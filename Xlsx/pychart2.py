import xlsxwriter

wb = xlsxwriter.Workbook('Product20.xlsx')
worksheet = wb.add_worksheet()

headings = ['Category', 'Values']
data = [
   ['Q1', 'Q2', 'Q3', 'Q4'],
   [125, 60, 100, 80],
]
bold=wb.add_format({'bold':True})
worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])

chart1 = wb.add_chart({'type': 'pie'})
chart1.add_series({
   'name': 'Quarterly sales data',
   'categories': ['Sheet1', 1, 0, 4, 0],
   'values': ['Sheet1', 1, 1, 4, 1],
   'data_labels': {'percentage':True},
})
chart1.set_title({'name': 'Pie Chart of Quarterly Sales'})

worksheet.insert_chart('D2', chart1)
chart1.set_style(155)

wb.close()