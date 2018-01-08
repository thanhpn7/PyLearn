# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:02:38 2017

@author: THANHPN7
"""

"""Define list"""
li = ["a", "b", "c", 1, 2]
print(li)

"""Access list's elements"""
print("\r\n**** Access list ****")
print(li[1])
print(li[-1])

"""Slicing list"""
print("\r\n**** Slice list ****")
print(li[0:3])
print(li[1:-1])
print(li[:3])
print(li[3:])
print(li[:])

"""Add element to list"""
print("\r\n**** Add element to list ****")
li.append([4, 5])
print(li)
li.insert(2, "new_insert")
print(li)
li.extend(["new_extend1", "new_extend2"])
print(li)

li_new = ["a", "b", "c", "d", "e", "f"]
li = li + li_new
print(li)

"""Get list size"""
print("\r\n**** Get list size ****")
print("List size:", li.count('a'))

""""Search element in list"""
print("\r\n**** Search element in list ****")
print(li.index("a"))
print("c" in li)

"""" Remove element from list"""
print("\r\n**** Remove element from list ****")
li.remove("a")
print(li)
print(li.pop())
print(li)
