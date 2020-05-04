#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:06:04 2019

@author: gsolana

https://scitools.org.uk/cartopy/docs/v0.14/matplotlib/feature_interface.html

class cartopy.feature.GSHHSFeature(scale='auto', levels=None, **kwargs)[source]

    An interface to the GSHHS dataset.

    See https://www.ngdc.noaa.gov/mgg/shorelines/gshhs.html

    Args:

        scale:

            The dataset scale. One of ‘auto’, ‘coarse’, ‘low’, ‘intermediate’, ‘high, or ‘full’ (default is ‘auto’).

        levels:

            A list of integers 1-4 corresponding to the desired GSHHS feature levels to draw (default is [1] which corresponds to coastlines).

    Kwargs:
        Keyword arguments to be used when drawing the feature. Defaults are edgecolor=’black’ and facecolor=’none’.






"""
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.offsetbox import AnchoredText

from cartopy.io import shapereader



def plotMozambique(ax):
    """ Plot Mozambique map as a subplot
    
    INPUT
    
    
    
    """
    import os
    import conda
    conda_file_dir = conda.__file__
    conda_dir = conda_file_dir.split('lib')[0]
    proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
    os.environ["PROJ_LIB"] = proj_lib
    from mpl_toolkits.basemap import Basemap

    from itertools import chain

    
    #ax = fig.add_axes([.55, .65, .24, .24])
    #ax = fig.add_axes(box)
    ax.set_title("Mozambique",fontsize=9)
    
    
    #Mozambique coordetiantes
    moz_lon_min = 0
    moz_lon_max = 51
    moz_lon_0 = (moz_lon_min + moz_lon_max) / 2.

    moz_lat_min = -37
    moz_lat_max = 0.0 
    moz_lat_0 = (moz_lat_min + moz_lat_max) / 2.
    
            
    #Mozambioqque
    map2 = Basemap(projection='merc', llcrnrlon=moz_lon_min, llcrnrlat=moz_lat_min, \
                   urcrnrlon=moz_lon_max, urcrnrlat=moz_lat_max, lat_0=moz_lat_0, lon_0=moz_lon_0, \
                   resolution='l', ax=ax)

    map2.drawmapboundary()
    map2.drawcoastlines()
    map2.drawstates()
    map2.drawcountries()
    map2.fillcontinents(color='coral',lake_color='aqua',  alpha=0.50)

    # Plot Mozambique contour
    countour_path='/home/gsolana/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/00_Work/00_Python/Datos/mzshape/'
    countout_file='mozambique'
    map2.readshapefile(
            shapefile=countour_path+countout_file, 
            name='Mozambique',
            zorder = 10,
            linewidth=0.1,
            color = 'k', 
            drawbounds = True)
  
    # PLot a red dot in Inhambane
    
    x, y = map2(np.array(35.32), np.array(-23.5))
    map2.scatter(x, y, label='cities_names', marker='o',color='r', norm=1, alpha=1)


    meridians = np.arange(moz_lon_min, moz_lon_max, 10)
    map2.drawmeridians(meridians, linewidth=1, labels=[0, 0, 0, 1], alpha=0.8, color='k',fontsize=8)

    parallels = np.arange(moz_lat_min, moz_lat_max , 10)
    map2.drawparallels(parallels, linewidth=1, labels=[1, 0, 0, 0], alpha=0.8, color='k',fontsize=8)
    
    return


def plotWetlands(ax):
    
    path="/home/gsolana/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/00_Work/00_Python/Datos/"
    wetlands_shp="wetlands_inhambane.shp"
    
    alpha=0.8

    tidalflat=[445335838, 445294087, 6624023, 6625538,6625538, 445288444, 
            445215817, 445215815, 445215810, 6623161, 6623161,445215814,  
            445215812, 445215812, 445215808, 445216534,  445469257, 445469253,
            445469250, 445215816, 445215811, 445215809, 6623243, 445294083, 
            445294082, 6623224, 445329834, 445329853, 445329860, 445329851,
            445335857, 445335854, 445335861, 445329845, 445329830, 445329857,
            445335865, 445335848, 445335851]
    tidalflat.sort()
        
    mangroveis=[9331289,9331296,9331297,9331254, 670923734, 9331090, 9349722, 
                9331084, 9331237, 9331085, 9331085, 9326169, 9326101, 9326100,
                9326102]
    mangroveis.sort()
    
    wetlands = shapereader.Reader(path+wetlands_shp)
    for record, geometry in zip(wetlands.records(), wetlands.geometries()):
        if record.attributes['osm_id'] in str(tidalflat):
            print(record.attributes['osm_id'], record.attributes['name'])
            ax.add_geometries([geometry], ccrs.PlateCarree(), facecolor='chocolate',
                          edgecolor='chocolate', alpha=alpha)
        if record.attributes['osm_id'] in str(mangroveis):
            print(record.attributes['osm_id'], record.attributes['name'])
            ax.add_geometries([geometry], ccrs.PlateCarree(), facecolor='lightgreen',
                          edgecolor='lightgreen', alpha=alpha)

    return   
  
def plotRivers(ax):
 
    path="/home/gsolana/Work/UP_Unisaf/00 PesquisaEXtensao/2017 Modelicacao Baia/00_Work/00_Python/Datos/"
    rivers_shp="gis_osm_waterways_free_1.dbf"
     
    rivers=['232451083','232441738', '670004336']
    
    rivers_file = shapereader.Reader(path+rivers_shp)
    for record, geometry in zip(rivers_file.records(), rivers_file.geometries()):
        if record.attributes['osm_id'] in rivers:
            print(record.attributes['osm_id'], record.attributes['name'])
            ax.add_geometries([geometry], ccrs.PlateCarree(), facecolor='',
                          edgecolor='blue', alpha=0.8)

    return


def plotTrack(ax):
    """
    
    
    
 
    """ 
    import pandas as pd

    url = 'https://zenodo.org/record/3626183/files/20170721_Boya01.csv?download=1'
    
    df = pd.read_csv(url,
                 sep=',',
                 header=7,
                 decimal='.',
                 usecols=[ 1, 2, 3],
                 names=['time', 'lat', 'lon']
                 )

    ax.scatter(df['lon'], df['lat'], alpha=1.0, linewidths=0.3, s=0.5, c='hotpink',  transform=ccrs.Geodetic())  # Plot
    ax.plot(df['lon'][0], df['lat'][0], c='hotpink', marker='o', fillstyle=None, transform=ccrs.Geodetic())
    ax.plot(df['lon'][0], df['lat'][0], c='black', marker='x', transform=ccrs.Geodetic())

    
def scaleBar(ax, length=None, location=(0.5, 0.05), linewidth=3):
    """
    ax is the axes to draw the scalebar on.
    length is the length of the scalebar in km.
    location is center of the scalebar in axis coordinates.
    (ie. 0.5 is the middle of the plot)
    linewidth is the thickness of the scalebar.
    """
    #Get the limits of the axis in lat long
    llx0, llx1, lly0, lly1 = ax.get_extent(ccrs.PlateCarree())
    #Make tmc horizontally centred on the middle of the map,
    #vertically at scale bar location
    sbllx = (llx1 + llx0) / 2
    sblly = lly0 + (lly1 - lly0) * location[1]
    tmc = ccrs.TransverseMercator(sbllx, sblly)
    #Get the extent of the plotted area in coordinates in metres
    x0, x1, y0, y1 = ax.get_extent(tmc)
    #Turn the specified scalebar location into coordinates in metres
    sbx = x0 + (x1 - x0) * location[0]
    sby = y0 + (y1 - y0) * location[1]

    #Calculate a scale bar length if none has been given
    #(Theres probably a more pythonic way of rounding the number but this works)
    if not length: 
        length = (x1 - x0) / 5000 #in km
        ndim = int(np.floor(np.log10(length))) #number of digits in number
        length = round(length, -ndim) #round to 1sf
        #Returns numbers starting with the list
        def scaleNumber(x):
            if str(x)[0] in ['1', '2', '5']: return int(x)        
            else: return scale_number(x - 10 ** ndim)
        length = scale_number(length) 

    #Generate the x coordinate for the ends of the scalebar
    bar_xs = [sbx - length * 500, sbx + length * 500]
    #Plot the scalebar
    ax.plot(bar_xs, [sby, sby], transform=tmc, color='k', linewidth=linewidth)
    #Plot the scalebar label
    ax.text(sbx, sby, str(length) + ' km', transform=tmc,
            horizontalalignment='center', verticalalignment='bottom')

def plotGridLines(ax):
    """
    
    
    """

    import matplotlib.ticker as mticker
    from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle='--')

    gl.xlocator = mticker.FixedLocator([35.25, 35.35, 35.45, 35.55, 35.65])
    gl.xlines = True
    gl.xlabels_top = False
    gl.xlabels_bottom = True
    gl.xformatter = LONGITUDE_FORMATTER
    gl.xlabel_style = {'size': 8, 'color': 'black'}

    gl.ylocator = mticker.FixedLocator([-24.10, -24, -23.90,-23.80, -23.70, -23.60])
    gl.ylines = True
    gl.ylabels_left = False
    gl.ylabels_right = True
    gl.yformatter = LATITUDE_FORMATTER
    gl.ylabel_style = {'size': 8, 'color': 'black'}

    return


def plotInterestPoint(ax):
    """
    
    
    """
    from pandas import read_excel

    filepath="../data/points.xls"
    points=read_excel(filepath, sheet_name="Map3" )    
    
    for lon, lat, cname, h_alig  in zip(points.lon, points.lat, points.name, points.h_alig):   #range(len(cities_name)):
        ax.plot(lon, lat, label=cname, marker='o', transform=ccrs.Geodetic())                     #, c='b'
        ax.text(lon, lat, cname, fontsize=8, horizontalalignment=h_alig, transform=ccrs.Geodetic())

    return

def saveFig(fig, file=""):
    """ Save the figure
    
    INPUT:
        filename : the complete filename (path + filename + extension)
    
    """


    if file != "":
        plt.savefig('./sample/'+file+'.png', format='png', dpi=300)
        plt.savefig('./sample/'+file+'.pdf', format='pdf', dpi=150, transparent=True)


def main():
    """
    
    lon0 = 35.25; lat0 = -23.60
    lon1 = 35.25; lat1 = -24.0
    lon2 = 35.65; lat2 = -24.0
    lon3 = 35.65; lat3 = -23.60
   
    
    https://stackoverflow.com/questions/52356926/how-to-set-offset-for-python-cartopy-geometry
    """


    # Create the figure
    fig = plt.figure(figsize=(5,6))
 
    from cartopy.io.img_tiles import OSM 

           
    # Add OSM image as background for the selected extension
    tiler = OSM()
    ax = plt.axes(projection=tiler.crs)

    # Openstreet layer zoom detail
    zoom=12
    
    ax.add_image(tiler, zoom, alpha=0.75)

    extent = [35.25, 35.65, -24.05, -23.60]

    ax.set_extent(extent)

    # Set figure title
    ax.set_title('Study area',fontsize=10)


    # Plot coastline from GSHHSF
    coast_line=cfeature.GSHHSFeature(scale='full')
    
    ax.add_feature(coast_line,  alpha=1.0,  linewidths=0.5, edgecolor='black' )

        
    plotWetlands(ax)
    plotRivers(ax)
    

    plotInterestPoint(ax)
 
    # plot difters track
    plotTrack(ax) 


    # Plot escale bar
    scaleBar(ax, length=10, location=(0.8, 0.80), linewidth=1.5)
    
    plotGridLines(ax)
    
    # Criate a subfigure 
    #subfigure = [.58, .09, .30, .20]
    ax2 = fig.add_axes([.58, .09, .30, .20]) 
    plotMozambique(ax2)

    # Adjust plot the the figure
    plt.tight_layout()

    plt.show()

    #saveFig(fig, file='estudyArea3')
  
    
if __name__ == '__main__':
    main()
