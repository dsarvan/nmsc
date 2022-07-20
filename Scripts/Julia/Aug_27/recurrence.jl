#!/usr/bin/env julia
# File: recurrence.jl
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to compute polynomials using recurrence relations """

# Chebyshev polynomials
function Chebyshev(x, n)
    # recurrence relation of Chebyshev polynomials of first kind
    # T_0 = 1, T_1 = x
    # T_(n+1) = 2 x T_(n) - T_(n-1)
    n == 0 && return 1
    n == 1 && return x
    2x*Chebyshev(x, n-1) - Chebyshev(x, n-2)
end

# Hermite polynomials
function Hermite(x, n)
    # recurrence relation of Hermite polynomials
    # H_0 = 1, H_1 = 2x
    # H_(n+1) = 2 x H_(n) - 2 n H_(n-1)
    n == 0 && return 1
    n == 1 && return 2*x
    2x*Hermite(x, n-1) - 2(n-1)*Hermite(x, n-2)    
end

# Laguerre polynomials
function Laguerre(x, n)
    # recurrence relation of Laguerre polynomials
    # L_0 = 1, L_1 = 1-x
    # (n+1) L_(n+1) = (2n + 1 - x) L_(n) - n L_(n-1)
    n == 0 && return 1
    n == 1 && return 1-x
    ((2(n-1) + 1 - x)*Laguerre(x, n-1) - (n-1)*Laguerre(x, n-2))/n
end

# Legendre polynomials
function Legendre(x, n)
    # recurrence relation of Legendre polynomials
    # P_0 = 1, P_1 = x
    # (n+1)  P_(n+1) = (2n+1) x P_(n) - n P_(n-1)
    n == 0 && return 1
    n == 1 && return x
    ((2(n-1) + 1)*x*Legendre(x, n-1) - (n-1)*Legendre(x, n-2))/n
end
