def swap(A,m,n):
    A[m],A[n]=A[n],A[m]

def permute(k,A):
    p = []
    k-=1
    if(k):
        for i in range(k):
            p += permute(k,A)
            if(k & 1):
                swap(A,i,k)
            else:
                swap(A,0,k)
        
        p += permute(k,A)
    else:
        p = [A.copy()]

    return p

def permutation(A):
    return permute(len(A),A)
