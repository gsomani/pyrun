def generate_bitmask(bits,base_bits):
    base = 1 << base_bits
    num = 0
    bits_in_block = base_bits << 1
    for i in range(bits//bits_in_block):
        num = (num << bits_in_block) | (base - 1)
    return num
   
def generate_all_bitmask(bits):
    bitmask = []
    base_bits = 1
    while(base_bits < bits):
        bitmask.append(generate_bitmask(bits,base_bits))
        base_bits = base_bits << 1
    return bitmask 

def pop_count(n,bitmask,bits,base_bits):
    if(bits == base_bits):
        return n

    even_bits = n & bitmask[0]
    odd_bits = (n >> base_bits) & bitmask[0]
    sum_bits = odd_bits + even_bits

    return pop_count(sum_bits,bitmask[1:],bits,base_bits << 1)

def count_set_bits_naive(n):
    i = 0
    while(n):
        i += n & 1
        n = n >> 1
    return i
 
def count_set_bits_karnighan(n):
    i = 0
    while(n):
        n &= (n - 1)
        i += 1
    return i
       
def count_set_bits(numbers,method):
    sum_bits = []
    for i in numbers:
        sum_bits.append(method(i))
    return sum_bits 
 
def count_set_bits_pop_count(numbers,bits):
    bitmask = generate_all_bitmask(bits)
    sum_bits = []
    for n in numbers:
        sum_bits.append(pop_count(n,bitmask,bits,1))
    return sum_bits

numbers = list(range(1<<21))

print(count_set_bits_pop_count(numbers,32) == count_set_bits(numbers,count_set_bits_karnighan) == count_set_bits(numbers,count_set_bits_naive))
