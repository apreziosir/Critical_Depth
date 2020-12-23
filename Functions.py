# ==============================================================================
# Python functions to estimate critical depth of prismatic channel sections
# using Froude number
# Antonio Preziosi-Ribero
# Universidad Santo Tomas
# November 2020
# ============================================================================

# Importing useful libraries
import numpy as np
from Plotting import Plot_Results

# Function to estimate critical depth of triangular cross-section
def Triang(Q, m): 
    
    # Estimando la profundidad crítica para las caracterísitcas dadas
    yc =  ((2 * Q ** 2) / (m ** 2 * 9.81)) ** 0.2
    
    # Vectores donde se almacenará el valor de las diferentes alturas y 
    # energías
    y = np.linspace(0.05, 10, 500)    
    E = np.zeros_like(y)
    
    # Cálculo de la energía específica del caso analizado
    E = y + (Q ** 2) / (2 * 9.81 * m ** 2 * y ** 4)
    
    # Construcción del diccionario que almacenará todo lo que necesito 
    # sacar de la función
    Tri = { "Shape": "Triangular", 
            "m": m,
            "Q": Q,
            "yc": yc,
            "Y": y,
            "E": E
          }
    
    # Llamando función de impresión de resultados y graficado
    Plot_Results(Tri)
        
    return 

# Function to estimate critical depth of rectangular cross-section
def Rect(Q, b): 
    
    # Calculando la altura crítica para caso rectangular
    yc = ((Q ** 2) / (b ** 2 * 9.81)) ** (1 / 3)
    
    # Calculando los arreglos de valores para la curva de energía
    # específica
    Y, E = SE_Trapez(Q, b, 0)
    
    # Construyendo el diccionario que almacena los valores para graficar
    Rect = { "Shape": "Rectangular",
            "b": b,
            "Q": Q,
            "yc": yc,
            "Y": Y,
            "E": E
          }
    # Llamando función de impresión de resultados y graficado
    Plot_Results(Rect)
    
    return

# Function to estimate critical depth of trapezoidal section
def Trapez(Q, b, m):

    # Setting values for iterations
    err = 1e6
    tol = 1e-4

    # Assuming an initial value for yc to iterate
    y0 = 1.0

    # Getting constant value of iterations:
    A = ((Q ** 2) / 9.81) ** (1 / 3)

    # Looping over the function to get yc
    while err > tol:

        # Estimating value of yc with formula
        y1 = A * ((b + 2 * m * y0) ** (1 / 3)) / (b + m * y0)

        # Error calculation
        err = np.abs(y1 - y0) / y0

        # Updating seed value for iteration
        y0 = y1

    # Making the result equal to yc
    yc = y1
    
    # Calculando los arreglos de valores para la curva de energía
    # específica
    Y, E = SE_Trapez(Q, b, m)
    
    # Construyendo el diccionario que tendrá los valores
    Trapez = { "Shape": "Trapezoidal",
            "b": b,
            "m": m,
            "Q": Q,
            "yc": yc,
            "Y": Y,
            "E": E
          }
    # Llamando función de impresión de resultados y graficado
    Plot_Results(Trapez)
    
    return

# Function to estimate critical depth of circular section
def Circ(Q, d0):

    # First, the critical angle is found and then its value is translated to
    # critical depth using the known formula. We are going to use a numerical
    # method to find this value since the simple iteration while solving a
    # trigonometric equation is quite complicated.
    # Using Newtoh-Raphson:

    # Values for iteration
    tol = 1e-4
    err = 100
    theta0 = np.pi / 4

    # Constant value
    B = (8 ** 3 * Q ** 2) / (9.81 * d0 ** 5)

    # Looping to get critical angle
    while err > tol:

        # Value of 2theta0 - sin(2theta0)
        C = 2 * theta0 - np.sin(2 * theta0)

        # Value of f(theta)
        ft = B * np.sin(theta0) / (C ** 3) - 1

        # Value of f'(theta)
        cost = np.sin(theta0) * (2 - 2 * np.cos(2 * theta0))
        fpt = B * (C * np.cos(theta0) - 3 * B * cost) / (C ** 4)

        # Value of new theta
        theta1 = theta0 - ft / fpt

        # Printing for checking purposes
        # print(theta1)

        # Calculating error
        err = np.abs(theta0 - theta1) / theta0

        # Getting new value of theta
        theta0 = theta1

    # Getting yc:
    yc = (d0 / 2) * (1 - np.cos(theta1))
    
    # Encontrado los arreglos de Y y E
    Y, E = SE_Circ(Q, d0)
    
    # Construyendo el diccionario que tendrá los valores
    Circ = { "Shape": "Circular",
            "D0": d0,
            "Q": Q, 
            "yc": yc,
            "Y": Y,
            "E": E
          }
    
    # Plotting function
    Plot_Results(Circ)
    
    return  

# Function to calculate energy and depth for specific discharge trapezoidal
# cross section (a rectangle is a trapezoidal shape with m = 0)
def SE_Trapez(Q, b, m):
    
    # Vectores donde se almacenará el valor de las diferentes alturas y 
    # energías
    y = np.linspace(0.05, 10, 500)    
    E = np.zeros_like(y)
    
    E = y + (Q ** 2) / (2 * 9.81 * ((b + m * y) * y) ** 2)
        
    return y, E

# Function to calculate energy and depth for specific discharge circular
# cross section 
def SE_Circ(Q, d0):
    
    # Vectores donde se almacenará el valor de las diferentes alturas y 
    # energías
    theta = np.linspace(0.001, 3.141592, 500)
    y = (d0 / 2) * (1 - np.cos(theta))    
    E = np.zeros_like(y)
    
    E = y + (32 * Q ** 2) / (d0 ** 4 * (2 * theta - np.sin(2 * theta)) ** 2)    
       
    return y, E


    
    