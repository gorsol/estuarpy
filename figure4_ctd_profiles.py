#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:49:29 2019

@author: gsolana

https://oceanpython.org/2013/02/11/plot-a-ctd-profile/

https://ocefpaf.github.io/python4oceanographers/blog/2013/07/29/python-ctd/
https://matplotlib.org/3.1.1/tutorials/introductory/lifecycle.html#sphx-glr-tutorials-introductory-lifecycle-py

"""

# Extract data from file *********************************
import numpy as np
import os
import pandas as pd
import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import axes_grid1

from scipy.interpolate import interp1d

max_depth=6.75
max_depth=6.75
data_range=[15,-15]
ylim=[0, max_depth]
xmark=[33]

#salinity_xlim=[32, 33.5]
salinity_xlim=[30, 35]
temperature_xlim=[22, 23]

xlim=temperature_xlim
xlim=[30, 34]

    
def read2017():
    """
    
    
    """
    
 
    # Files path
    filepath="/home/gsolana/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/2017 paper/Graficos/Datos/ctd/20170718/"
    #filepath="/home/gsolana/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/2017 paper/Graficos/Datos/ctd/20190204/"

    max_depth=6.75
    data_range=[15,-15]
    ylim=[0, max_depth]
    xmark=[33]

    salinity_xlim=[32, 33.5]
    temperature_xlim=[22, 23]

    xlim=temperature_xlim

    # Get data files
    files=os.listdir(filepath)

    # Remove bad data set 2017
    files.remove('inhambane 180717_64.txt')



    files.sort()

    # Create a dpeth grip
    depth_grid=np.arange(0, max_depth, 0.05, float)

    salinity_data_grid=np.zeros([depth_grid.shape[0], len(files)])

    temperature_data_grid=np.zeros([depth_grid.shape[0], len(files)])

    time_list=[]
    time_line=np.zeros([len(files)])


    i=0

    for file in  files:
        # Read data from files
        read_data= pd.read_csv(filepath+file,
                    skiprows = 1,
                    sep = ';',
                    header = 0) 

        f_salinity= interp1d(np.array(read_data.sort_values(by='Press')['Press']), 
                np.array(read_data.sort_values(by='Press')['Sal.']), 
                kind='linear', 
                bounds_error=False, 
                assume_sorted=False)

        salinity_data_grid[:,i]=f_salinity(depth_grid)


        f_temperature= interp1d(np.array(read_data.sort_values(by='Press')['Press']), 
                np.array(read_data.sort_values(by='Press')['Temp']), 
                kind='linear', 
                bounds_error=False, 
                assume_sorted=False)
    
        temperature_data_grid[:,i]=f_temperature(depth_grid)
    
        # Get profile time as datetime objkect
        read_time = dt.datetime.strptime(read_data['Date'][0] + "  " + read_data['Time'][0], '%d/%m/%Y %H:%M:%S')

        #time_list.append(read_time)
        time_list.append(read_data['Time'][0])

        # Converta datatime object to timestamp and punt into time_line
        time_line[i]= dt.datetime.timestamp(read_time)

        i +=1

    data_grid=temperature_data_grid

    return (salinity_data_grid, temperature_data_grid)


def read2019():
    """
    
    
    
    """
    # Files path
    #filepath="/home/gsolana/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/2017 paper/Graficos/Datos/ctd/20170718/"
    filepath="/home/gsolana/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/2017 paper/Graficos/Datos/ctd/20190204/"

    max_depth=6.75
    data_range=[15,-15]
    ylim=[0, max_depth]
    xmark=[33]

    #salinity_xlim=[32, 33.5]
    salinity_xlim=[30, 35]

    temperature_xlim=[22, 23]

    xlim=temperature_xlim

    # Get data files
    files=os.listdir(filepath)

    # Remove bad data set 2017
    #files.remove('inhambane 180717_64.txt')
    #Remove bad data set 2019
    files.remove('040219.txt')
    files.remove('040219_31.txt')     # there aren't valid results    
    

    files.sort()

    # Create a dpeth grip
    depth_grid=np.arange(0, max_depth, 0.05, float)

    salinity_data_grid=np.zeros([depth_grid.shape[0], len(files)])

    temperature_data_grid=np.zeros([depth_grid.shape[0], len(files)])

    time_list=[]
    time_line=np.zeros([len(files)])
    

    i=0

    for file in  files:
        # Read data from files
        read_data= pd.read_csv(filepath+file,
                    skiprows = 1,
                    sep = ';',
                    header = 0) 

        f_salinity= interp1d(np.array(read_data.sort_values(by='Depth')['Depth']), 
                np.array(read_data.sort_values(by='Depth')['Sal.']), 
                kind='linear', 
                bounds_error=False, 
                assume_sorted=False)
        

        salinity_data_grid[:,i]=f_salinity(depth_grid)


        f_temperature= interp1d(np.array(read_data.sort_values(by='Depth')['Depth']), 
                np.array(read_data.sort_values(by='Depth')['Temp']), 
                kind='linear', 
                bounds_error=False, 
                assume_sorted=False)
    
        temperature_data_grid[:,i]=f_temperature(depth_grid)
    
        # Get profile time as datetime objkect
        read_time = dt.datetime.strptime(read_data['Date'][0] + "  " + read_data['Time'][0], '%d/%m/%Y %H:%M:%S')

        #time_list.append(read_time)
        time_list.append(read_data['Time'][0])

        # Converta datatime object to timestamp and punt into time_line
        time_line[i]= dt.datetime.timestamp(read_time)

        i +=1

    data_grid=temperature_data_grid

    return (salinity_data_grid,data_grid)

def forceAspect(ax,aspect):
    font = {'family':'verdana','size':8 }
    matplotlib.rc('font', **font)

    im = ax.get_images()
    extent =  im[0].get_extent()

    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)

    ax.set_xlabel('Time (GMT)', fontsize='8')
    
    #datetime.fromtimestamp(timestamp)
    
    ax.set_ylabel('Depth (m)')
    
    #this reverses the yaxis (i.e. deep at the bottom)
    ax.set_ylim(ylim[::-1]) 

def AxesAspect2017(ax):
    """ Format Axes
    
    IMPUT: ax object
    """
    #ax.set_title("Salinity profile's tidal variation \n (2017/07/18)", fontsize=10)
    font = {'family':'verdana','size':8 }
    matplotlib.rc('font', **font)

    
    ax.grid(False)
    
    #ax.set_xlabel('Time (GMT)', fontsize='8')
    ax.set_ylabel('Depth (m)', fontsize='8')
    
    #this reverses the yaxis (i.e. deep at the bottom)
    ax.set_ylim(ylim[::-1]) 
    
    #x_labels=['6:09:45','8:09:25','10:011:27', '12:05:46',
    #        '14:04:34','16:06:20','18:02:53']

    x_labels=['6:00','8:00','10:00','12:00',
           '14:00','16:00','18:00']

    ax.set_xticklabels(x_labels, rotation=-45, ha='left', fontsize='8')


    # Draw flood-tide and edd-tide lines
    ax.vlines(3.75, 0, 1, transform=ax.get_xaxis_transform(),  ls='--', colors='w')
    ax.text(3.75, 6.25, 'High tide', size=8, ha='center', va='center', color='k')

    ax.vlines(9.75, 0, 1, transform=ax.get_xaxis_transform(),  ls='--', colors='w')
    ax.text(9.75, 6.25, 'Low tide', size=8, ha='center', va='center', color='k',  fontsize='8')
    
def AxesAspect2019(fig, img2, ax):
    """ Format Axes
    
    IMPUT: ax object
    """
    #ax.set_title("Salinity profile's tidal variation \n (2017/07/18)", fontsize=10)
    font = {'family':'verdana','size':8 }
    matplotlib.rc('font', **font)

    
    ax.grid(False)
    
    #ax.set_xlabel('Time (GMT)', fontsize='8')
    ax.set_ylabel('Depth (m)', fontsize='8')
    
    #this reverses the yaxis (i.e. deep at the bottom)
    ax.set_ylim(ylim[::-1]) 
    
    #x_labels=['6:09:45','8:09:25','10:011:27', '12:05:46',
    #        '14:04:34','16:06:20','18:02:53']

    x_labels=['6:00','8:00','10:00','12:00',
           '14:00','16:00','18:00']

    ax.set_xticklabels(x_labels, rotation=-45, ha='left', fontsize='8')

    
    divider = axes_grid1.make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.1)
    
      # Define colorbar caractheristics
    cbar_tics = np.linspace(xlim[0], xlim[1], 6, endpoint=True)
    img2.set_clim(xlim[0], xlim[1])

    # Define colorbar caractheristics
    cbar_tics = np.linspace(xlim[0], xlim[1], 6, endpoint=True)
    
    #cbar = plt.colorbar(img, ax=ax3, ticks=cbar_tics)
    cbar=fig.colorbar(img2, cax=cax, ticks=cbar_tics)
    cbar.set_label('uniform')
    cbar.set_label('Salinity (PSU)', fontsize='8')

    # Tidal lines
    # Draw flood-tide and edd-tide lines
    ax.vlines(3.95, 0, 1, transform=ax.get_xaxis_transform(),  ls='--', colors='w')
    ax.text(3.95, 6.25, 'Low tide', size=8, ha='center', va='center', color='k')

    ax.vlines(10.25, 0, 1, transform=ax.get_xaxis_transform(),  ls='--', colors='w')
    ax.text(10.25, 6.25, 'High tide', size=8, ha='center', va='center', color='k',  fontsize='8')
    

    
def PlotContour(var, ax, data, extent, smoothed=True):
    """ Plot contour iso lines
    IMPUT:
        var -> string  "sal" ou "temp"
        data
        ax  -> subplot axe   ax1 or 
    
    
    """
    import scipy.ndimage as ndimage
    
    if var == "sal":
        #ax=ax1
        levels = np.arange(30.0, 35.0, 0.1)
        sigma=0.75
    elif var == "temp":
        #ax=ax3
        levels = np.arange(22.0, 23, 0.05)
        sigma=1
    else:
        print("Incorrect variavel")
    
    #smoothed = False
    
    # Smooth the 500-hPa geopotential height field
    # Be sure to only smooth the 2D field
    # https://unidata.github.io/python-gallery/examples/Smoothing_Contours.html
    
    if smoothed == True:
        smoothed_data = ndimage.gaussian_filter(data, sigma=sigma, order=0)
    else:
        smoothed_data = data
   
    ax.contour(smoothed_data, levels, origin='image', extent=extent, colors='k', linewidths=0.3)   #, origin='image', extent=extent)

    return

    
def saveFig(file=""):
    """ Save the figure
    
    INPUT:
        filename : the complete filename (path + filename + extension)
    
    """


    if file != "":
        plt.savefig('../../'+file+'.png', format='png', dpi=300)
        plt.savefig(file+'.pdf', format='pdf', dpi=150, transparent=True)



def main():
    """
    
    
    """

    
    
  
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1,figsize=(6, 6), constrained_layout=True)
    
    # Define figure title
    #fig3.suptitle("Salinity profile's tidal variation \n (2017/07/18)", fontsize=10)
    fig.suptitle("CTD profile's tidal variation", fontsize=10)
    #
    ax1.set_title('a)- 18 July 2017', fontsize=8)
    ax2.set_title('b)- 4 February 2019', fontsize=8)
    
    extent=[0, 12, max_depth, 0]

    # First subplot    
    
    data2017=read2017()

    img1=ax1.imshow(data2017[0],
                   interpolation='bilinear',    #define sdnmndmanm,n
                   cmap='jet',
                   origin='upper', 
                   extent=extent)
    
    PlotContour('sal', ax1, data2017[0], extent)

    img1.set_clim(xlim[0], xlim[1])
    
    AxesAspect2017(ax1)
    
    divider = axes_grid1.make_axes_locatable(ax1)
    cax = divider.append_axes('right', size='5%', pad=0.1)

    # Define colorbar caractheristics
    cbar_tics = np.linspace(xlim[0], xlim[1], 6, endpoint=True)
   
    cbar=fig.colorbar(img1, cax=cax, ticks=cbar_tics)
    cbar.set_label('uniform')
    cbar.set_label('Salinity (PSU)', fontsize='8')
 




    # Second subplot

    data2019=read2019()
    
    img2=ax2.imshow(data2019[0],
                   interpolation='bilinear',    #define sdnmndmanm,n
                   cmap='jet',
                   origin='upper', 
                   extent=extent)

      
    PlotContour("sal", ax2, data2019[0], extent)

    #xlim=[30, 32.5]


    AxesAspect2019(fig, img2, ax2)
    

    #plt.tight_layout()
    plt.show()

    file="ctd_profile_total"
    saveFig(file=file)

    print("2017: Mean salinity", np.nanmean(data2017[0]))
    print("    : std", np.nanstd(data2017[0]))
    print("    : var", np.nanvar(data2017[0]))

    
    print("2019: Mean salinity", np.nanmean(data2019[0]))
    print("    : std", np.nanstd(data2019[0]))
    print("    : var", np.nanvar(data2019[0]))

if __name__ == "__main__":
    main()
