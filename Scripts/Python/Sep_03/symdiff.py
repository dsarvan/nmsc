#!/usr/bin/env python
# File: symdiff.py
# Name: D.Saravanan
# Date: 01/10/2021

""" Symbolic differentiation in Python """

import sympy as sym

f = sym.symbols('f', cls=sym.Function)
x = sym.symbols('x')

f = x**2 + x/2 - sym.sin(x)/x
print(sym.diff(f, x))
