import numpy as np
import copy

class rational(object):
    @staticmethod
    def gcd(p,q):
        if(q>p):
            return rational.gcd(q,p)
        if(q<0):
            return rational.gcd(p,-q)
        if(q==0):
            return p
        return rational.gcd(q,p%q)
    
    @staticmethod
    def lcm(p,q):
        return p*(q//rational.gcd(p,q))

    @staticmethod
    def continuedFraction(num,eps):
        p = 1
        q = 0
        a = [int(num)]
        num -= a[0]
        if(num < 0):
            num += 1
            a = [a[0] - 1]
        

        r = [a[0],1]

        while(abs(num) > eps):
            num = 1/num
            a = int(num) 
            rNext = [r[0]*a+p,r[1]*a+q]
            
            if(rNext[1]*eps > 1):
                break

            p = r[0]
            q = r[1]
            r = copy.copy(rNext)
            num -= a

        return r

    def __init__(self,p,q=1,eps=2**-8):
        if(isinstance(p,rational) and q==1):
            self.p = p.p
            self.q = p.q
            self.eps = p.eps
            return
        self.eps = eps
        if(isinstance(p,int)):
            g = rational.gcd(p,q)
            rat = [p//g, q//g]
        else:
            rat = rational.continuedFraction(p,eps=eps)
        self.p,self.q = rat
        
    def __float__(self):    
        return self.p/self.q

    def _cmp(self,r):
        r = rational(r,eps=self.eps)
        diff = self - r
        return diff.p

    def __gt__(self,r):
        return self._cmp(r) > 0  

    def __ge__(self,r):
        return self._cmp(r) >= 0  

    def __le__(self,r):
        return self._cmp(r) <= 0  

    def __lt__(self,r):
        return self._cmp(r) < 0 

    def __eq__(self,r):
        return self._cmp(r) == 0

    def __add__(self,r):
        r = rational(r,eps=self.eps)
        l = rational.lcm(self.q,r.q)
        p1 = self.p * (l//self.q)
        p2 = r.p * (l//r.q)
        p = p1+p2
        q = l
        return rational(p,q)

    def __mul__(self,r):
        r = rational(r,eps=self.eps)
        g1 = rational.gcd(self.p,r.q)
        g2 = rational.gcd(self.q,r.p)
        p1 = self.p // g1
        p2 = r.p // g2
        q1 = self.q // g2
        q2 = r.q // g1
        p = p1*p2
        q = q1*q2
        return rational(p,q)

    def __truediv__(self,r):
        r = rational(r,eps=self.eps)
        rat = rational(r.q,r.p)
        return self*rat

    def __neg__(self):
        return rational(-self.p,self.q)

    def __sub__(self,r):
        r = rational(r,eps=self.eps)
        return self + (-r)

    def __isub__(self,rat):
        return self - rat

    def __imul__(self,rat):
        return self * rat

    def __iadd__(self,rat):
        return self + rat

    def __idiv__(self,rat):
        return self / rat
   
    def __repr__(self):
        return ("%d/%d(%f)" %(self.p,self.q,float(self)))
    
    def __str__(self):
        return ("%d/%d(%f)" %(self.p,self.q,float(self)))

    @property
    def inv(self):
        return rational(self.q,self.p)

    
class rationalMatrix(object): 
    @staticmethod
    def toRational(array,eps):
        shape = array.shape
        if(len(shape)==0):
            return rational(array,eps=eps)
        rat = []
        for a in array:
            rat.append(rationalMatrix.toRational(a,eps))
        return np.array(rat)
        
    def __init__(self,matrix,eps=2**-8):
        if(isinstance(matrix,rationalMatrix)):
            self.matrix = matrix
            self.eps = eps
            return
        self.matrix = rationalMatrix.toRational(matrix,eps=eps)
        self.eps = eps

    def __repr__(self):
        return self.matrix.__repr__()
   
    def __str__(self):
        return self.matrix.__str__()

    def __add__(self,other):
        return self.matrix + other.matrix

    def __sub__(self,other):
        return self.matrix - other.matrix

    def __mul__(self,other):
        return rationalMatrix(np.dot(self.matrix,other.matrix))

    @staticmethod
    def identity(n):
       return rationalMatrix(np.eye(n))

