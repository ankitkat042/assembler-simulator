def checklen(cmd,type,inslist):
    if(type=='A'):
        if(len(cmd)!=4):
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid length")
            return False
        else:
            return True
    
    elif(type=='B' or type=='C' or type=='D'):
        if(len(cmd)!=3):
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid length")
            return False
        else:
            return True
    
    elif(type=='E'):
        if(len(cmd)!=2):
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid length")
            return False
        else:
            return True
    
    elif(type=='F'):
        if(len(cmd)!=1):
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid length")
            return False
        else:
            return True

def checking_typeA(cmd,dicisnt,dicreg,inslist):
    if(cmd[1] not in dicreg.keys() or cmd[2] not in dicreg.keys() or cmd[3] not in dicreg.keys()):
        print(f"Error At line {inslist[' '.join(cmd)]} : Invalid register")
        return False
    else:
        return True

def checking_typeB(cmd,dicinst,dicreg,inlist):
    if(cmd[1] not in dicreg.keys()):
        print(f"Error At line {inslist[' '.join(cmd)]} : Invalid register")
        return False
    else:
        if(cmd[2][0]!='$'):
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid Immediate syntax")
            return False
        else:
            if(0<=int(cmd[2][1:])<=255):
                return True
            else:
                print(f"Error At line {inslist[' '.join(cmd)]} : Number out of range")
                return False

def checking_typeC(cmd,dicinst,dicreg,count):
    if(cmd[1] not in dicreg.keys() or cmd[2] not in dicreg.keys()):
        print(f"Error At line {inslist[' '.join(cmd)]} : Invalid register")
        return False
    else:
        return True

def checking_typeD(cmd,dicinst,dicreg,varDict,count):
    if(cmd[1] not in dicreg.keys()):
        print(f"Error At line {inslist[' '.join(cmd)]} : Invalid register")
        return False
    else:
        if(cmd[2] not in varDict.keys()):
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid variable")
            return False
        else:
            return True

def checking_typeE(cmd,dicinst,dicreg,diclabel,count):
    if(cmd[1] not in diclabel.keys()):
        print(f"Error At line {inslist[' '.join(cmd)]} : Invalid label")
        return False
    else:
        return True

def checking_typeF(cmd,dicinst,dicreg,diclabel):
    return True

def checking(cmd,dicinst,dicreg,varDict,diclabel,inslist):
    if(list(inslist.keys())[-1]=='hlt'):

        if(cmd[0] not in dicinst.keys() or cmd[0]=='var'):
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid Instruction")
            return False

        else:
            if(cmd[0]=='mov'):
                if(cmd[2][0].isalpha()):
                        typ = 'C'
                else:
                    typ = 'B'
                    
            else:
                if(cmd[0]=='var'):
                    typ = 'X'
                else:
                    typ = dicinst[cmd[0]][1]

            if(checklen(cmd,typ,inslist)):
                if(typ=='A'):
                    result = checking_typeA(cmd,dicinst,dicreg,inslist)
                    return result

                elif(typ=='B'):
                    result = checking_typeB(cmd,dicinst,dicreg,inslist)
                    return result

                elif(typ=='C'):
                    result = checking_typeC(cmd,dicinst,dicreg,inslist)
                    return result
                
                elif(typ=='D'):
                    result = checking_typeD(cmd,dicinst,dicreg,varDict,inslist)
                    return result

                elif(typ=='E'):
                    result = checking_typeE(cmd,dicinst,dicreg,diclabel,inslist)
                    return result
                
                elif(typ=='F'):
                    result = checking_typeF(cmd,dicinst,dicreg,inslist)
                    return result
            else:
                return False
    else:
        print("Error At End: No hlt statement at end")
        return False



dicinst = {"add":['10000','A'],"sub":['10001','B'],"mov":['10010','B'],"mov":['10011','C'],"ld":['10100','D'],
"st":['10101','D'],"mul":['10110','A'],"div":['10111','C'],"rs":['11000','B'],"ls":['11001','B'],"xor":['11010','A'],
"or":['11011','A'],"and":['11100','A'],"not":['11101','C'],"cmp":['11110','C'],"jmp":['11111','E'],
"jlt":['01100','E'],"jgt":['01101','E'],"je":['01111','E'],"hlt":['01010','F']}

dicreg = {'R1': "000",'R2':"001",'R3':"010","R4":"100","R5":"101","R6":"110"}
diclabel = {}

inslist = {'var X':1, 'var y':2, 'var Z':3, 'var u':4, 'add R1 R2 R3':5, 'mov R1 $9':6,'hlt':7}
instDict = {'add R1 R2 R3': 1, 'mov R1 $9': 2,'hlt':3}
varDict = {'X': 3, 'y': 4, 'Z': 5, 'u': 6}

# print(inslist.keys())

for i in instDict.keys():
        cmd = i.split()
        if(checking(cmd,dicinst,dicreg,varDict,diclabel,inslist)==False):
            break
