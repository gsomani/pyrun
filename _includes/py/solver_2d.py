'''
Define doping profile 
Unit of x is microns.
Unit of doping is per cubic centimeter
'''
def doping(x,y):
    if(y<1 and x<10):
        return 1e18
    elif(y<1 and x>30):
        return -1e18
    elif(y>99):
        return -1e18
    else:
        return 1e12
    
''' 
Define node positions and mesh spacing about them as [node position,spacing]
Length unit : microns
'''
nodes_x = [[0,1],[10,0.1],[20,2],[200,4]]
nodes_y = [[0,0.25],[1,0.1],[10,2],[50,4],[90,2],[99,0.1],[100,0.25]]

nodes = [nodes_x,nodes_y]

'''
Define top and bottom boundary conditions as [contact_type,value] where value is potential offset for ohmic and schottky contacts and electric field for normal derivative boundary conditions. Boundary conditions are described for each section. Section is the region between two nodes defined.
'o' - ohmic
's' - schottky
'n' - normal electric field
Potential unit - Volts
Electric field unit - Volts/micron
'''
contact_top = [['n',0],['n',0],['n',0]]
contact_bot = [['n',0],['n',0],['n',0]]

contact = [contact_top,contact_bot]

mesh,Nd,V,n,p = solution_eq_2d(params,nodes,doping,contact,geom='cyl')

plot_solution_2d(mesh,Nd,V,n,p,params,show=True)