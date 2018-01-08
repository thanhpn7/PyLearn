#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 09:36:16 2018

@author: thanhpn7
"""

s = 'Dive into Python'
print('String length:', len(s))

s = s + ' 3'
print(s)
print(s.lower().count('d'))

"""Slice a string"""
print("\r\n**** Slicing a string ****")
print('From 3 to 11:', s[3:11])
print('From 3 to -3:', s[3:-3])
print('To 12:', s[:12])
print('To 8:', s[8:])

"""Replace in a string"""
replaced_str = s.replace('Python', 'Perl')
print(replaced_str)
