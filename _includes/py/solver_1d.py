'''
Define doping profile 
Unit of x is microns.
Unit of doping is per cubic centimeter
'''
def doping(x): 
    if(x<5):
        return -1e18
    elif(x>=95):
        return 1e18
    else:
        return 1e12

''' 
Define node positions and mesh spacing about them as [node position,spacing]
Length unit : microns
'''
nodes = [[0,0.5],[5,0.01],[50,1],[95,0.01 ],[100,0.5]]  

'''
Define left and right boundary conditions as [contact_type,value] where value is potential offset for ohmic and schottky contacts and electric field for normal derivative boundary conditionsplotter.plot_1d(x,V,'Potential','volt')
plotter.plot_1d(x,n,'Electron density','density',scale='logy')
plotter.plot_1d(x,p,'Hole density','density',scale='logy')
plotter.plot_1d(x,n+p,'Total carrier density','density',scale='logy')
'o' - ohmic
's' - schottky
'n' - normal electric field
Potential unit - Volts
Electric field unit - Volts/micron
'''
boundary = [['o',0],['o',0]]

mesh,Nd,V,n,p = solution_eq_1d(params,nodes,doping,boundary,geom='rect')

plot_solution_1d(mesh,Nd,V,n,p,params,show=True)