import numpy as np

def count_set_bits(n):
    i = 0
    while(n):
        n &= (n - 1)
        i += 1
    return i
 
def int_to_bit_array(num,bits): 
    bit = np.empty(bits,dtype=int) 
    for i in range(bits): 
        bit[i] = num & 1 
        num = num >> 1 
    return bit

def bits_to_int(bits):
    num = 0
    for i in range(len(bits)):
        num += 1 << bits[i] ;
    return num

def disparity(num,bits): 
    return 2*count_set_bits(num) - bits

def xored(num,bits): 
    bit = int_to_bit_array(num,bits) 
    x = np.empty(bits+1,dtype=int) 
    x[0] = bit[0] 
    for i in range(1,bits): 
        x[i] = x[i-1] ^ bit[i] 
    x[bits]=1
    x = bits_to_int(x) 
    return x 

def data_word(num):
    ones = count_set_bits(num)
    x = int(xored(num,8))
    y = x ^ 0b010101011
    if(ones<4 or (ones==4 and (num&1))):
        return x
    else:
        return y
        

for i in range(256):
    print(disparity(data_word(i),9))    
