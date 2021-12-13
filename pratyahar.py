import numpy as np

letters = ["अ","इ","उ","ऋ","ऌ","ए","ओ","ऐ", "औ","क","ख","ग","घ","ङ","च","छ","ज","झ","ञ","ट","ठ","ड","ढ","ण","त","थ","द","ध","न","प","फ","ब","भ","म","य","र","ल","व","श","ष","स","ह"] 

sutra =["अइउ","ऋऌ","एओ","ऐऔ","हयवर","ल","ञमङणन","झभ","घढध","जबगडद","खफछठथचटत","कप","शषस","ह"]

its = ["ण्","क्","ङ्","च्","ट्","ण्","म्","ञ्","ष्","श्","व्","य","र्","ल़्"]

pratyahar = {}

code = {}



def set_pratyahar(n):
    
    set_of_sets = set() 

    cur = set()
 
    for i in range(n,-1,-1):
        for s in sutra[i][::-1]:
            cur.add(s)
            set_of_sets.add(frozenset(cur))

    return set_of_sets
        
def pratyahar_count(n):
   
    l = 0
    
    set_of_sets = set()

    for i in range(n):
        set_of_sets.update(set_pratyahar(i))
    
    return len(set_of_sets)



print(pratyahar_count(14))
