# 
# CLASSS: Gauss
# FUN: GaussElim, Sol
#
# IN: m, z
# OUT: Post Gauss elimination-matrix, Solution to system

# from TrafficAnalyzer import Z, m
import sys

class Gauss():
    def __init__(self, Z, m, f):
        self.Z = Z
        self.m = m
        self.f = f

    def GuassElim(self, Z, m):
        for i in range(m):
            if Z[i][j] == 0.0:
                sys.exit('Not compatible data') # Division by 0
            for j in range(m):
                if i != j:
                    r = Z[j][i] / Z[i][i] #pivot
                    for k in range(m + 1):
                        Z[j][k] = Z[j][k] - r * Z[i][k]
        return Z


    def Sol(self, m, Z, f):
        for i in range(m):
            f[i] = Z[i][m] / Z[i][i]






