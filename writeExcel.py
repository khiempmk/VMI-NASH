import xlsxwriter
import os
def writeBuyer(test,j,y,Pc):
    folder = "out/test"+str(test)
    if not os.path.exists(folder):
        os.mkdir(folder) 
    wb = xlsxwriter.Workbook(folder+"/"+str(j)+".xlsx")
    ws = wb.add_worksheet('Sheet1')
    for i in range(len(y)):
        ws.write(i,0,y[i])
    ws.write(len(y),0,Pc)
    wb.close()
