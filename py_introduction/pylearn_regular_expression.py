#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 18:08:51 2018

@author: thanhpn7
"""
address = '470 DAI MO MAIN ROAD'
print(address)

modified_address = address.replace('ROAD', 'RD.')
print(modified_address)

address = '470 DAI MO BROAD ROAD'
print(address)
modified_address = address.replace('ROAD', 'RD.')
print(modified_address)

import re
modified_address = re.sub('ROAD$', 'RD.', address)
print(modified_address)