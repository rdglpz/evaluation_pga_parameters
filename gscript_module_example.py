# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import sys
import subprocess

# define GRASS Database
# add your path to grassdata (GRASS GIS database) directory
# specify (existing) Directory, Location and Mapset

'''
Example locating GrassGisDatabase directory, Grass Location and grass mapset:
-------

*this is the database grass gis directory where inside is the grass location futures_triange***

(base) rodrigo@rodrigo-centromet:~/grassData2/FUTURES_triangle$ ls
futures_ncspm  futures_triangle_files

The mapsets are found in Futures
(base) rodrigo@rodrigo-centromet:~/grassData2/FUTURES_triangle$ ls futures_ncspm/
CREDITS.txt  FUTURES_triangle  PERMANENT                  population_trend.csv  VERSION.txt
demand.csv   HISTORY.txt       population_projection.csv  practice1

'''
gisdb = os.path.join(os.path.expanduser("~"), "grassData2/FUTURES_triangle")

location = "futures_ncspm"

mapset = "practice1"

# path to the GRASS GIS launch script
# we assume that the GRASS GIS start script is available and on PATH
# query GRASS itself for its GISBASE
# (with fixes for specific platforms)
# needs to be edited by the user

'''
Example: finding grass executable file 

$ locate -b -r ^grass76$
/usr/bin/grass76 <--
/usr/lib/grass76
/usr/share/grass76

it can be set using the absolute path if it is not in the path
grass7bin = '/usr/bin/grass76'
or 
grass7bin = 'grass76'

'''

grass7bin = 'grass76'

startcmd = [grass7bin, '--config', 'path']

try:
    p = subprocess.Popen(startcmd, shell=False,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
except OSError as error:
    sys.exit("ERROR: Cannot find GRASS GIS start script"
             " {cmd}: {error}".format(cmd=startcmd[0], error=error))
if p.returncode != 0:
    sys.exit("ERROR: Issues running GRASS GIS start script"
             " {cmd}: {error}"
             .format(cmd=' '.join(startcmd), error=err))
    
gisbase = out.strip(os.linesep)

# set GISBASE environment variable
os.environ['GISBASE'] = gisbase
    
# define GRASS-Python environment
grass_pydir = os.path.join(gisbase, "etc", "python")
sys.path.append(grass_pydir)

# import (some) GRASS Python bindings
import grass.script as gscript
import grass.script.setup as gsetup

# launch session
rcfile = gsetup.init(gisbase, gisdb, location, mapset)

print("Example Calls")
gscript.message('Current GRASS GIS 7 environment:')
print gscript.gisenv()

gscript.message('Available raster maps:')
for rast in gscript.list_strings(type='raster'):
    print rast

gscript.message('Available vector maps:')
for vect in gscript.list_strings(type='vector'):
    print vect
    
    
'''
Reference:
----------

https://grass.osgeo.org/grass76/manuals/libpython/script.html#module-script.setup

'''