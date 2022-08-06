import sys
from matplotlib import pyplot as plt
def bin8Convert (n):
    return '{0:08b}'.format(n)

def bin16Convert(n):
    return '{0:016b}'.format(n)


def printing(PC,dicreg):
    print(bin8Convert(PC),end=' ')
    for i in dicreg.values():
        print(bin16Convert(bin_dec(i)),end=' ')
    print()

def flag_reset(dicreg):
    dicreg["111"] = "0000000000000000"

def bin_dec(s):
    return int(s,2)

def typeA(cmd,PC,dicreg):
    if(cmd[:5]=="10000"): #------------------Addition----------------
        if(bin_dec(dicreg[cmd[7:10]]) + bin_dec(dicreg[cmd[10:13]])<65536): #-------------- checking condition for overflow------------ 
            a = bin_dec(dicreg[cmd[7:10]])
            b = bin_dec(dicreg[cmd[10:13]])
            dicreg[cmd[13:]] = bin16Convert(a + b)
            printing(PC,dicreg)
            flag_reset(dicreg)
            PC+=1
            return PC
        else:       # what to do when overflow occur
            dicreg[cmd[13:]] = bin16Convert(65535)
            dicreg["111"] = "0000000000001000"
            printing(PC,dicreg)
            flag_reset(dicreg)
            PC+=1
            return PC

    elif(cmd[:5]=="10001"): #-----------------subtraction-----------------------------
        if(bin_dec(dicreg[cmd[7:10]])<=bin_dec(dicreg[cmd[10:13]])):
            dicreg[cmd[13:]] = "0000000000000000"
            printing(PC,dicreg)
            flag_reset(dicreg)
            PC+=1
            return PC

        elif(bin_dec(dicreg[cmd[7:10]])-bin_dec(dicreg[cmd[10:13]])>0):
            dicreg[cmd[13:]] = bin16Convert(bin_dec(dicreg[cmd[7:10]])-bin_dec(dicreg[cmd[10:13]]))
            printing(PC,dicreg)
            flag_reset(dicreg)
            PC+=1
            return PC

        else:
            #--------------------------TO BE REVIEWED________________________
            dicreg[cmd[13:]] = "0000000000000000"
            dicreg["111"] = "0000000000001000"
            printing(PC,dicreg) #-------------when underflow occur
            flag_reset(dicreg)
            PC+=1
            return PC
    
    elif(cmd[:5]=="10110"): #-----------------Multiply------------
        if(bin_dec(dicreg[cmd[7:10]]) * bin_dec(dicreg[cmd[10:13]])<65536):
            dicreg[cmd[13:]] = bin16Convert(bin_dec(dicreg[cmd[7:10]]) * bin_dec(dicreg[cmd[10:13]]))
            printing(PC,dicreg)
            flag_reset(dicreg)
            PC+=1
            return PC

        else:
            dicreg[cmd[13:]] = "1111111111111111"
            dicreg["111"] = "0000000000001000"   #------------what to do when overflow occur
            printing(PC,dicreg)
            flag_reset(dicreg)
            PC+=1
            return PC

    elif(cmd[:5]=="11010"): #-----------Exclusive XOR----------------I think mistake in calculation--
        dicreg[cmd[13:]] = bin16Convert(bin_dec(dicreg[cmd[7:10]]) ^ bin_dec(dicreg[cmd[10:13]]))
        printing(PC,dicreg)
        PC+=1
        flag_reset(dicreg)
        return PC

    elif(cmd[:5]=="11011"): #---------------OR#--------------------------
        dicreg[cmd[13:]] = bin16Convert(bin_dec(dicreg[cmd[7:10]]) | bin_dec(dicreg[cmd[10:13]]))
        printing(PC,dicreg)
        PC+=1
        flag_reset(dicreg)
        return PC

    elif(cmd[:5]=="11100"):#--------------------------AND#--------------------------
        dicreg[cmd[13:]] = bin16Convert(bin_dec(dicreg[cmd[7:10]]) & bin_dec(dicreg[cmd[10:13]]))
        printing(PC,dicreg)
        flag_reset(dicreg)
        PC+=1
        return PC


def typeB(cmd,PC,dicreg):
    if(cmd[:5]=="10010"):#--------------------------Move immediate#--------------------------
        dicreg[cmd[5:8]] = bin16Convert(bin_dec(cmd[8:]))
        printing(PC,dicreg)
        flag_reset(dicreg)
        PC+=1
        return PC
    
    elif(cmd[:5]=="11001"):#--------------------------left shift#--------------------------
        if(bin_dec((dicreg[cmd[5:8]])) << bin_dec((dicreg[cmd[8:]]))<65536):
            dicreg[cmd[5:8]] = bin16Convert(bin_dec(dicreg[cmd[5:8]]) << bin_dec(dicreg[cmd[8:]]))
            printing(PC,dicreg)
            flag_reset(dicreg)
            PC+=1
            return PC


def typeC(cmd,PC,dicreg):
    if(cmd[:5]=="10011"):#--------------------------Move register#--------------------------
        dicreg[cmd[13:]] = dicreg[cmd[10:13]]
        printing(PC,dicreg)
        flag_reset(dicreg)
        PC+=1
        return PC

    elif(cmd[:5]=="10111"):#--------------------------Divide#--------------------------
        dicreg["000"] = bin16Convert(bin_dec(dicreg[cmd[10:13]])//bin_dec(dicreg[cmd[13:]])) #------check division format----------
        dicreg["001"] = bin16Convert(bin_dec(dicreg[cmd[10:13]]) % bin_dec(dicreg[cmd[13:]]))
        printing(PC,dicreg)
        flag_reset(dicreg)
        PC+=1
        return PC

    elif(cmd[:5]=="11101"):#--------------------------NOT#--------------------------
        dicreg[cmd[13:]] = bin16Convert(~(bin_dec(dicreg[cmd[10:13]])))
        printing(PC,dicreg)
        flag_reset(dicreg)
        PC+=1
        return PC

    elif(cmd[:5]=="11110"):#--------------------------CMP#--------------------------
        a = bin_dec(dicreg[cmd[13:]])
        b = bin_dec(dicreg[cmd[10:13]])
        if(a>b):
            dicreg["111"] = "0000000000000100" #----------------------Flag setting remaining-------------------
            printing(PC,dicreg)
            PC+=1
            return PC

        elif(a<b):
            dicreg["111"] = "0000000000000010"
            printing(PC,dicreg)
            PC+=1
            return PC

        elif(a==b):
            dicreg["111"] = "0000000000000001"
            printing(PC,dicreg)
            PC+=1
            return PC


def typeD(cmd,PC,dicreg,dic):
    if(cmd[:5]=="10100"):#--------------------------LOAD#--------------------------
        dicreg[cmd[5:8]] = bin16Convert(bin_dec(dic[bin_dec(cmd[8:])]))
        printing(PC,dicreg)
        flag_reset(dicreg)
        PC+=1
        return PC

    elif(cmd[:5]=="10101"):#--------------------------Store#--------------------------
        dic[bin_dec(cmd[8:])] = bin16Convert(bin_dec(dicreg[cmd[5:8]]))
        printing(PC,dicreg)
        flag_reset(dicreg)
        PC+=1
        return PC

def typeE(cmd,PC,dicreg):
    if(cmd[:5]=="11111"): #jmp
        PC = int(cmd[8:])
        return PC
    
    elif(cmd[:5]=="01100"): #jlt
        if(dicreg["111"]=="0000000000000100"):
            PC = int(cmd[8:],2)
            return PC
        else:
            PC+=1
            return PC
    
    elif(cmd[:5]=="01101"): #jgt
        if(dicreg["111"]=="0000000000000010"):
            PC = int(cmd[8:],2)
            return PC
        else:
            PC+=1
            return PC

    elif(cmd[:5]=="01111"): #je
        if(dicreg["111"]=="0000000000000001"):
            PC = int(cmd[8:],2)
            return PC
        else:
            PC+=1
            return PC


PC = 0
cycle = 0
dic = {}
x = []
y = []
inut = sys.stdin
# inut = open("input.txt", "r")
data = inut.read().split("\n")

count = 0
dicreg = {"000" : "0000000000000000",
       "001" : "0000000000000000",
        "010": "0000000000000000",
        "011": "0000000000000000",
        "100": "0000000000000000",
        "101": "0000000000000000",
        "110": "0000000000000000",
        "111": "0000000000000000"}

A=["10000","10001","10110","11010","11011","11100"]
B=["10010","11001"]
C=["10011","10111","11101","11110"]
D=["10100","10101"]
E=["11111","01100","01101","01111"]

for i in range(0,256):
    dic[i] = "0000000000000000"

for lines in data:
    if(lines!=''):
        dic[count] = lines
        # print(lines)
        count +=1
# print(dic)
# for i in dic.keys():
#     print(dic[i])

while(dic[PC][:5]!="01010"):
    x.append(cycle)
    y.append(PC)
    if(dic[PC][:5] in A):
        PC = typeA(dic[PC],PC,dicreg)
    
    elif(dic[PC][:5] in B):
        PC = typeB(dic[PC],PC,dicreg)
    
    elif(dic[PC][:5] in C):
        PC = typeC(dic[PC],PC,dicreg)

    elif(dic[PC][:5] in D):
        x.append(cycle)
        y.append(int(dic[PC][8:],2))
        PC = typeD(dic[PC],PC,dicreg,dic)
    
    elif(dic[PC][:5] in E):
        PC = typeE(dic[PC],PC,dicreg)
    cycle+=1
printing(PC,dicreg)
for i in dic.keys():
    print(dic[i])
x.append(cycle)
y.append(PC)

plt.scatter(x,y)
plt.xlabel("Cycle")
plt.ylabel("Memory")
plt.show()
