# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:56:29 2019

@author: amjuli
"""
import win32api, win32con,win32gui
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    

for i in range(0,60):
    click(1310,1007)
    time.sleep(60)