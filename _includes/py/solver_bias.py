contact = [['o',0],['o',0]]  # set boundary condition at contacts. Unit of potential is volt

def gen(x): # define carrier generation rate by physical process other than thermal generation (Unit : per cubic centimeter per second)
    return 0
    
bias = [-5,1] # Voltage bias sweep (Reverse bias and forward bias) to be applied on left end with respect to right end. Unit of voltage is volt

mesh,Nd,solution_start,solution_end,V,J,J_left,J_right = solve_current(params,nodes,doping,contact,bias)

plot_JV(V,J,params,show=False)

plot_solution_both_ends(mesh,Nd,params,solution_start,solution_end,show=False)