#!/usr/bin/env octave
% File: recurrence.m
% Name: D.Saravanan
% Date: 06/08/2021
% Script for fibonacci recurrence series

N = 20;

% exact values
e = zeros(N,1);
e(1) = 2.95;
e(2) = 2.95;

% values
a = zeros(N,1);
a(1) = 2.95;
a(2) = 2.95;

% relative error terms
err = zeros(N,1);

for n = 2:N-1
    a(n+1) = a(n) + a(n-1);
    e(n+1) = 2.95 * fibonacci(n+1);
end

for n = 1:N
    err(n) = abs((a(n)-e(n))./e(n));
end

% print relative error terms
disp(err);
