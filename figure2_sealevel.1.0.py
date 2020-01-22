#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 13:31:37 2019

@author: gsolana

https://github.com/sam-cox/pytides/wiki/How-to-make-your-own-Tide-Table-using-Python-and-Pytides
https://ocefpaf.github.io/python4oceanographers/blog/2014/07/07/pytides/

"""
import numpy as np

import pandas as pd
from pandas import read_csv, DataFrame
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from pytides import tide




##Import our tidal data

filepath='/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/2017 paper/Graficos/Datos'

filename2011='/mares/Inhambane_2011-07-02_2011-09-27_h900a.csv'




otpx_prediction='/home/gsolana/Downloads/OTPSnc/ibane_predict_OTPX_9v1.out'


def ibane_deck2017():
    """
 
    
    
    """
    import csv

    t = []
    heights = []

    filepath='/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/2017 paper/Graficos/Datos'
    filename='/mareografo/Datos_mareografo_c.csv'
        
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
    #my_tide = Tide.decompose(np.array(heights[::1]), np.array(t[::1]), constituents=ibane)
    #conts
    #my_tide = tide.Tide.decompose(np.array(heights[::1]), np.array(t[::1]), constituents=ibane)

    return t, heights, my_tide


def readUHSML():
    '''#Read UHSML 2011 dateseirgh


    '''
    filepath='/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/2017 paper/Graficos/Datos'
    filename2011='/mares/Inhambane_2011-07-02_2011-09-27_h900a.csv'

    t = []
    heights = []

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
    #my_tide2011 = tide.Tide.decompose(np.array(heights[::]), np.array(t[::]))


    return t, heights, my_tide2011


def read_otpx():
    """
    
    """
    
    #otpx_prediction='/home/gsolana/Downloads/OTPSnc/ibane_predict_OTPX_9v1.out'

    #Read TPXO Atlas data prediction
    otpx_pred=read_csv(
            otpx_prediction, 
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


def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        for tl in ax.get_xticklabels() + ax.get_yticklabels():
            tl.set_visible(False)
    return

def format_axes(axes):
    # Plot each axes
    for ax in axes:    # "enumerate(axes.ravel()):
        ax.set_ylim(yrange)
        ax.set_ylabel('Sea level (m)')
       
        ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

        ax.plot(sorted(randint(0,10,10)), sorted(randint(0,10,10)), marker=markers[i], color=colors[i])  
        ax.set_title('Ax: ' + str(i))
        ax.yaxis.set_ticks_position('none')

def print_constitues(df_constituents):
    #df2011 = DataFrame(my_tide2011.model, index=constituent).drop('constituent', axis=1)
    #
    print(df_constituents.sort_values('amplitude', ascending=False).head(20))


def join_constitunt(df1, df2, df3):
    #df1=df1.sort_values
    #df2=df2.sort_values
    
    return pd.concat([df1,df2, df3], axis=1, sort=False)

    

#a=join_constitunt(UHSLM_df2011,OTPX_df)

total_const=pd.concat([UHSLM_df2011,OTPX_df,df_ibane], axis=1, sort=False)

total_const.to_excel("constituentes.xls")

def plot_ibane():
    
    fig4, ax4 = plt.figure(figsize=(10,3),constrained_layout=True)
    
    fig4, ax4 = plt.subplots(2, 1,figsize=(10,3), sharex=True)
    fig4.subplots_adjust(hspace=0)

    fig4.suptitle("Comparison of Observed and UHSLC dataset predictions",fontsize=8)

    
    
    
    ax4.set_title('b) 30/07 to 06/08 comparation', fontsize=9)
    ax4.grid(b=True, linestyle='-')

    ax4[0].plot(ibane_t, ibane_heights-df_ibane.amplitude['Z0'],"-", c="red")
    ax4[0].plot(ibane_t, UHSLM_prediction201707-UHSLM_df2011.amplitude['Z0'],"-", c="blue")
    ax4[0].plot(ibane_t, OTPX_prediction201707-OTPX_df.amplitude['Z0'],"-", c="green")

    xrange = (ibane_t[0], ibane_t[-1])
    ax4[0].set_xlim(xrange)

    yrange = (-2.0, 2.0)
    ax4[0].set_ylim(yrange)
    ax4[0].set_ylabel('Sea level (m)',fontsize=9)

    ax4[0].grid(b=True, linestyle='-')

    fig4.legend()
    fig4.show()

    fig4.savefig('../../figura_tydes1.png', format='png', dpi=300, transparent=True)



def plotObserved():
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
    UHSLM_tide2011 = tide.Tide.decompose(np.array(heights[::]), np.array(t[::]))

    #constituent = [c.name for c in tide.model['constituent']]
    UHSLM_constituent = [c.name for c in UHSLM_tide2011.model['constituent']]

    UHSLM_df2011 = DataFrame(UHSLM_tide2011.model, index=UHSLM_constituent).drop('constituent', axis=1)



    ##############################################################################


    otpx_t, otpx_z, OTPX_tide=read_otpx()

    OTPX_constituent = [c.name for c in OTPX_tide.model['constituent']]

    OTPX_df = DataFrame(OTPX_tide.model, index=OTPX_constituent).drop('constituent', axis=1)

    #################################################################################
    
    
    
    fig = plt.figure(figsize=(6,3))
    
    fig.suptitle('Tidal level',fontsize=9)


    #ax2 = plt.subplot(gs[1, :])
    ax2 = plt.subplot()
    
    #ax2.set_title('b) 2017/07/30 to 2017/08/06 comparation', fontsize=9)
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
             label="OTPX Atlas Modeled")
    
    
    #xrange = np.arange(ibane_t[0], ibane_t[-1], 5)
    #ax2.set_xlim(xrange)
    #ax2.set_xticklabels(xrange, rotation=70, horizontalalignment='right')
    
    #xticks(np.arange(12), calendar.month_name[1:13], rotation=20)


    ax2.set_xticklabels(ax2.get_xticklabels(),rotation=-45,horizontalalignment='center')

    
    
    #ax2.set_xlabel('Date')
 
    yrange = (-1.50, 1.5)
    ax2.set_ylim(yrange)
    ax2.set_ylabel('Sea level (m)')

    ax2.legend(loc ='lower center',fontsize=8)
    plt.tight_layout()
    fig.show()

    saveFig(file='../../tidalcomparation2.png')


    


def main():

    plotObserved()
    
    return





#################################################################################


"""
# initializing K 
#K = timedelta(hours=0.70)
K = timedelta(hours=0)
  
# using list comprehension 
# adding K to each element 
res = [x + K for x in otpx_t]
prediction2011 =  my_tide2011.at(res)
"""
##############################################################################
# Modeling 2017 data

# time serie
t0 = datetime(2017, 1, 1)
tf = datetime(2017, 12, 1)
t2017 = np.arange(t0, tf, timedelta(hours=2)).astype(datetime)

UHSLM_prediction2017 =  UHSLM_tide2011.at(t2017)
OTPX_prediction2017 =  OTPX_tide.at(t2017)

# Modeling July 2017 data

# time serie
ibane_t
UHSLM_prediction201707 = UHSLM_tide2011.at(ibane_t)
OTPX_prediction201707=OTPX_tide.at(ibane_t)




##########################################################################
#https://matplotlib.org/users/gridspec.html

#fig = plt(figsize=(100,50), sharex=True)

#fig.suptitle("Observed UHSLC Historic dataset and OTPX Modeled sea levelp")

fig = plt.figure(figsize=(100,50),constrained_layout=True)
#fig.suptitle("Observed Ibane Deck vs UHSLC Modeles and OTPX Modeled sea level", fontsize=20)

gs = gridspec.GridSpec(3, 3, figure=fig)


ax1 = plt.subplot(gs[0, :])
ax1.set_title('a) 2017 year comparation', fontsize=10)
ax1.grid(b=True, linestyle='-')


ax1.plot(t2017, UHSLM_prediction2017-UHSLM_df2011.amplitude['Z0'],"-", c="blue", label="UHSLC 2017 Modeled")
ax1.plot(t2017, OTPX_prediction2017-OTPX_df.amplitude['Z0'],"-", c="green", label="OTPX Atlas Modeled")
ax1.plot(ibane_t, ibane_heights-df_ibane.amplitude['Z0'],"-", c="red", label="2017 Observed Ibane deck")

ax1.axvline(ibane_t[0], ls='--', color='r')
ax1.axvline(ibane_t[-1], ls='--', color='r')

xrange = (t2017[0], t2017[-1])
ax1.set_xlim(xrange)

yrange = (-2.0, 2.0)
ax1.set_ylim(yrange)
ax1.set_ylabel('Sea level (m)')



ax2 = plt.subplot(gs[1, :])
ax2.set_title('b) 2017/07/30 to 2017/08/06 comparation', fontsize=10)
ax2.grid(b=True, linestyle='-')

ax2.plot(ibane_t, ibane_heights-df_ibane.amplitude['Z0'],"-", c="red")
ax2.plot(ibane_t, UHSLM_prediction201707-UHSLM_df2011.amplitude['Z0'],"-", c="blue")
ax2.plot(ibane_t, OTPX_prediction201707-OTPX_df.amplitude['Z0'],"-", c="green")

xrange = (ibane_t[0], ibane_t[-1])
ax2.set_xlim(xrange)

yrange = (-2.0, 2.0)
ax2.set_ylim(yrange)
ax2.set_ylabel('Sea level (m)')



ax3 = plt.subplot(gs[2, 0])            #.grid(True, linewidth=0.7, linestyle=':')

t1=50
t2=200
n=6
ax2.axvline(ibane_t[t1], ls='--', color='r')
ax2.axvline(ibane_t[t2], ls='--', color='r')

ax3.set_title('c) 30/07 to 06/08 comparation', fontsize=10)


ax3.plot(ibane_t[t1:t2:n], ibane_heights[t1:t2:n]-df_ibane.amplitude['Z0'],"-", c="red" )
ax3.plot(ibane_t[t1:t2:n], UHSLM_prediction201707[t1:t2:n]-UHSLM_df2011.amplitude['Z0'],"-", c="blue")
ax3.plot(ibane_t[t1:t2:n], OTPX_prediction201707[t1:t2:n]-OTPX_df.amplitude['Z0'],"-", c="green")

xrange = (ibane_t[t1], ibane_t[t2])
ax3.set_xlim(xrange)
ax3.set_xticklabels(ax3.get_xticklabels(),rotation=60,horizontalalignment='right')

yrange = (-2.0, 2.0)
ax3.set_ylim(yrange)
ax3.set_ylabel('Sea level (m)')

ax3.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)


ax4 = plt.subplot(gs[2, 1])
         
t3=350
t4=550
n=6

ax2.axvline(ibane_t[t3], ls='--', color='r')
ax2.axvline(ibane_t[t4], ls='--', color='r')

ax4.set_title('d) 30/07 to 06/08 comparation', fontsize=10)

ax4.plot(ibane_t[t3:t4:n], ibane_heights[t3:t4:n]-df_ibane.amplitude['Z0'],"-", c="red")
ax4.plot(ibane_t[t3:t4:n], UHSLM_prediction201707[t3:t4:n]-UHSLM_df2011.amplitude['Z0'],"-", c="blue" )
ax4.plot(ibane_t[t3:t4:n], OTPX_prediction201707[t3:t4:n]-OTPX_df.amplitude['Z0'],"-", c="green")

xrange = (ibane_t[t3], ibane_t[t4])
ax4.set_xlim(xrange)
ax4.set_xticklabels(ax4.get_xticklabels(),rotation=60,horizontalalignment='right')

yrange = (-2.0, 2.0)
ax4.set_ylim(yrange)
ax4.set_ylabel('Sea level (m)')

ax4.grid(b=True,linestyle='-')



ax5 = plt.subplot(gs[2, 2])

t5=-300
t6=-100
n=6

ax2.axvline(ibane_t[t5], ls='--', color='r')
ax2.axvline(ibane_t[t6], ls='--', color='r')

ax5.set_title('e) 30/07 to 06/08 comparation', fontsize=10)


ax5.plot(ibane_t[t5:t6:n], ibane_heights[t5:t6:n]-df_ibane.amplitude['Z0'],"-", c="red" )
ax5.plot(ibane_t[t5:t6:n], UHSLM_prediction201707[t5:t6:n]-UHSLM_df2011.amplitude['Z0'],"-", c="blue")
ax5.plot(ibane_t[t5:t6:n], OTPX_prediction201707[t5:t6:n]-OTPX_df.amplitude['Z0'],"-", c="green" )

xrange = (ibane_t[t5], ibane_t[t6])
ax5.set_xlim(xrange)
ax5.set_xticklabels(ax5.get_xticklabels(),rotation=60,horizontalalignment='right')

yrange = (-2.0, 2.0)
ax5.set_ylim(yrange)
ax5.set_ylabel('Sea level (m)')

ax5.grid(b=True, linestyle='-')

fig.legend()
fig.show()

#########################################################################
#########################################################################
#########################################################################
#########################################################################
