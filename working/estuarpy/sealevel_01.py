#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 13:31:37 2019

@author: gsolana

Based on:
https://github.com/sam-cox/pytides/wiki/How-to-make-your-own-Tide-Table-using-Python-and-Pytides
https://ocefpaf.github.io/python4oceanographers/blog/2014/07/07/pytides/

"""
import csv
import numpy as np
   
import pandas as pd
from pandas import read_csv, DataFrame
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

from pytides import tide
from pytides import constituent



##Import our tidal data

filepath='../data/sealevel/'




def ibane_deck2017():
    """
    Read and descompese Inhambanes deck tidal gauge seal level serie
    
    
    """

    t = []
    heights = []

    filename='Datos_mareografo_c.csv'
        
    csv_file = open(filepath+filename, 'r')

    reader = csv.reader(csv_file)

    next(reader)
    next(reader)

    for row in reader:
        #print(" ".join(row[:6]))
        a=row[0]+" "+row[1]
        t.append(datetime.strptime(a, "%y/%m/%d %H:%M:%S"))
        heights.append(float((row[3])))

    csv_file.close()
    
    ##Fit the tidal data to the harmonic model using Pytides
    ibaneconst= [ constituent._M2, 
                  constituent._S2, 
                  constituent._N2, 
                  constituent._K2, 
                  constituent._K1, 
                  constituent._O1]
    
    my_tide = tide.Tide.decompose(np.array(heights[::1]), np.array(t[::1]), constituents=ibaneconst)

    return t, heights, my_tide


def readUHSML():
    '''#Read UHSML 2011 dataset


    '''
 

    t = []
    heights = []

    filename2011='Inhambane_2011-07-02_2011-09-27_h900a.csv'

    csv_file2011 = open(filepath+filename2011, 'r')
    reader = csv.reader(csv_file2011, delimiter=',')

    for row in reader:
        tmp = float(row[4])
        if (tmp <= -30000) :
            next(reader)
        else:
            #print(" ".join(row[:6]))
            a=row[0]+"/"+row[1]+"/"+row[2]+" "+row[3]
            t.append(datetime.strptime(a, "%Y/%m/%d %H") - 0*timedelta(hours=1.15))
            heights.append(float((row[4]))/1000)

    csv_file2011.close()

    ##UHSLC Fit the tidal data to the harmonic model using Pytides
    my_tide2011 = tide.Tide.decompose(np.array(heights[::]), np.array(t[::]))


    return t, heights, my_tide2011


def read_otpx():
    """
    
    """
    
    otpx_prediction='/home/gsolana/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/00_Work/00_Python/Datos/tpxo/ibane_predict_OTPX_9v1.out'
    otpx_prediction='ibane_predict_OTPX_9v1.out'

    #Read TPXO Atlas data prediction
    otpx_pred=read_csv(
            filepath+otpx_prediction, 
            sep=r'\s+',
            header=3,
            skiprows=6,
            names=['Lat', 'Lon', 'Date', 'Time', 'Z', 'Depth'], 
            parse_dates = {'date_col' : ["Date", "Time"]}
            )
    #Change date_col to strin to datetime format
    otpx_pred['date_col'] = pd.to_datetime(otpx_pred['date_col'])
    
    ##Fit the tidal data to the harmonic model using Pytides
    OTPX_tide = tide.Tide.decompose(otpx_pred.Z, otpx_pred.date_col)

    return otpx_pred.date_col, otpx_pred.Z, OTPX_tide


   
def saveFig(file=""):
    """ Save the figure
    
    INPUT:
        filename : the complete filename (path + filename + extension)
    
    """


    if file != "":
        plt.savefig('../sample/'+file+'.png', format='png', dpi=300)
        plt.savefig('../sample/'+file+'.pdf', format='pdf', dpi=300, transparent=True)

    

def main():
    """
    
    
    """
    
    

    # Ibane tidal gauge
    ibane_t, ibane_heights, ibane_tide = ibane_deck2017()
    
    constituent = [c.name for c in ibane_tide.model['constituent']]

    df_ibane = DataFrame(ibane_tide.model, index=constituent).drop('constituent', axis=1)


    ##############################################################################
    ##UHSLC Fit the tidal data to the harmonic model using Pytides
    t, heights, UHSLM_tide2011 = readUHSML()

    ##UHSLC Fit the tidal data to the harmonic model using Pytides
    #UHSLM_tide2011 = tide.Tide.decompose(np.array(heights[::]), np.array(t[::]))

    #constituent = [c.name for c in tide.model['constituent']]
    UHSLM_constituent = [c.name for c in UHSLM_tide2011.model['constituent']]

    UHSLM_df2011 = DataFrame(UHSLM_tide2011.model, index=UHSLM_constituent).drop('constituent', axis=1)

    UHSLM_prediction201707 = UHSLM_tide2011.at(ibane_t)
  

    ##############################################################################


    otpx_t, otpx_z, OTPX_tide=read_otpx()

    OTPX_constituent = [c.name for c in OTPX_tide.model['constituent']]

    OTPX_df = DataFrame(OTPX_tide.model, index=OTPX_constituent).drop('constituent', axis=1)

    OTPX_prediction201707=OTPX_tide.at(ibane_t)

    #################################################################################
    

    
    fig = plt.figure(figsize=(6,4))
    
    fig.suptitle('Tidal level',fontsize=9)

    ax2 = plt.subplot()
    
    ax2.grid(b=True, linestyle='-')

    ax2.plot(ibane_t, 
             ibane_heights-df_ibane.amplitude['Z0'],
             "-", 
             c="red", 
             label="2017 Observed Ibane deck")
    
    ax2.plot(ibane_t, 
             UHSLM_prediction201707-UHSLM_df2011.amplitude['Z0'],
             "-", 
             c="blue", 
             label="UHSLC 2017 Modeled")
    
    ax2.plot(ibane_t,
             OTPX_prediction201707-OTPX_df.amplitude['Z0'],
             "-", 
             c="green", 
             label="TPXO Atlas Modeled")
    
    
    ax2.set_xticklabels(ax2.get_xticklabels(),rotation=-45,horizontalalignment='center')

    
    #ax2.set_xlabel('Date')
 
    yrange = (-1.50, 1.5)
    ax2.set_ylim(yrange)
    ax2.set_ylabel('Sea level (m)')

    ax2.legend(loc ='lower center',fontsize=8)
    #plt.tight_layout()
    fig.show()

    saveFig(file='tidalcomparation')


    
if __name__ == "__main__":
    main()
