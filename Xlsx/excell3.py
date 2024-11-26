from openpyxl import Workbook

workbook=Workbook()

print(workbook.active.title)   #Returns by defoult active sheet
print(workbook.sheetnames)

workbook['Sheet'].title='CartDetails2'
sheet1=workbook.active

sheet1['A1'].value='Product Id '
sheet1['B1'].value='Product name '
sheet1['C1'].value='Product Price '

sheet1['A2'].value=1 
sheet1['B2'].value='OnePlus12R '
sheet1['C2'].value=40000.00 

sheet1['A3'].value=2 
sheet1['B3'].value='Nothing Phone 2'
sheet1['C3'].value=39999.00 

sheet1['A4'].value=3 
sheet1['B4'].value='Apple Iphone 15 pro'
sheet1['C4'].value=145000.00

# workbook.save('Phone.xlsx')   ##will be local file

workbook.save('C:\\Users\\AJAY KUMAR TIWARI\\OneDrive\\Desktop\\Phone1.xlsx')
print("File Created Successfully......!")

# [Note: We have to add"\\" in the middle of all the junctions to avoid path exceptions]


