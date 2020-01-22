#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:37:39 2019

@author: gsolana

https://python.swaroopch.com/modules.html

"""

class TidalGauge:
    """ Module examplo
    
    
    """
    
    __version__=0.1
  
    

    def __init__(self, filepath=True):
        """ Tidal Gauge data set analise
        
        
        """
        import os
        
        self.filepath=os.getcwd()
        

    def __repr__(self):
        """
        
        """
        return "Tidal gauge data set"
        
        
 