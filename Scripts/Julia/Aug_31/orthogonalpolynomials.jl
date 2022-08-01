#!/usr/bin/env julia
# File: orthogonalpolynomials.jl
# Name: D.Saravanan
# Date: 01/08/2022

""" Script to compute the orthogonal polynomials """

using Polynomials
using SpecialPolynomials

# Chebyshev polynomials
function Tn(x, n) 
    convert(Polynomial, basis(Chebyshev, n))
end

# Hermite polynomials
function Hn(x, n) 
    convert(Polynomial, basis(Hermite, n))
end

# Laguerre polynomials
function Ln(x, n)
    convert(Polynomial, basis(Laguerre{0}, n))
end

# Legendre polynomials
function Pn(x, n) 
    convert(Polynomial, basis(Legendre, n))
end
