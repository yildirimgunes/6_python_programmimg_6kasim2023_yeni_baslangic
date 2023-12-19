#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:31:50 2023

@author: yildirimgunes
"""

#dictionaries
dic={"CLASS":"pos",
     "NEG":"neg",
     "NO":"notr"}
dic
len(dic)
dic={"CLASS":40,
     "NEG":50,
     "NO":60}
dic={"CLASS":[10, "a","b","c"],
     "NEG":["d","e","f",50],
     "NO":[60,"j","k","l","m"]}
dic
dic["NO"]
dic={"CLASS":{"CL":10, 
              "a":20,
              "b":30,
              "c":40},
     "MULTI":{"ML":10,
              "a":20,
              "b":30,
              "c":40},
     "NO":[60,"j","k","l","m"]}
     
dic["MULTI"]
dic["MULTI"]["a"]
dic["MULTI"]={"ML":30}
dic["MULTI"]
dic["XGB"]="extreme"

l=[1]
dic[l]=12
t=(12,)
dic["t"]=32