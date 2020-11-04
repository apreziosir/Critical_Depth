# ==============================================================================
# Python functions to estimate critical depth of prismatic channel sections
# using Froude number
# Antonio Preziosi-Ribero
# Universidad Santo Tomas
# November 2020
# ==============================================================================

# Importing useful libraries
import numpy as np

# Function to estimate critical depth of triangular cross-section
def Triang(Q,m):

    yc = ((2 * Q ** 2) / (m ** 2 * 9.81)) ** 0.2

    return yc

# Function to estimate critical depth of rectangular cross-section
def Rect(Q, b):

    yc = ((Q ** 2) / (b ** 2 * 9.81)) ** (1 / 3)

    return yc

# Function to estimate critical depth of trapezoidal section

def Trapez(Q, b, m):

    # Setting values for iterations
    err = 1e6
    tol = 1e-4

    # Assuming an initial value for yc to iterate
    y0 = 1.5

    # Looping over the function to get yc
    while err > tol:

        # Estimating value of yc with formula
        y1 = (1 / (b + m * y0)) * ((b + 2 * m * y0) / 9.81 ) ** (1/3)

        # Error calculation
        err = np.abs(y1 - y0) / y0

        # Updating seed value for iteration
        y0 = y1

    # Making the result equal to yc
    yc = y1

    return yc

# Function to estimate critical depth of circular section
def Circ(Q, d0):

    # First, the critical angle is found and then its value is translated to
    # critical depth using the known formula

    # Values for iteration
    tol = 1e-4
    err = 100
    theta0 = np.pi / 2

    # Constant denominator value
    DENOM = (Q ** 2) * (8 ** 3)
    K1 = 9.81 * d0 ** 5

    # Looping to get critical angle
    while err > tol:

        # Estimating nuew value of theta
        NUM = K1 * (2 * theta0 - np.sin(2 * theta0)) ** 2
        theta1 = np.arcsin(NUM / DENOM)

        # Calculating error
        err = np.abs(theta0 - theta1) / theta0

        # Getting new value of theta
        theta0 = theta1

    # Getting yc:
    yc = (d0 / 2) * (1 - np.cos(theta1))

    return yc
