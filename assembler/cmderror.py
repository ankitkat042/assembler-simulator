# def getline_no(inslist,s):
#     for i in inslist.values():
#         if()



from main2 import*

def checklen(cmd,type,inslist,q,s,count):
    if(type=='A'):
        if(len(cmd)!=4):
            if(q==1):
                print(f"Error At line {list(inslist.keys())[count]} : Invalid Instruction length in Label")
                q=0
                return False
            else:    
                print(f"Error At line {list(inslist.keys())[count]} : Invalid length")
                return False
        else:
            return True
    
    elif(type=='B' or type=='C' or type=='D'):
        if(len(cmd)!=3):
            if(q==1):
                print(f"Error At line {list(inslist.keys())[count]} : Invalid Instruction length in Label")
                q=0
                return False
            else:    
                print(f"Error At line {list(inslist.keys())[count]} : Invalid length")
                return False
        else:
            return True
    
    elif(type=='E'):
        if(len(cmd)!=2):
            if(q==1):
                print(f"Error At line {list(inslist.keys())[count]} : Invalid Instruction length in Label")
                q=0
                return False
            else:    
                print(f"Error At line {list(inslist.keys())[count]} : Invalid length")
                return False
        else:
            return True
    
    elif(type=='F'):
        if(len(cmd)!=1):
            if(q==1):
                print(f"Error At line {list(inslist.keys())[count]} : Invalid Instruction length in Label")
                q=0
                return False
            else:    
                print(f"Error At line {list(inslist.keys())[count]} : Invalid length")
                return False
        else:
            return True

def checking_typeA(cmd,dicisnt,dicreg,inslist,q,s,count):
    if((cmd[1] not in dicreg.keys()or cmd[1]=="FLAGS") or (cmd[2] not in dicreg.keys() or cmd[2]=="FLAGS") or (cmd[3] not in dicreg.keys() or cmd[3]=="FLAGS")):
        if(q==1):
            print(f"Error At line {list(inslist.keys())[count]} : Invalid Register in Label")
            q=0
            return False
        else:
            print(f"Error At line {list(inslist.keys())[count]} : Invalid register")
            return False
    else:
        return True

def checking_typeB(cmd,dicinst,dicreg,inlist,q,s,count):
    if(cmd[1] not in dicreg.keys() or cmd[1]=="FLAGS"):
        if(q==1):
            print(f"Error At line {list(inslist.keys())[count]} : Invalid Register in Label")
            q=0
            return False
        else:
            print(f"Error At line {list(inslist.keys())[count]} : Invalid register")
            return False
    else:
        if(cmd[2][0]!='$'):
            print(f"Error At line {list(inslist.keys())[count]} : Invalid Immediate syntax")
            return False
        else:
            if(0<=int(cmd[2][1:])<=255):
                return True
            else:
                print(f"Error At line {list(inslist.keys())[count]} : Number out of range")
                return False

def checking_typeC(cmd,dicinst,dicreg,q,s,count):
    if((cmd[1] not in dicreg.keys() or cmd[1]=="FLAGS") or cmd[2] not in dicreg.keys()):
        if(q==1):
            print(f"Error At line {list(inslist.keys())[count]} : Invalid Register in Label")
            q=0
            return False
        else:
            print(f"Error At line {list(inslist.keys())[count]} : Invalid register")
            return False
    else:
        return True

def checking_typeD(cmd,dicinst,dicreg,varDict,q,s,count):
    if(cmd[1] not in dicreg.keys() or cmd[1]=="FLAGS"):
        if(q==1):
            print(f"Error At line {list(inslist.keys())[count]} : Invalid Register in Label")
            q=0
            return False
        else:
            print(f"Error At line {list(inslist.keys())[count]} : Invalid register")
            return False
    else:
        if(cmd[2] not in varDict.values()):
            print(f"Error At line {list(inslist.keys())[count]} : Invalid variable")
            return False
        else:
            return True

def checking_typeE(cmd,dicinst,dicreg,diclabel,inslist,q,s,count):
    if(cmd[1] not in diclabel.values()):
        if(q==1):
            print(f"Error At line {list(inslist.keys())[count]} : Invalid Label")
            q=0
            return False
        else:
            print(f"Error At line {list(inslist.keys())[count]} : Invalid Memory address")
            return False
    else:
        return True

def checking_typeF(cmd,dicinst,dicreg,diclabel,q,s,count):
    return True

def check_space(i,inlist,count):
    c = 0
    for j in i:
        if(j==' '):
            c+=1
    if(len(i.split())-1==c):
        return True
    else:
        print(f"Error At line {list(inslist.keys())[count]} : Invalid spaces in instruction")
        return False


def checking(cmd,dicinst,dicreg,varDict,diclabel,inslist,q,s,count):
    l = list(inslist.values())
    if(list(inslist.values())[-1]=='hlt' and l.count('hlt')==1):
        if(check_space(s,inslist,count)):
            if(cmd[0] not in dicinst.keys() or cmd[0]=='var'):
                if(q==1):
                    print(s)
                    print(f"Error At line {list(inslist.keys())[count]} : Invalid Instruction in Label")
                    q=0
                    return False
                else:
                    print(cmd)
                    print(f"Error At line {list(inslist.keys())[count]} : Invalid Instruction")
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

                if(checklen(cmd,typ,inslist,q,s,count)):
                    if(typ=='A'):
                        result = checking_typeA(cmd,dicinst,dicreg,inslist,q,s,count)
                        return result

                    elif(typ=='B'):
                        result = checking_typeB(cmd,dicinst,dicreg,inslist,q,s,count)
                        return result

                    elif(typ=='C'):
                        result = checking_typeC(cmd,dicinst,dicreg,inslist,q,s,count)
                        return result
                    
                    elif(typ=='D'):
                        result = checking_typeD(cmd,dicinst,dicreg,varDict,q,s,count)
                        return result

                    elif(typ=='E'):
                        result = checking_typeE(cmd,dicinst,dicreg,diclabel,inslist,q,s,count)
                        return result
                    
                    elif(typ=='F'):
                        result = checking_typeF(cmd,dicinst,dicreg,inslist,q,s,count)
                        return result
                else:
                    return False
        else:
            # print(f"Error At line {inslist[s]} : Invalid spaces in Instruction")
            return False
    else:
        print("Error At End: No hlt statement at end or hlt statement in between the code")
        return False


def checking_label(s,diclabel,inslist,q,count):
    idx = s.index(':')
    x = idx+2
    y = idx-1
    if(idx==0 or idx==len(s)-1 or s[x]==' ' or s[y]==' '):
        print(f"Error At line {count} : Invalid label syntax")
        return False
    else:
        q=1
        # lineno = inslist[s]
        o = list(s.split())[1:]
        k = checking(o,dicinst,dicreg,varDict,diclabel,inslist,q,s,count)
        return k


q = 0
dicinst = {"add":['10000','A'],"sub":['10001','B'],"mov":['10010','B'],"mov":['10011','C'],"ld":['10100','D'],
"st":['10101','D'],"mul":['10110','A'],"div":['10111','C'],"rs":['11000','B'],"ls":['11001','B'],"xor":['11010','A'],
"or":['11011','A'],"and":['11100','A'],"not":['11101','C'],"cmp":['11110','C'],"jmp":['11111','E'],
"jlt":['01100','E'],"jgt":['01101','E'],"je":['01111','E'],"hlt":['01010','F']}

dicreg = {'R1': "000",'R2':"001",'R3':"010","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
# diclabel = {'label1':3}

# inslist= {0: 'var X', 1: 'var y', 2: 'var Z', 4: 'var u', 6: 'add R1 R2 R3', 7: 'add R1 R2 R3', 9: 'add R1 R2 R3', 13: 'mov R1 $9', 18: 'add: add R3 R3 R4', 20: 'hlt'}
# instDict={0: 'add R1 R2 R3', 1: 'add R1 R2 R3', 2: 'add R1 R2 R3', 3: 'mov R1 $9', 4: 'add: add R3 R3 R4', 5: 'hlt'}
# varDict= {6: 'X', 7: 'y', 8: 'Z', 9: 'u'}
# diclabel= {18: 'add'}
input_file = open("1112.txt","r")
a = input_file.read().split("\n")
inslist = {}
for i in range(1,len(a)+1):
    if a[i-1] == '':
        pass
    else:
        inslist[i] = a[i-1]  
purified = []
for line in inslist.values():
    if line.split()[0] == "var":
        pass
    else:
        purified.append(line)
instDict = {}
for i in range(1,len(purified)+1):
    instDict[i]= purified[i-1]
x = len(instDict)
varDict = {}
f = list(inslist.values())
for i in range(1,len(f)+1):
    if f[i-1].split()[0] == 'var' and len(f[i].split()) == 2:
        varDict[i+x] = f[i-1].split()[1]
    else:
        break
diclabel = {}
iterator = 0
for i in inslist.values():
    if ":" in i and (i[0] !=":" or i[-1] != ":"):
        diclabel[list(inslist.keys())[iterator]] = i[0:i.index(":")]
    iterator+=1
# print(inslist.keys())
count = len(varDict.values())
for i in instDict.values():
   
    if(':' in i):
        if(check_space(i,inslist,count)):
            if(checking_label(i,diclabel,inslist,q,count)==False):
                break
            else:
                print(i)
                print(convertor(i.split()[1:], varDict, diclabel))
    else:
        cmd = i.split()
        if(checking(cmd,dicinst,dicreg,varDict,diclabel,inslist,q,i,count)==False):
            break
        
        else:
            print(i)
            print(convertor(i.split(), varDict, diclabel))
    count+=1
