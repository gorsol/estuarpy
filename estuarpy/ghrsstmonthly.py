#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:34:17 2019

@author: gsolana

https://www.afahadabdullah.com/blog/how-to-read-netcdf-file-in-python
https://joehamman.com/2013/10/12/plotting-netCDF-data-with-Python/
https://iescoders.com/reading-netcdf4-data-in-python/


Dataset:
    
    https://thredds.jpl.nasa.gov/thredds/ncss/grid/ncml_aggregation/OceanTemperature/ghrsst/aggregate__ghrsst_JPL_OUROCEAN-L4UHfnd-GLOB-G1SST_OI.ncml/pointDataset.html

"""

# Import quered libraries
import numpy as np

from netCDF4 import Dataset as nc
from netCDF4 import num2date, date2num, date2index

from datetime import datetime, timedelta

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits import axes_grid1

import conda
import os
conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib

from mpl_toolkits.basemap import Basemap

def ncdump(nc_fid, verb=True):
    '''
    ncdump outputs dimensions, variables and their attribute information.
    The information is similar to that of NCAR's ncdump utility.
    ncdump requires a valid instance of Dataset.

    Parameters
    ----------
    nc_fid : netCDF4.Dataset
        A netCDF4 dateset object
    verb : Boolean
        whether or not nc_attrs, nc_dims, and nc_vars are printed

    Returns
    -------
    nc_attrs : list
        A Python list of the NetCDF file global attributes
    nc_dims : list
        A Python list of the NetCDF file dimensions
    nc_vars : list
        A Python list of the NetCDF file variables
    '''
    def print_ncattr(key):
        """
        Prints the NetCDF file attributes for a given key

        Parameters
        ----------
        key : unicode
            a valid netCDF4.Dataset.variables key
        """
        try:
            print( "\t\ttype:", repr(nc_fid.variables[key].dtype))
            for ncattr in nc_fid.variables[key].ncattrs():
                print( '\t\t%s:' % ncattr,
                      repr(nc_fid.variables[key].getncattr(ncattr)))
        except KeyError:
            print( "\t\tWARNING: %s does not contain variable attributes" % key)

    # NetCDF global attributes
    nc_attrs = nc_fid.ncattrs()
    if verb:
        print("NetCDF Global Attributes:")
        for nc_attr in nc_attrs:
            print( '\t%s:' % nc_attr, repr(nc_fid.getncattr(nc_attr)))
    nc_dims = [dim for dim in nc_fid.dimensions]  # list of nc dimensions
    # Dimension shape information.
    if verb:
        print( "NetCDF dimension information:")
        for dim in nc_dims:
            print( "\tName:", dim) 
            print( "\t\tsize:", len(nc_fid.dimensions[dim]))
            print_ncattr(dim)
    # Variable information.
    nc_vars = [var for var in nc_fid.variables]  # list of nc variables
    if verb:
        print("NetCDF variable information:")
        for var in nc_vars:
            if var not in nc_dims:
                print('\tName:', var)
                print("\t\tdimensions:", nc_fid.variables[var].dimensions)
                print("\t\tsize:", nc_fid.variables[var].size)
                print_ncattr(var)
    return nc_attrs, nc_dims, nc_vars
    
   
def readDataset(verb=False):
    """
    
    
    """
    
    
    def verbose():
        """
        
        
        
        """

        # To show the dataset estructure
        #print(dataset.variables)
        
        #read variable 
        
        sst_units = dataset.variables['analysed_sst'].units
        # Chenge temperature escala
        

        #print('units = %s, values = %s' % (time_units, time[:]))

        return    
    
    path="/home/gsolana/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/00_Work/00_Python/Datos/GHRSST/"
    filename="aggregate__ghrsst_JPL_OUROCEAN-L4UHfnd-GLOB-G1SST_OI.ncml.nc"

    base_time = "2010-06-09T12:00:00Z" 

    # Open file in a netCDF reader
    dataset = nc(path+filename, mode='r')
    sst=dataset.variables['analysed_sst'][:][:][:] # ":" takes all the data dimension from the file
    time=dataset.variables['time'][:]
    lon=dataset.variables['lon'][:]
    lat=dataset.variables['lat'][:]
    
    time_units=dataset.variables['time'].units
    dates = num2date(time[:], units=time_units)

    #ncdump(dataset, verb=True)
    
    # Close nc file
    dataset.close()


    #print([datetime.strftime('%Y-%m-%d %H:%M:%S') for datetime in dates[:10]]) # print only first ten...

    #timedim = sfctmp.dimensions[0] # time dim name
    #print('name of time dimension = %s' % timedim)

    # Change SST units
    sst=sst-273
    sst_units='ºC'
 
    return sst, dates, lat, lon


def findPointIndex(point, lat, lon):
    """
    Find the points closest index
    
    INPUT:
        point --> dict point={'lat':-23.6577, 'lon':35.4969}
  
    RETUTN    
        index={'lat':latitudes index , 'lon':longitudes index}
    """
    
    # Find the nearest latitude and longitude for Darwin
    lat_idx = np.abs(lat - point['lat']).argmin()
    lon_idx = np.abs(lon - point['lon']).argmin()

    index={'lat':lat_idx, 'lon':lon_idx}

    return index


def calcMeanValues(C11, sst, dates, lat, lon):
    """
    
    INPUT:
        C11 --> Estation point
        sst
            dates
            
    RETURN
        mean_values ->
        std_values  ->
        
    """
    
    idx=findPointIndex(C11,lat=lat, lon=lon)
 
    sst.mean(axis=(0,1))[0]
    point_mean=sst[:,idx['lat'],idx['lon']].mean()
    
    mean_values=[]
    std_values=[]
    
    january_sst=[]
    february_sst=[]
    march_sst=[]
    may_sst=[]
    april_sst=[]
    june_sst=[]
    july_sst=[]
    august_sst=[]
    september_sst=[]
    outuber_sst=[]
    november_sst=[]
    dezember_sst=[]

    for daily, sst_temp in zip(dates, sst[:,idx['lat'],idx['lon']]):
        index=np.where(dates == daily)[0][0]
            
        #print(daily,  daily.month, index, sst_temp)
        if daily.month == 1:
            january_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 2:
            february_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 3:
            march_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 4:
            may_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 5:
            april_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 6:
            june_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 7:
            july_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 8:
            august_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 9:
            september_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 10:
            outuber_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 11:
            november_sst.append(sst[index,idx['lat'],idx['lon']])
        elif daily.month == 12:
            dezember_sst.append(sst[index,idx['lat'],idx['lon']])
              
    mean_values=[]
    std_values=[]

    files=[january_sst, february_sst, march_sst, may_sst, april_sst, june_sst, 
           july_sst, august_sst, september_sst, outuber_sst, november_sst, 
           dezember_sst]

    for month in files:
        mean_values.append(np.ma.array(month).mean())
        std_values.append(np.ma.array(month).std())

    print(C11, mean_values, std_values)
    return( [mean_values, std_values])

def plotMonthly(ax, point1, point2, point3, legends=""):
    """
    
    
    http://www.atmos.albany.edu/facstaff/brose/classes/ATM623_Spring2015/Notes/Lectures/Lecture15%20--%20Seasonal%20cycle%20and%20heat%20capacity.html
    """

    labels=['Jan', 'Feb', 'Mar', 'May', 'Apr', 'Jun', 
           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    x=np.arange(0,12)

    # Now switch to a more OO interface to exercise more features.
    #https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.errorbar.html
    
    width = 0.30
    yrange = (20, 30)
        
    ax.set_title('Monthly mean SST from 2010/01 to 2019/08')

    ax.set_ylim(yrange)
    ax.bar(x-width*3/3, point1[0], yerr=point1[1], width=width, color='blue', ecolor='red', alpha=0.7, label=legends[0])
    ax.bar(x, point2[0], yerr=point2[1], width=width, color='green', ecolor='red', alpha=0.7, label=legends[1], tick_label=labels)
    ax.bar(x+width*3/3, point3[0], yerr=point3[1], width=width, color='cyan', ecolor='red', alpha=0.7, label=legends[2])

    # 29.01. 28.9, 23.5, 26.64
    
    ax.scatter(1-width*3/3,28.51, color='k', alpha=1 )
    ax.scatter(1,28.4, color='k', alpha=1 )

    ax.scatter(6-width*3/3,23.0, color='k', alpha=1 )
    ax.scatter(6,23.14, color='k', alpha=1 )

    # Draw sst mean  and edd-tide lines
    #ax.hlines(point_mean, -1, 12,  ls='--', colors='k')

    ax.legend(loc='upper center')


    ax.set_ylabel('Temperature (ºC)')
    #ax.set_xlabel(labels)
    ax.set_xticklabels(labels, rotation=45, fontsize=10 )
    # set a title for x-axis
    #ax.set_xlabel("Month")

    plt.tight_layout()

    
    plt.show()
    
    return


def saveFig(fig, file=""):
    """ Save the figure
    
    INPUT:
        filename : the complete filename (path + filename + extension)
    
    """


    if file != "":
        plt.savefig('./sample/'+file+'.png', format='png', dpi=600)
        plt.savefig('./sample/'+file+'.pdf', format='pdf', dpi=600, transparent=True)

    return
   

def main():
    """
    
    
    """
    # Read netCDF file 
    sst, dates, lat, lon = readDataset()

    C6= {'Estation':'C6', 'lat':-23.7925, 'lon':35.3869,  'sst':23.5}
    C8 = {'Estation':'C8','Description':'Canal Central', 'lon':35.4233, 'lat':-23.7400, 'sst':23.64}
    C10 = {'Estation':'C10','Description':'Canal Central', 'lon':35.4483333, 'lat':-23.6811111, 'sst':23.72}
    Outter = {'Estation':'Outter','Description':'Canal Central', 'lon':35.60, 'lat':-23.6577778, 'sst':25.0}

    # Calculate for selected statios the monhly sst mean values and std 
    C6_data=calcMeanValues(C6, sst=sst, dates=dates, lat=lat, lon=lon)
    C8_data=calcMeanValues(C8, sst=sst, dates=dates, lat=lat, lon=lon)
    C10_data=calcMeanValues(C8, sst=sst, dates=dates, lat=lat, lon=lon)

    outter=calcMeanValues(Outter, sst=sst, dates=dates, lat=lat, lon=lon)

    fig, axs = plt.subplots(figsize=(5,3), ncols=1)
    legends=['C6 Station', 'C8 Station', 'Open sea']
    plotMonthly(axs, C6_data, C8_data, outter, legends)
    
    file="sst_monthly_manel"
    saveFig(fig, file)

if __name__ == "__main__":
    main()


