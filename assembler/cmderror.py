def checklen(cmd,type,inslist,q,s):
    if(type=='A'):
        if(len(cmd)!=4):
            if(q==1):
                print(f"Error At line {inslist[s]} : Invalid Instruction length in Label")
                q=0
                return False
            else:    
                print(f"Error At line {inslist[' '.join(cmd)]} : Invalid length")
                return False
        else:
            return True
    
    elif(type=='B' or type=='C' or type=='D'):
        if(len(cmd)!=3):
            if(q==1):
                print(f"Error At line {inslist[s]} : Invalid Instruction length in Label")
                q=0
                return False
            else:    
                print(f"Error At line {inslist[' '.join(cmd)]} : Invalid length")
                return False
        else:
            return True
    
    elif(type=='E'):
        if(len(cmd)!=2):
            if(q==1):
                print(f"Error At line {inslist[s]} : Invalid Instruction length in Label")
                q=0
                return False
            else:    
                print(f"Error At line {inslist[' '.join(cmd)]} : Invalid length")
                return False
        else:
            return True
    
    elif(type=='F'):
        if(len(cmd)!=1):
            if(q==1):
                print(f"Error At line {inslist[s]} : Invalid Instruction length in Label")
                q=0
                return False
            else:    
                print(f"Error At line {inslist[' '.join(cmd)]} : Invalid length")
                return False
        else:
            return True

def checking_typeA(cmd,dicisnt,dicreg,inslist,q,s):
    if((cmd[1] not in dicreg.keys()or cmd[1]=="FLAGS") or (cmd[2] not in dicreg.keys() or cmd[2]=="FLAGS") or (cmd[3] not in dicreg.keys() or cmd[3]=="FLAGS")):
        if(q==1):
            print(f"Error At line {inslist[s]} : Invalid Register in Label")
            q=0
            return False
        else:
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid register")
            return False
    else:
        return True

def checking_typeB(cmd,dicinst,dicreg,inlist,q,s):
    if(cmd[1] not in dicreg.keys() or cmd[1]=="FLAGS"):
        if(q==1):
            print(f"Error At line {inslist[s]} : Invalid Register in Label")
            q=0
            return False
        else:
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

def checking_typeC(cmd,dicinst,dicreg,q,s):
    if((cmd[1] not in dicreg.keys() or cmd[1]=="FLAGS") or cmd[2] not in dicreg.keys()):
        if(q==1):
            print(f"Error At line {inslist[s]} : Invalid Register in Label")
            q=0
            return False
        else:
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid register")
            return False
    else:
        return True

def checking_typeD(cmd,dicinst,dicreg,varDict,q,s):
    if(cmd[1] not in dicreg.keys() or cmd[1]=="FLAGS"):
        if(q==1):
            print(f"Error At line {inslist[s]} : Invalid Register in Label")
            q=0
            return False
        else:
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid register")
            return False
    else:
        if(cmd[2] not in varDict.keys()):
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid variable")
            return False
        else:
            return True

def checking_typeE(cmd,dicinst,dicreg,diclabel,inslist,q,s):
    if(cmd[1] not in diclabel.keys()):
        if(q==1):
            print(f"Error At line {inslist[s]} : Invalid Label")
            q=0
            return False
        else:
            print(f"Error At line {inslist[' '.join(cmd)]} : Invalid Memory address")
            return False
    else:
        return True

def checking_typeF(cmd,dicinst,dicreg,diclabel,q,s):
    return True





def checking(cmd,dicinst,dicreg,varDict,diclabel,inslist,q,s):
    if(list(inslist.keys())[-1]=='hlt'):

        if(cmd[0] not in dicinst.keys() or cmd[0]=='var'):
            if(q==1):
                print(s)
                print(f"Error At line {inslist[s]} : Invalid Instruction in Label")
                q=0
                return False
            else:
                print(cmd)
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

            if(checklen(cmd,typ,inslist,q,s)):
                if(typ=='A'):
                    result = checking_typeA(cmd,dicinst,dicreg,inslist,q,s)
                    return result

                elif(typ=='B'):
                    result = checking_typeB(cmd,dicinst,dicreg,inslist,q,s)
                    return result

                elif(typ=='C'):
                    result = checking_typeC(cmd,dicinst,dicreg,inslist,q,s)
                    return result
                
                elif(typ=='D'):
                    result = checking_typeD(cmd,dicinst,dicreg,varDict,inslist,q)
                    return result

                elif(typ=='E'):
                    result = checking_typeE(cmd,dicinst,dicreg,diclabel,inslist,q,s)
                    return result
                
                elif(typ=='F'):
                    result = checking_typeF(cmd,dicinst,dicreg,inslist,q,s)
                    return result
            else:
                return False
    else:
        print("Error At End: No hlt statement at end")
        return False


def checking_label(s,diclabel,inslist,q):
    idx = s.index(':')
    x = idx+2
    y = idx-1
    if(idx==0 or idx==len(s)-1 or s[x]==' ' or s[y]==' '):
        print(f"Error At line {inslist[s]} : Invalid label syntax")
        return False
    else:
        q=1
        # lineno = inslist[s]
        o = list(s.split())[1:]
        k = checking(o,dicinst,dicreg,varDict,diclabel,inslist,q,s)
        return k


q = 0
dicinst = {"add":['10000','A'],"sub":['10001','B'],"mov":['10010','B'],"mov":['10011','C'],"ld":['10100','D'],
"st":['10101','D'],"mul":['10110','A'],"div":['10111','C'],"rs":['11000','B'],"ls":['11001','B'],"xor":['11010','A'],
"or":['11011','A'],"and":['11100','A'],"not":['11101','C'],"cmp":['11110','C'],"jmp":['11111','E'],
"jlt":['01100','E'],"jgt":['01101','E'],"je":['01111','E'],"hlt":['01010','F']}

dicreg = {'R1': "000",'R2':"001",'R3':"010","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
diclabel = {'label1':3}

inslist = {'var X':1, 'var y':2, 'var Z':3, 'var u':4, 'add R1 R2 R3':5, 'mov R1 $9':6,'label1: add R1 R2 R3':7,'jlt label1': 8,'ld R1 X':9,'hlt':10}
instDict = {'add R1 R2 R3': 1, 'mov R1 $9': 2,'label1: add R1 R2 R3':3,'jlt label1':4,'ld R1 X':5,'hlt':6}
varDict = {'X': 6, 'y': 7, 'Z': 8, 'u': 9}

# print(inslist.keys())

for i in instDict.keys():
    if(':' in i):
        if(checking_label(i,diclabel,inslist,q)==False):
            break
    else:
        cmd = i.split()
        if(checking(cmd,dicinst,dicreg,varDict,diclabel,inslist,q,i)==False):
            break
