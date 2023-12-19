#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:21:46 2023

@author: yildirimgunes
"""

#sets_unique_elements
s=set()
l=[1,"a",2,"c",3]
s=set(l)
len(s)
t=("k","l")
s=set(t)
j="john_is_going_to_school"
type(j)
s=set(j)
s
l=["l","m","n","l","m","n",1,2,3,4,1,2,3,4,1]
len(l)
s=set(l)
s
len(s)
l=["pencil", "pen"]
s=set(l)
dir(s)
s.add("notebook")
s
s.add("notebook")
s
s.remove("notebook")
s.discard("notebook")
s.discard("notebook")
s
# =============================================================================
# difference_intersection_union_symmetric_difference
# =============================================================================
set1=set([1,3,5])
set2=set([1,2,3])
set1.difference(set2)
set2.difference(set1)
set1.symmetric_difference(set2)
set1-set2
set2-set1
set1.intersection(set2)
set1.union(set2)
set1&set2
set1.intersection_update(set2)
set1
set1=set([7,8,9])
set2=set([5,6,7,8,9,10])
#isdisjoint_issubset_issuperset
set1.isdisjoint(set2)
set1.issubset(set2)
set2.issubset(set1)
set2.issuperset(set1)