
memspace=input("Enter the space in memory(KB/MB etc): ")
if len(memspace.split())==1:
    memspace=memspace+' B'
size=memspace.split()[-1]
sizeDic={'KB': 8192,
      'Kb': 1024,
      'MB': 8388608,
      'Mb': 1048576,
      'GB': 8589934592,
      'Gb': 1073741824,
      'B': 8,
      'b': 1,
    }
while size not in sizeDic:
    print("memory type unavailable, Enter again")
    memspace=input("Enter the space in memory(KB/MB etc): ")
    size=memspace.split()[-1]




s='''
1. Bit Addressable Memory - Cell Size = 1 bit
2. Nibble Addressable Memory - Cell Size = 4 bit
3. Byte Addressable Memory - Cell Size = 8 bits(standard)
4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)

'''
print(s)

memType=int(input("Enter the number from above options: "))
word=0
if memType==4:
    word=int(input("(for option 4)Enter the word addressable CPU size: "))
mem={1:1, 2:4, 3:8, 4:word}
addressBits=mem[memType]
print("-------------------------------------------------")


totalMemSize=int(memspace.split()[0])*sizeDic[size]
import math

addressableMemBits=int(math.ceil(math.log2(totalMemSize/addressBits)))

instructionLen=int(input("Enter the length one instruction in bits: "))
resistorbitsLen=int(input("Enter the length of resistor in bits: "))

opcodeBits=instructionLen-addressableMemBits-resistorbitsLen
fillerBits=instructionLen-opcodeBits-2*resistorbitsLen

print(f'''
minimum bits are needed to represent an address in this architecture- {addressableMemBits}
Number of bits needed by opcode- {opcodeBits}
Number of filler bits in Instruction type 2- {fillerBits}
Maximum numbers of instructions this ISA can support- {2**opcodeBits}
Maximum number of registers this ISA can support- {2**resistorbitsLen}
''')

print('---------------------System Enhancement------------------------------')
instructionLen2=int(input("No of Bits CPU has: "))
print(s)
memType2=int(input("Enter the new option(pick a different option this time): "))
if memType2==4:
    word=int(input("(for option 4)Enter the word addressable CPU size: "))
    sizeDic[4]=word
if memType2==4:
    print((instructionLen2-int(math.ceil(math.log2(totalMemSize/word)))-resistorbitsLen))
else:
        print((instructionLen2-int(math.ceil(math.log2(totalMemSize/mem[memType2])))-resistorbitsLen))