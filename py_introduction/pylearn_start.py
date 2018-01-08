# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:10:16 2017

@author: THANHPN7
"""

def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.
    Return string."""
    return ";".join(["%s=%s" % (i,j) for i, j in params.items()])

if __name__ == "__main__":
    """Module test suite.
    Run directly inside module code."""
    myParams = {"server":"mpilgrim", \
                "database":"master", \
                "uid":"sa", \
                "pwd":"secret" \
                }
    print(buildConnectionString(myParams))
