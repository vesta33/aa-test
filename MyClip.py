__author__ = 'anastassias'
import os

#python MyClip.py kopeerib clipboardi programmi output
def addToClipBoard():

    command = 'python Isikukood_new.py | clip'
    os.system(command)

#example
addToClipBoard()