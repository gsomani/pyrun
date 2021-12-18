from unidecode import unidecode

def devnagari_unicode():
    block_start =  ord('अ') & 0xFF00
    count = 0x80
    devnagari = []
    for i in range(block_start,block_start+count):
        if(unidecode(chr(i))):
            devnagari.append([i,chr(i)])
    return devnagari

devnagari = devnagari_unicode()

for unicode,char in devnagari:
    print("%04x %s" % (unicode,char)) 
