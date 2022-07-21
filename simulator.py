PC = 0
dic = {}
f = open("input.txt.txt","r")
data = f.readlines()
count = 0
dicreg = {"000" : 0,
       "001" : 0,
        "010": 0,
        "011": 0,
        "100": 0,
        "101": 0,
        "110": 0,
        "111": 0,}

A=["10000","10001","10110","11010","11011","11100"]
B=["10010","11001"]
C=["10011","10111","11101","11110"]
D=["10100","10101"]
E=["11111","01100","01101","01111"]

def typeA(cmd):
    if(cmd[:5]=="10000"):
        r1 = 
    pass

def typeB(cmd):
    pass

def typeC(cmd):
    pass

def typeD(cmd):
    pass

def typeE(cmd):
    pass



for lines in data:
    dic[count] = lines
    count +=1

while(dic[PC][:5]!="01010"):
    if(dic[PC][:5] in A):
        typeA(dic[PC])
    elif(dic[PC][:5] in B):
        typeB(dic[PC])
    
    elif(dic[PC][:5] in C):
        typeC(dic[PC])

    elif(dic[PC][:5] in D):
        typeD(dic[PC])
    elif(dic[PC][:5] in E):
        typeE(dic[PC])