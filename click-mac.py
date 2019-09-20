# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:56:29 2019

@author: amjuli
"""
import pyautogui
import time

for i in range(0,60):
    pyautogui.click(0,0)
    time.sleep(1)
    print('done')