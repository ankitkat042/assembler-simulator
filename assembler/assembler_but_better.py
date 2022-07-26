from sys import stdin
from collections import Counter

op   =   {"add" : "10000",
          "sub" : "10001",
          "mov" : "10010",
          "ld"  :  "10100",
          "st"  :  "10101",
          "mul" : "10110",
          "div" : "10111",
          "rs"  :  "11000",
          "ls"  :  "11001",
          "xor" : "11010",
          "or"  :  "11011",
          "and" : "11100",
          "not" : "11101",
          "cmp" : "11110",
          "jmp" : "11111",
          "jlt" : "01100",
          "jgt" : "01101",
          "je"  :  "01111",
          "hlt" : "01010"}


reg = {"R0" : "000",
       "R1" : "001",
        "R2": "010",
        "R3": "011",
        "R4": "100",
        "R5": "101",
        "R6": "110",
        "FLAGS": "111",}


A = ["add","sub","mul","xor","or","and"]
B = ["mov","rs","ls"]
C = ["mov","div","not","cmp"]
D = ["ld","st"]
E = ["jmp","jlt","jgt","je"]
F = ["hlt"]

def unusedBits(n):
    return "0"*n

def binConvert (n):
    return '{0:08b}'.format(n)

def convertor(syntax, varDict, diclabel):
    code = syntax[0]
    if code in A:
        return op[code] + unusedBits(2) + reg[syntax[1]] + reg[syntax[2]] + reg[syntax[3]]
    
    elif code in B and syntax[-1][0] == "$":
        num=int(syntax[-1][1:])
        return op[code] + reg[syntax[1]] + binConvert(num)

    elif code in C:
        s=op[code]
        if code == "mov":
            s="10011"
        return s + unusedBits(5) + reg[syntax[1]] + reg[syntax[2]]
    
    elif code in D:
        var=syntax[2]
        return op[code] + reg[syntax[1]] + binConvert(varDict[var])
    
    elif code in E:
        label=syntax[1]

        return op[code] + unusedBits(3) + binConvert(diclabel[label])
    
    elif code in F:
        return op[code] + unusedBits(11)


# ------------------Testing--------------------------------
# s="mov R1 R2"   #write sytnax
# ans="0101000000000000"          #write the expected bin conversion
# syntaxx=s.split()
# mem_location=None
# bin=convertor(syntaxx, mem_location)
# print(bin==ans)
# # print(bin)
# ------------------------------------------------------------



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
q = 0
dicinst = {"add":['10000','A'],"sub":['10001','A'],"mov":['10010','B'],"mov":['10011','C'],"ld":['10100','D'],
"st":['10101','D'],"mul":['10110','A'],"div":['10111','C'],"rs":['11000','B'],"ls":['11001','B'],"xor":['11010','A'],
"or":['11011','A'],"and":['11100','A'],"not":['11101','C'],"cmp":['11110','C'],"jmp":['11111','E'],
"jlt":['01100','E'],"jgt":['01101','E'],"je":['01111','E'],"hlt":['01010','F']}

dicreg = {"R0" : "000",
       "R1" : "001",
        "R2": "010",
        "R3": "011",
        "R4": "100",
        "R5": "101",
        "R6": "110",
        "FLAGS": "111",}
# diclabel = {'label1':3}

# inslist= {0: 'var X', 1: 'var y', 2: 'var Z', 4: 'var u', 6: 'add R1 R2 R3', 7: 'add R1 R2 R3', 9: 'add R1 R2 R3', 13: 'mov R1 $9', 18: 'add: add R3 R3 R4', 20: 'hlt'}
# instDict={0: 'add R1 R2 R3', 1: 'add R1 R2 R3', 2: 'add R1 R2 R3', 3: 'mov R1 $9', 4: 'add: add R3 R3 R4', 5: 'hlt'}
# varDict= {6: 'X', 7: 'y', 8: 'Z', 9: 'u'}
# diclabel= {18: 'add'}

#############################      FILE INPUT    ###########################

#input_file = open("1112.txt","r")
input_file=stdin
# print(input_file)
a = input_file.read().split("\n")
# a = ['var X', 'mov R1 $10', 'label1: hlt ','mov R2 $100', 'label2: hlt','mul R3 R1 R2','jmp label1','cmp R1 R2', 'jgt label2','st R3 X', 'hlt', '']

############################################################################



# --------------------------------------------------------------------------
'''def printf():
    print(inslist)
    print(f)
    print(varDict)
    print(diclabel)
    print(labeldic)
    print(hltinlabel)
'''
# --------------------------------------------------------------------------



inslist = {}
for i in range(1,len(a)+1):
    if a[i-1] == '' or '\t' in a[i-1] :
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

# -----------------------error type: varibale in between-----------------------
def varinbetween():
    inn=-1
    statevar=True
    for i in range(len(a)):
        
        if a[i][0:3]=="var":
            inn=i
        elif a[i]=='':
            pass
        elif statevar==True:
            inx=i
            statevar=False

    if inn>inx:
        print(f"Error in std-input at line {inn+1}: Varible declared after instruction")
        return False
    return True
# ----------------------------------------------------------------------------
varCheck = True
varhelp = 0
for i in range(1,len(f)+1):
    if f[i-1].split()[0] == 'var':
        if(check_space(f[i-1],inslist,varhelp)):
            if f[i-1].split()[0] == 'var' and len(f[i-1].split()) == 2:
                varDict[i+x-1] = f[i-1].split()[1]                          # change 1.0 : [i+x]->[i+x-1] to correct the variable numbers
            elif f[i-1].split()[0] == 'var' and len(f[i-1].split()) != 2:
                print(f"Error at line {list(inslist.keys())[i-1]}: Invalid variable")
                varCheck = False
                break
            else:
                print(f"Error at line {list(inslist.keys())[i-1]}: Invalid variable")
                varCheck = False
                break
        else:
            varCheck = False
            break
    else:
        pass
    varhelp+=1
diclabel = {}
labeldic={} # change 1.1
iterator = 0
for i in inslist.values():
    if ":" in i and (i[0] !=":" or i[-1] != ":"):
        diclabel[list(inslist.keys())[iterator]] = i[0:i.index(":")]
        labeldic[i[0:i.index(":")]]=i[i.index(":")+1:].strip()  #change 1.1.a             
    iterator+=1
varDicta = {value:key for key, value in varDict.items()}
diclabela = {value:key for key, value in diclabel.items()}
hltinlabel=0
if 'hlt' in labeldic.values():
    hltinlabel=1
# ----------------------------------error type: var name == label name   ----------------------------------
def checklabelinvar():
    varkeys=list(varDicta.keys())
    labelkeys=list(diclabela.keys())
    for i in range(len(varkeys)):
        for j in range(len(labelkeys)):
            if varkeys[i]==labelkeys[j]:
                print(f"Error at line {diclabela[labelkeys[j]]}: label name cannot be same as variable name")
                return False
    return True
# ------------------------------------------------------------------------------------------------------------




# -----------------------error type: same name variable-----------------------
cn = Counter(varDict.values())
cna=sorted(k for k,v in varDict.items() if cn[v] == 1)
def checkvar():
    if len(cna)!=len(varDict):
        z=-1
        cul=sorted(k for k,v in varDict.items() if cn[v] != 1)
        keyy=varDict[cul[-1]]
    
        culpritvar=f"var {keyy}"

        for i in range(len(a)):
            if a[i]==culpritvar:
                z=i+1
        print(f"General Syntax Error at line {z} : Two or more different variables have same names ")
        return False
    return True
# -----------------------------------error type: same name label----------------------


cnlabel = Counter(diclabel.values())
cnalabel=sorted(k for k,v in diclabel.items() if cnlabel[v] == 1)
def checklabel():
    if len(cnalabel)!=len(diclabel):
        z=-1
        cul=sorted(k for k,v in diclabel.items() if cnlabel[v] != 1)
        
        keyy=diclabel[cul[-1]]
        
        z=diclabela[keyy]
        
        print(f"General Syntax Error {z}: Two or more different labels have same names ")
        return False
    return True

# print(inslist.keys())




# count = len(varDict.values())
final=[]
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
    if(cmd[1] in dicinst.keys() or cmd[2] in dicinst.keys() or cmd[3] in dicinst.keys()):
        if(q==1):
            print(f"Error At line {list(inslist.keys())[count]} : Register cannot be a keyword in Label")
            q=0
            return False
        else:
            print(f"Error At line {list(inslist.keys())[count]} : Register cannot be a Keyword")
            return False
    elif((cmd[1] not in dicreg.keys()or cmd[1]=="FLAGS") or (cmd[2] not in dicreg.keys() or cmd[2]=="FLAGS") or (cmd[3] not in dicreg.keys() or cmd[3]=="FLAGS")):
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
    if(cmd[1] in dicinst.keys()):
        if(q==1):
            print(f"Error At line {list(inslist.keys())[count]} : Register cannot be a keyword in Label")
            q=0
            return False
        else:
            print(f"Error at line {list(inslist.keys())[count]} : Register cannot be a Keyword")
            return False
    elif(cmd[1] not in dicreg.keys() or cmd[1]=="FLAGS"):
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
            if(cmd[2][1:] in dicinst.keys()):
                print(f"Error at line {list(inslist.keys())[count]} : Immediate value cannot a keyword")
                return False
            elif(0<=int(cmd[2][1:])<=255):
                return True
            else:
                print(f"Error At line {list(inslist.keys())[count]} : Number out of range")
                return False

def checking_typeC(cmd,dicinst,dicreg,inslist,q,s,count):
    if(cmd[1] in dicinst.keys() or cmd[2] in dicinst.keys()):
        if(q==1):
            print(f"Error At line {list(inslist.keys())[count]} : Register cannot be a Keyword in label")
            q=0
            return False
        else:
            print(f"Error at line {list(inslist.keys())[count]} : Register cannot be a Keyword")
            return False
    elif((cmd[1] not in dicreg.keys() or cmd[1]=="FLAGS") or cmd[2] not in dicreg.keys()):
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
    if(cmd[1] in dicinst.keys()):
        if(q==1):
            print(f"Error At line {list(inslist.keys())[count]} : Register cannot be a Keyword in Label")
            q=0
            return False
        else:
            print(f"Error at line {list(inslist.keys())[count]} : Register cannot be a Keyword")
            return False
    elif(cmd[1] not in dicreg.keys() or cmd[1]=="FLAGS"):
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
    if(cmd[1] in dicinst.keys()):
        if(q==1):
            print(f"Error At line {list(inslist.keys())[count]} : Memory address cannot be a Keyword in Label")
            q=0
            return False
        else:
            print(f"Error at line {list(inslist.keys())[count]} : Memory address cannot be a Keyword")
            return False
    elif(cmd[1] not in diclabel.values()):
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


def checking(cmd,dicinst,dicreg,varDict,diclabel,inslist,q,s,count):
    l = list(inslist.values())
    if(list(inslist.values())[-1]=='hlt' and l.count('hlt')==1 or hltinlabel):
        # if(check_space(s,inslist,count)):
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
        # else:
        #     # print(f"Error At line {inslist[s]} : Invalid spaces in Instruction")
        #     return False
    else:
        print("Error At End: No hlt statement at end or hlt statement in between the code")
        return False


def checking_label(s,diclabel,inslist,q,count):
    idx = s.index(':')
    y = idx-1
    if(idx==0 or idx==len(s)-1 or s[y]==' '):
        print(f"Error At line {list(inslist.keys())[count]} : Invalid label syntax")
        return False
    elif(s[:idx] in dicinst.keys()):
        print(f"Error at line {list(inslist.keys())[count]} : label name cannot be a Keyword")
        return False
    else:
        q=1
        # lineno = inslist[s]
        o = list(s.split())[1:]
        k = checking(o,dicinst,dicreg,varDict,diclabel,inslist,q,s,count)
        return k

count = len(varDict.keys())
if(varCheck):
    if varinbetween() and checklabelinvar() and checkvar() and checklabel():
        for i in instDict.values():
                
                if(':' in i):
                    # if(check_space(i,inslist,count)):
                        if(checking_label(i,diclabel,inslist,q,count)==False):
                            break
                        else:
                            
                            final.append(convertor(i.split()[1:], varDicta, diclabela))
                            
                else:
                    cmd = i.split()
                    if(checking(cmd,dicinst,dicreg,varDict,diclabel,inslist,q,i,count)==False):
                        break
                    
                    else:
                        
                        final.append(convertor(i.split(), varDicta, diclabela))
                count+=1


for i in range(len(final)):
    if i<256:
        print(final[i])
