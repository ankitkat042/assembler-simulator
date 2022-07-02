from asyncio.windows_events import NULL

def checklen(cmd,type):
    if(type=='A'):
        if(len(cmd)!=4):
            print("Invalid length")
            return False
        else:
            return True
    
    elif(type=='B' or type=='C' or type=='D'):
        if(len(cmd)!=3):
            print("Invalid length")
            return False
        else:
            return True
    
    elif(type=='E'):
        if(len(cmd)!=2):
            print("Invalid length")
            return False
        else:
            return True
    
    elif(type=='F'):
        if(len(cmd)!=1):
            print("Invalid length")
            return False
        else:
            return True

def checking_typeA(cmd,dicisnt,dicreg,count):
    if(cmd[1] not in dicreg.keys() or cmd[2] not in dicreg.keys() or cmd[3] not in dicreg.keys()):
        print("Error in line :Invalid register")
        return False
    else:
        return True

def checking_typeB(cmd,dicinst,dicreg,count):
    if(cmd[1] not in dicreg.keys()):
        print("Invalid register")
        return False
    else:
        if(cmd[2][0]!='$'):
            print("Invalid Immediate syntax")
            return False
        else:
            if(0<=int(cmd[2][1:])<=255):
                return True
            else:
                print("Number out of range")
                return False

def checking_typeC(cmd,dicinst,dicreg,count):
    if(cmd[1] not in dicreg.keys() or cmd[2] not in dicreg.keys()):
        print("Invalid register")
        return False
    else:
        return True

def checking_typeD(cmd,dicinst,dicreg,dicvar,count):
    if(cmd[1] not in dicreg.keys()):
        print("Invalid register")
        return False
    else:
        if(cmd[2] not in dicvar.keys()):
            print("Invalid variable")
            return False
        else:
            return True

def checking_typeE(cmd,dicinst,dicreg,diclabel,count):
    if(cmd[1] not in diclabel.keys()):
        print("Invalid memory address")
        return False
    else:
        return True

def checking_typeF(cmd,dicinst,dicreg,diclabel,count):
    # if(cmd[1] not in diclabel.keys()):
    #     print("Invalid memory address")
    #     return False
    # else:
        return NULL

def checking(cmd,dicinst,dicreg,dicvar,diclabel,count):
    if(cmd[0] not in dicinst.keys()):
        print("Invalid Instruction")
        return False

    else:
        if(cmd[0]=='mov'):
            if(cmd[2][0].isalpha()):
                    typ = 'C'
            else:
                typ = 'B'
                
        else:
            typ = dicinst[cmd[0]][1]

        if(checklen(cmd,typ)):
            if(typ=='A'):
                result = checking_typeA(cmd,dicinst,dicreg,count)
                return result

            elif(typ=='B'):
                result = checking_typeB(cmd,dicinst,dicreg,count)
                return result

            elif(typ=='C'):
                result = checking_typeC(cmd,dicinst,dicreg,count)
                return result
            
            elif(typ=='D'):
                result = checking_typeD(cmd,dicinst,dicreg,dicvar,count)
                return result

            elif(typ=='E'):
                result = checking_typeE(cmd,dicinst,dicreg,diclabel,count)
                return result
            
            elif(typ=='F'):
                result = checking_typeF(cmd,dicinst,dicreg,count)
                return result
        else:
            return False



dicinst = {"add":['10000','A'],"sub":['10001','B'],"mov":['10010','B'],"mov":['10011','C'],"ld":['10100','D'],
"st":['10101','D'],"mul":['10110','A'],"div":['10111','C'],"rs":['11000','B'],"ls":['11001','B'],"xor":['11010','A'],
"or":['11011','A'],"and":['11100','A'],"not":['11101','C'],"cmp":['11110','C'],"jmp":['11111','E'],
"jlt":['01100','E'],"jgt":['01101','E'],"je":['01111','E'],"hlt":['01010']}

dicreg = {'R1': "000",'R2':"001",'R3':"010","R4":"100","R5":"101","R6":"110"}

dicvar = {'X':'00000011'}
diclabel = {}
count = 0
l = ["var X"," ","mov R2 r3","add R1 R2 R3"," ","st R3 X","mov R1 $100"]
for i in l:
    if(i==''):
        count+=1
        continue
    else:
        cmd = i.split()
        print(checking(cmd,dicinst,dicreg,dicvar,diclabel,count))
        count+=1
