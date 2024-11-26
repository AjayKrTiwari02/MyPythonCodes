
import xlsxwriter

workbook = xlsxwriter.Workbook('chart_Line67.xlsx')

worksheet = workbook.add_worksheet()
	

bold = workbook.add_format({'bold': 1})
	

headings = ['Number', 'Batch 1', 'Batch 2']
	
data = [
	[2, 3, 4, 5, 6, 7],
	[70, 65, 55, 60, 50, 40],
	[60, 50, 60, 20, 10, 20],
]
	

worksheet.write_row('A1', headings, bold)
	

worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])
	

chart1 = workbook.add_chart({'type': 'line'})
	
	
# Configure the first series.
# = Sheet1 !$A$1 is equivalent to ['Sheet1', 0, 0].

# note : spaces is not inserted in b / w
# = and Sheet1, Sheet1 and !
# if space is inserted it throws warning.

chart1.add_series({
	'name':	 '= Sheet1 !$B$1',
	'categories': '= Sheet1 !$A$2:$A$7',
	'values':	 '= Sheet1 !$C$2:$C$7',
})
	
# Configure a second series.
# Note use of alternative syntax to define ranges.
# [sheetname, first_row, first_col, last_row, last_col].

chart1.add_series({
	'name':	 ['Sheet1', 0, 2],
	'categories': ['Sheet1', 1, 0, 6, 0],
	'values':	 ['Sheet1', 1, 2, 6, 2],
})
	

chart1.set_title ({'name': 'Results of data analysis'})
	

chart1.set_x_axis({'name': 'Test number'})
	

chart1.set_y_axis({'name': 'Data length (mm)'})
	

chart1.set_style(11)
	

worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
	

workbook.close()
