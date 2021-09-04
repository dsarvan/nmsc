#!/usr/bin/env octave
% File: condition.m
% Name: D.Saravanan
% Date: 17/08/2021
% Script to compute condition number of a matrix

N = 20;

A = eye(N) - 10 * diag(ones(N-1, 1), -1) + 9 * diag(ones(N-2, 1), -2);
A(2,1) = 0;

cond_A = cond(A);

disp("Condition number of matrix A:"), disp(cond_A);

B = eye(N) - 1 * diag(ones(N-1, 1), -1) - 1 * diag(ones(N-2, 1), -2);
B(2,1) = 0;

cond_B = cond(B);

disp("Condition number of matrix B:"), disp(cond_B);
