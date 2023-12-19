#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:03:16 2023

@author: yildirimgunes
"""

#data_types_structures
#lists[]velist()
numbers=[90,80,70,50]
type(numbers)
dataset1=["a",1,35,10.3,80,["b",2,9],numbers]
len(dataset1)
type(dataset1[6])
combined_list=[numbers,dataset1]
#del combined_list
#elements_of_list
listed=[90,20,40,80,15]
listed[0:2]
listed[2]
listed[2:5]
listeda=["a",90,80,30,[10,20,30]]
listeda
len(listeda)
listeda[4][1]
listedb=["john","jonatha","mike","nikita"]
listedb[1]="jonathan"
listedb
listedb[0:2]="john_bro","jonathan_bro"
listedb
listedb+["joseph"]
listedb=listedb+["joseph"]
listedb
#del listedb[4]
listedb
dir(listedb)
#append_remove
listedb.append("jonny")
listedb
listedb.remove("jonny")
listedb
#insert_pop
listedb.insert(0,"me")
listedb.remove("me")
listedb[0]="me"
listedb
listedb.insert(3,"koyoko")
listedb.insert(7,"tomo")
listedb
len(listedb)
listedb.insert(len(listedb),"klm")
listedb.pop(0)
listedb
listedb.pop(5)
#count
listedb.insert(len(listedb),"john")
listedb.insert(len(listedb),"john")
listedb.insert(0,"john_bro")
listedb.count("john")
#copy
listedb_stepne=listedb.copy()
listedb_stepne
#extend
listedb.extend(["a","b","c"])
listedb
#index
listedb.index("john")
#reverse
listedb.reverse()
listedb
#sort
listedb.sort()
listedb.sort()
listedb
#clear
listedb.clear()
listedb