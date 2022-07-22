def bin8Convert (n):
    return '{0:08b}'.format(n)

def bin16Convert(n):
    return '{0:016b}'.format(n)


def printing(PC,dicreg):
    print(bin8Convert(PC),end=' ')
    for i in dicreg.values():
        print(bin16Convert(i),end=' ')



def typeA(cmd,PC,dicreg):
    if(cmd[:5]=="10000"):
        if(dicreg[cmd[7:10]] + dicreg[cmd[10:13]]<65536): #-------------- checking condition for overflow 
            dicreg[cmd[13:]] = dicreg[cmd[7:10]] + dicreg[cmd[10:13]]
            printing(PC,dicreg)
        else:       # what to do when overflow occur
            pass

    elif(cmd[:5]=="10001"):
        if(dicreg[cmd[7:10]]<dicreg[cmd[10:13]]):
            dicreg[cmd[13:]] = 0
        elif(dicreg[cmd[7:10]]-dicreg[cmd[10:13]]<0):
            dicreg[cmd[13:]] = dicreg[cmd[7:10]] - dicreg[cmd[10:13]]
            printing(PC,dicreg)
        else:
                #------------ what to do when underflow occur
            pass
    
    elif(cmd[:5]=="10110"):
        if(dicreg[cmd[7:10]] * dicreg[cmd[10:13]]<65536):
            dicreg[cmd[13:]] = dicreg[cmd[7:10]] * dicreg[cmd[10:13]]
            printing(PC,dicreg)
        else:   #------------what to do when overflow occur
            pass 

    elif(cmd[:5]=="11010"):
        dicreg[cmd[13:]] = dicreg[cmd[7:10]] ^ dicreg[cmd[10:13]]
        printing(PC,dicreg)

    elif(cmd[:5]=="11011"):
        dicreg[cmd[13:]] = dicreg[cmd[7:10]] | dicreg[cmd[10:13]]
        printing(PC,dicreg)
    
    elif(cmd[:5]=="11100"):
        dicreg[cmd[13:]] = dicreg[cmd[7:10]] & dicreg[cmd[10:13]]
        printing(PC,dicreg)


def typeB(cmd,PC,dicreg):
    if(cmd[:5]=="10010"):
        dicreg[cmd[5:8]] = int(cmd[8:])
        printing(PC,dicreg)
    
    elif(cmd[:5]=="11001"):
        if(int(dicreg[cmd[5:8]] << int(dicreg[cmd[8:]]))<65536):
            dicreg[cmd[5:8]] = dicreg[cmd[5:8]] << int(dicreg[cmd[8:]])
            printing(PC,dicreg)


def typeC(cmd):
    if(cmd[:5]=="10011"):
        dicreg[cmd[13:]] = dicreg[cmd[10:13]]
        printing(PC,dicreg)

    elif(cmd[:5]=="10111"):
        dicreg["000"] = dicreg[cmd[10:13]]//dicreg[cmd[13:]]
        dicreg["001"] = dicreg[cmd[10:13]] % dicreg[cmd[13:]]
        printing(PC,dicreg)

    elif(cmd[:5]=="11101"):
        dicreg[cmd[13:]] = ~(dicreg[cmd[10:13]])
        printing(PC,dicreg)

    elif(cmd[:5]=="11110"):
        pass #----------------------Flag setting remaining-------------------

def typeD(cmd,PC,dicreg):
    pass

def typeE(cmd,PC,dicreg):
    pass


PC = 0
dic = {}
f = open("input.txt","r")
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




for lines in data:
    dic[count] = lines
    count +=1

while(dic[PC][:5]!="01010"):
    if(dic[PC][:5] in A):
        typeA(dic[PC],PC,dicreg)
    
    elif(dic[PC][:5] in B):
        typeB(dic[PC],PC,dicreg)
    
    elif(dic[PC][:5] in C):
        typeC(dic[PC],PC,dicreg)

    elif(dic[PC][:5] in D):
        typeD(dic[PC],PC,dicreg)
    
    elif(dic[PC][:5] in E):
        typeE(dic[PC],PC,dicreg)
    print("\n")
    PC+=1