'''
input_solver - defines mesh and solves poisson eqaution
'''
import numpy as np
from input_solver import *

T = 300 # K
k = 11.8
Nc = 2.8e19 # /cm^3
Nv = 1.04e19 # /cm^3
Eg = 1.1
mu_n = 1000 # cm^2/V-s
mu_p = 500 # cm^2/V-s
tn = 1000 # us
tp = 1000 # us
affinity = 1 # eV

params = [T,k,Nc,Nv,Eg,mu_n,mu_p,tn,tp,affinity]