#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:01:52 2023

@author: yildirimgunes
"""

def multip_num(x,y,z=1):
    m=(x*y*z)+2
    print("numbers_given: "+str(x)+","+str(y)+","+str(z))
    print("conclusion: "+str(m))

multip_num(2,3,4)
multip_num(y=3, x=5, z=8)


def problem(x=1,y=1,z=1):
    m=(x+y)/z
    print("problem_values:"+str(x)+","+str(y)+","+str(z))
    print("problem_conclusion: "+str(m))

problem(22,45,78)