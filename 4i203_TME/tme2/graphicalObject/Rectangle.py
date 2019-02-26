'''
Created on 26 févr. 2019

@author: Thibaut SIMON-FINE
'''
from tme2.graphicalObject.SimpleGraphObject import SimpleGraphObject
from PyQt5.QtCore import QRect

class Rectangle(SimpleGraphObject,QRect):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        