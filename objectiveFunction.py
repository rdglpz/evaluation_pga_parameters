import sys
import os
import atexit
import numpy as np
import tempfile
from multiprocessing import Process, Queue

import grass.script.core as gcore
import grass.script.raster as grast
import grass.script.utils as gutils
from grass.exceptions import CalledModuleError

from grass.pygrass.modules.shortcuts import raster as r
from grass.pygrass.modules import Module

import pandas as pd

print(sys.version)




r.calib = Module('r.futures.calib')

development_start = "urban_1992"
development_end = "urban_2011"
subregions="calib_county"
patch_sizes = "patches_a.txt"
calibration_results = "calib_python_script.csv"
patch_threshold = "1800"
repeat = "1"
compactness_mean="0.1"
compactness_range="0.05"
discount_factor="0.1"
predictors = "road_dens_perc,forest_smooth_perc,dist_to_water_km,dist_to_protected_km"
demand = "demand.csv"
devpot_params = "potential.csv"
num_neighbors = "4"
seed_search = "2"
development_pressure= "devpressure_0_5" 
development_pressure_approach = "gravity" 
n_dev_neighbourhood="30" 
gamma="0.5" 
scaling_factor="0.1"

r.calib( development_start = development_start,
    development_end = development_end, 
    subregions = subregions,
    patch_sizes = patch_sizes,
    calibration_results = calibration_results,
    patch_threshold = "1800",
    repeat = "1",
    compactness_mean="0.1",
    compactness_range="0.05",
    discount_factor="0.1",
    predictors = "road_dens_perc,forest_smooth_perc,dist_to_water_km,dist_to_protected_km",
    demand = "demand.csv",
    devpot_params = "potential.csv",
    num_neighbors = "4",
    seed_search = "2",
    development_pressure= "devpressure_0_5",
    development_pressure_approach = "gravity", 
    n_dev_neighbourhood="30", 
    gamma="0.5", 
    scaling_factor="0.1",
    overwrite=True
        
        )


        
        
		
		
		
		
	 	
	
    
    
print("end")

#r.futures.calib development_start=urban_1992 development_end=urban_2011 subregions=calib_county patch_sizes=patches_a.txt calibration_results=calib.csv patch_threshold=1800 repeat=1 compactness_mean=0.1 compactness_range=0.05 discount_factor=0.1 predictors=road_dens_perc,forest_smooth_perc,dist_to_water_km,dist_to_protected_km demand=demand.csv devpot_params=potential.csv num_neighbors=4 seed_search=2 development_pressure=devpressure_0_5 development_pressure_approach=gravity n_dev_neighbourhood=30 gamma=0.5 scaling_factor=0.1 --o




print("running")

