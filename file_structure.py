# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:09:44 2019

@author: amjuli
"""

import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
        return f
            
f = list_files(r'K:\1. AOG Claims\1. AOG Claims BI\01. BI Products\02. Quarterly Score Card & CTR\CTR\2019\Q2')

f = list