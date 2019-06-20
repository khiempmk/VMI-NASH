import readExcel
import writeExcel
import random
import math
C_NPOP = 400 #sl NST
C_MAXGENS = 250#sl thế hệ
C_PXOVER = 0.8 #xác suất lai ghép
C_PMUTATION = 0.3 ##xác suất đột biến
W = 0.8
C1 = 0.1
C2 = 0.1
C_START = 10
C_TEST = 12
print("Run test in range (C_CTART,C_TEST) with:")
print("C_START = ")
C_START = int(input())
print("C_TEST = ")
C_TEST = int(input())

class NSTProfit():
    def __init__(self, profit,vt):
        self.profit = profit
        self.vt = vt
#--------danh gia do thich nghi------------
def TRC(y):
    tong = 0
    for i in range(M):
         tong = tong + H[i]*y[i]
    T = math.sqrt(2*A/tong)
    return A/T + tong*T/2
def evaluate(y): 
    Pc=0
    t = TRC(y)
    for i in range(M):
        Pc = Pc + a[i]*y[i]-b[i]*y[i]*y[i] - TRC(y) - Price[i]*y[i] 
    return Pc
#---------Them NST ----------------------
def addNST(y):
    gen.append(y) 
    genProfit.append(NSTProfit(evaluate(y),len(gen)-1))
    return
#---------khoi tao-----------------------   
def initialize(): 
    for vt in range(C_NPOP):
        y = []
        for i in range(M):
            y.append(random.randint(ymin[i], ymax[i]))
        addNST(y)
    return C_NPOP
#---------chon thế hệ tiếp theo ----------------
def updateBest():
    global  Gkbest
    global  Pkbest
    global Pbest
    global Gbest
    for ii in range(C_NPOP):
        if (genProfit[ii].profit > Pkbest):
            Pkbest = genProfit[ii].profit
            Pbest = gen[ii]
    if (Pkbest > Gkbest):
        Gkbest = Pkbest
        Gbest = Pbest
def updateV():
    for i in range(C_NPOP):
        for j in range(M):
            rand1 =random.random()
            rand2 =random.random()
            v[i][j] = W * v[i][j] +C1 * rand1 * (Pbest[j] - gen[i][j]) + C2 *rand2 *(Gbest[j] - gen[i][j])
def updateX():
    for i in range(C_NPOP):
        for j in range(M):
            if gen[i][j] + v[i][j] > ymax[j] :
                v[i][j]   = ymax[j] - gen[i][j]
                gen[i][j] = ymax[j]
            elif gen[i][j] +v[i][j] < ymin[j] :
                v[i][j] = ymin[j] - gen[i][j]
                gen[i][j] = ymin[j]
            else:
                gen[i][j] = int(gen[i][j] + v[i][j])
        genProfit[i].profit =  evaluate(gen[i])

def PSO():
    print("da dung PSO cua buyer",j,"voi", M, "product")
    for ip in range(C_MAXGENS):
        Pkbest =  -1000000000;
        updateBest()
        updateV()
        updateX()
    print(Gkbest)
    return (Gkbest)
#------------------MAIN----------------------------.
#------------------MAIN-----------------------------
for test in range(C_START,C_TEST):
    file = open("out/PSO.txt","a+")
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
        v = [[0 for row in range(0, M+1)] for col in range(0, C_NPOP+1)]
        Gkbest = -1000000000
        Pkbest = -1000000000
        Gbest = []
        Pbest = []
        Ab = readExcel.readBuyer(test,M,j,a,b,ymin,ymax,Hb)
        for i in range(M):
            ymax[i]=int(min(ymax[i],a[i]/b[i]))
            H[i]=Hb[i]+Hv[i];
        A=Ab+Av
        gen=[]
        genProfit=[]
        initialize()
        supplyProfit += PSO()
    print("Supply chain optimal profit =", supplyProfit)
    file.write("Test "+str(test)+"\t"+str(round(supplyProfit,2))+"\n")
    file.close()