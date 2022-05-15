import numpy as np
from sympy import *
x, y, z = symbols ("x y z")

class Interpolation():

  def LNDD_matrix(self,d,x):
    """ Devuelve el valor interpolado (diferencia divididas de Newton)
        dados valores de una matriz
        IN: x0, x1 --> evaluar y; x (para interpolar)
        OUT: y(x)

                         f(x1) - f(x0)
        Yint = f(x0) + ------------------ (x - x0)
                            x1 - x0   
    """

    yinterpol = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0])) 
    return yinterpol 

  def LNDD_lists(self,X,Y,x):
    """ Devuelve el valor interpolado (diferencia divididas de Newton)
        dados valores de listas (X,Y)
        IN: X,Y --> evaluar y; x (para interpolar)
        OUT: y(x)

                         f(x1) - f(x0)
        Yint = f(x0) + ------------------ (x - x0)
                            x1 - x0   
    """
    Yint = Y[1] + (x - X[1]) *((Y[2] - Y[1])/(X[2]-X[1]))
    return Yint

  def LNDD_fun(self):
    """ Devuelve el valor interpolado (diferencia divididas de Newton)
        dados valores x0, x1, x2int.
        IN: f --> función; x0,x1 --> evaluar f; x2int (para interpolar)
        OUT: f(x)

                         f(x1) - f(x0)
        Yint = f(x0) + ------------------ (x - x0)
                            x1 - x0   
    """
    f = x + 1
    Yint =f.subs(x, 0 )+ (1 - 0)*(f.subs(x,1.5) - (f.subs(x,0)))/( 1.5 - 0)

    return Yint



  def NewtonInerpolation(self,x,y,n,xi,ypred,ea):
    pass

def main():
  I = Interpolation() # Intancia de la clase

  # ========== LNDD_matrix =====================================================
  data=[[2019, 12124],[2021, 5700]]
  year_x=2020 # x (para interpolar)
  print("Population on year {} is".format(year_x), I.LNDD_matrix(data, year_x))

  # ========== LNDD_lists ======================================================
  X = [1,2,3,4,5]
  Y = [11,2.2,3.5,-88,1]
  x_to_int = 2.5
  y_int = I.LNDD_lists(X,Y,x_to_int)
  print("\nValue of y at x = " + str(y_int))

  # ========== LNDD_fun ======================================================
  x0 = 0 # Solo de referencia, subs requiere valores num
  x1 = 1.5
  x2int = 1
  y_intp = I.LNDD_fun(x0, x1, x)
  print("\nValue of y at x = " + str(y_intp))


if __name__ == "__main__":
  main()
