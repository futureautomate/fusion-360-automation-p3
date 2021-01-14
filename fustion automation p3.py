# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:10:01 2020

@author: Tejas
"""
import pyautogui
import time 

#while True:
#    time.sleep(1)    
#    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#    print(currentMouseX, currentMouseY)

time.sleep(2)
pyautogui.moveTo(185, 114, 5) # Move the mouse to XY coordinates.
pyautogui.click() #select sketch

time.sleep(2)
pyautogui.moveTo(903, 578, 5) # Move the mouse to XY coordinates.
pyautogui.click() #select the plane

option = input("Enter your selection\n1)Line\n2)Rectangle\n3)Circle\n")
if option == "1":
    time.sleep(2)
    pyautogui.moveTo(198, 118, 5) # Move the mouse to XY coordinates.
    pyautogui.click() #Select Line
if option == "2":
    time.sleep(2)
    pyautogui.moveTo(240, 125, 5) # Move the mouse to XY coordinates.
    pyautogui.click() #Select Rectangle
if option == "3":
    time.sleep(2)
    pyautogui.moveTo(295, 121, 5) # Move the mouse to XY coordinates.
    pyautogui.click() #Select Circle

time.sleep(2)
pyautogui.moveTo(500, 500,5)
pyautogui.dragTo(700, 700, 1, button='left') 
pyautogui.click() #Draw rectangle

time.sleep(2)
pyautogui.moveTo(1718, 124, 5) # Move the mouse to XY coordinates.
pyautogui.click() #finish sketch

time.sleep(2)
pyautogui.moveTo(340, 163, 5)
pyautogui.click() #click on create menu

time.sleep(2)
pyautogui.moveTo(310, 298, 5)
pyautogui.click() #click on extrude
time.sleep(1)
pyautogui.typewrite('5')

time.sleep(2)
pyautogui.moveTo(1776, 675, 5)
pyautogui.click() #click on ok button

