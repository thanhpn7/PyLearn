# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:09:12 2017

@author: THANHPN7
"""

"""Define dictionary"""
print("\r\n**** Create list ****")
dict = {"username":"thanhpn7", "pwd":"bao123thy456", "uid": 176854, "addr":"Hanoi"}
print(dict)

"""Change value"""
print("\r\n**** Change key value ****")
dict["username"] = "thanhpn"
print(dict)

"""Add element"""
print("\r\n**** Add element to dict ****")
dict["job"] = "engineer"
print(dict)

"""Copy dictionary"""
print("\r\n**** Copy from dict to other dict ****")
dict_copy = dict.copy()
print(dict_copy)

""""List keys"""
print("\r\n**** List keys ****")
print(dict.keys())

""""List values"""
print("\r\n**** List values ****")
print(dict.values())

"""Get element by key"""
print("\r\n**** Get element by key ****")
print(dict.get("job", "None"));
print(dict.get("gender", "None"));
dict.setdefault("gender", "default")
print(dict)

"""Creat new dictonary with key from list"""
print("\r\n**** Creat new dictonary with key from list ****")
li = ["age", "gender", "heigh"]
dict_new = dict.fromkeys(li, 10)
print(dict_new)

"""Append dict to dict"""
print("\r\n**** Append dict to dict ****")
dict.update(dict_new)
print(dict)

"""Pop element"""
print("\r\n**** Pop element ****")
print(dict.pop("gender", None))
print(dict)

"""Delete element"""
print("\r\n**** Delete element ****")
del dict["addr"]
print(dict)

"""Clear dictionary"""
print("\r\n**** Delete all elements ****")
dict.clear()
print(dict)

