sutra = ["अइउण्","ऋऌक्","एओङ्","ऐऔच्","हयवरट्","लण्","ञमङणनम्","झभञ्","घढधष्","जबगडदश्","खफछठथचटतव्","कपय्","शषसर्","हल्"]

panini_pratyahar = ["अण्","अक्","इक्","उक्","एङ्","अच्","इच्","एच्","ऐच्","अट्","अण्","इण्","यण्","अम्","यम्","ञम्","ङम्","यञ्","झष्","भष्","अश्","हश्","वश्","झश्","जश्","बश्","छव्","यय्","मय्","झय्","खय्","चय्","यर्","झर्","चर्","शर्","अल्","हल्","वल्","रल्","झल्"]

def pratyahar_with_nth_it(n):
    pratyahar = []
    num = 0
    
    for i in range(n,-1,-1):
        for s in sutra[i][-3::-1]:
            num |= 1 << (ord(s) & 0xFF)
            pratyahar.append([s+sutra[n][-2:],num])
	    
    return pratyahar[-1:0:-1]

def convert_to_set(num):
    pratyahar = []
    unicode_start = ord(sutra[0][0]) & 0xFF00
    i = 0
    while(num):
        if(num & 1):
            pratyahar.append(chr(unicode_start | i))
        num = num >> 1
        i += 1
    return pratyahar

        
def all_pratyahar():
    pratyahar = []
    for i in range(len(sutra)):
        pratyahar += pratyahar_with_nth_it(i)
    
    index = 0
    names = [p[0] for p in pratyahar]
    used_pratyahar = []
    
    for p in panini_pratyahar:
        index += names[index:].index(p)
        used_pratyahar.append([p,convert_to_set(pratyahar[index][1])])

    distinct_sets = set()
    
    for p in pratyahar:
        distinct_sets.add(p[1])

    return used_pratyahar,len(distinct_sets)
    
pratyahar, count  = all_pratyahar()

print("Total number of possible प्रत्याहार is %i" % count)  

print("Number of प्रत्याहार used by पाणिनि is %i" % len(pratyahar))

for p in pratyahar:
    print(p[0]+' = '+str(p[1]))
