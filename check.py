import readExcel
import writeExcel
import random
import math
print("Run test in range (C_CTART,C_TEST) with:")
print("C_START = ")
C_START = int(input())
print("C_TEST = ")
C_TEST = int(input())

#--------danh gia do thich nghi------------
def evaluate(y): 
    tong = 0;
    for i in range(M):
         tong = tong + H[i]*y[i]
    T = math.sqrt(2*A/tong)
    TRC = A/T + tong*T/2
    
    Pc=0
    for i in range(M):
        Pc = Pc + a[i]*y[i]-b[i]*y[i]*y[i] - TRC - Price[i]*y[i] 
    return Pc;
def process(i):
    if (i==M):
         return evaluate(y)
    y[i] = ymax[i]
    w = process(i+1)
    for r in range(ymin[i],ymax[i]):
        y[i] = r
        w = max(w,process(i+1))
    return w
#..................MAIN..............................
file = open("out/Check.txt","a+")
for test in range(C_START,C_TEST):
    print("PROCESS WITH TEST",test)
    # N: number of buyers M: number of product
    (N,M) = readExcel.readData(test)
    Hv=[]       
    Price=[]
    Av=readExcel.readVendor(test,M,Hv,Price)
    H=[i for i in range(M)]
    A=0
    supplyProfit = 0
    print("Co",N,"buyers va",M,"products")
    for j in range(N):
        a=[]
        b=[]
        ymin=[]
        ymax=[]
        Hb=[]
        Ab = readExcel.readBuyer(test,M,j,a,b,ymin,ymax,Hb)
        for i in range(M):
            x = a[i]/b[i]
            ymax[i]= int(min(ymax[i],x))
            H[i]=Hb[i]+Hv[i]
        A=Ab+Av
        y = [0 for i in range(M)]
        print("Do with Buyer",j)
        Pc=process(0)
        print(Pc)
        supplyProfit +=Pc
    print("Supply chain optimal profit =", supplyProfit)
    file.write("Test "+str(test)+"\t"+str(round(supplyProfit,2))+"\n")
file.close()