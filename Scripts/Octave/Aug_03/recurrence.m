#!/usr/bin/env octave
% File: recurrence.m
% Name: D.Saravanan
% Date: 03/08/2021
% Script for solving recurrence relation:
% a(n+2) = 10 a(n+1) - 9 a(n), a(1) = 2.95, a(2) = 2.95

N = 20;
a = zeros(N,1);
a(1) = 2.95;
a(2) = 2.95;

for n = 1:N-2
    a(n+2) = 10*a(n+1) - 9*a(n);
end

disp(a)
