import xlrd
def readData(test):
    file_location = "in/test"+str(test)+"/Data.xlsx"
    wb = xlrd.open_workbook(file_location)
    sheet = wb.sheet_by_index(0)
    return (int(sheet.cell_value(0,0)),int(sheet.cell_value(1,0)))
def readVendor(test,M,Hv,Price): 
    file_location = "in/test"+str(test)+"/Vendor.xlsx"
    wb = xlrd.open_workbook(file_location)
    sheet = wb.sheet_by_index(0)
    for i in range(1,M+1):
        Hv.append(sheet.cell_value(1, i))
    for i in range(1,M+1):
        Price.append(sheet.cell_value(2, i))
    Av = sheet.cell_value(3, 1)
    return Av
def readBuyer(test,M,j,a,b,ymin,ymax,Hb):
    file_location = "in/test"+str(test)+"/Buyer"+str(j)+".xlsx"
    wb = xlrd.open_workbook(file_location)
    sheet = wb.sheet_by_index(0)
    for i in range(1,M+1):
        a.append(sheet.cell_value(1, i))
    for i in range(1,M+1):
        b.append(sheet.cell_value(2, i))
    for i in range(1,M+1):
        ymin.append(int(sheet.cell_value(3, i)))
    for i in range(1,M+1):
        ymax.append(int(sheet.cell_value(4, i)))
    for i in range(1,M+1):
        Hb.append(sheet.cell_value(5, i))

    Ab= sheet.cell_value(6, 1)
    return Ab
    