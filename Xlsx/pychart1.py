
import xlsxwriter


workbook = xlsxwriter.Workbook('chart_pie22.xlsx')


worksheet = workbook.add_worksheet()


bold = workbook.add_format({'bold': 1})

# create a data list .
headings = ['Category', 'Values']

data = [
	['Apple', 'Cherry', 'Pecan'],
	[60, 30, 10],
]


worksheet.write_row('A1', headings, bold)

worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])


chart1 = workbook.add_chart({'type': 'pie'})

# Add a data series to a chart
# using add_series method.
# Configure the first series.
# [sheetname, first_row, first_col, last_row, last_col]

chart1.add_series({
	'name':	 'Pie sales data',
	'categories': ['Sheet1', 1, 0, 3, 0],   #[1strow,1stcolumn,lrow,lcolumn]
	'values':	 ['Sheet1', 1, 1, 3, 1],
})


chart1.set_title({'name': 'Popular Pie Types'})

# Set an Excel chart style. Colors with white outline and shadow.

chart1.set_style(15)

# Insert the chart into the worksheet(with an offset).
# the top-left corner of a chart is anchored to cell C2.

worksheet.insert_chart('C2', chart1, {'x_offset': 25, 'y_offset': 10})


workbook.close()
