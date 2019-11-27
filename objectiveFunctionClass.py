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




class evaluateFuturesParams:
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
    overwrite = True
    def __init__(self):  
        self.calibration_results = "calib_python_script.csv"
#        os.remove(self.calibration_results)
        print("File ",self.calibration_results," Removed!")
	
    def f(self,X):
        try:
            filePath = self.calibration_results
            os.remove(filePath)
        except:
            print("Error while deleting file ", filePath)
        print("Evaluating s", X)
        self.compactness_mean = str(X[0])
        self.compactness_range = str(X[1])
        self.discount_factor = str(X[2])
        r.calib = Module('r.futures.calib')
        r.calib(development_start = self.development_start,
        development_end = self.development_end, 
        subregions = self.subregions,
        patch_sizes = self.patch_sizes,
        calibration_results = self.calibration_results,
        patch_threshold = self.patch_threshold,
        repeat = self.repeat,
        compactness_mean = self.compactness_mean,
        compactness_range = self.compactness_range,
        discount_factor= self.discount_factor,
        predictors = self.predictors,
        demand = self.demand,
        devpot_params = self.devpot_params,
        num_neighbors = self.num_neighbors,
        seed_search = self.seed_search,
        development_pressure= self.development_pressure,
        development_pressure_approach = self.development_pressure_approach, 
        n_dev_neighbourhood = self.n_dev_neighbourhood, 
        gamma= self.gamma, 
        scaling_factor= self.scaling_factor ,
        overwrite=self.overwrite
        )
        self.results = pd.read_csv(self.calibration_results)
        os.remove(self.calibration_results)
        return self.results
        

        

#Usage
#/home/rodrigo/grassData2/FUTURES_triangle
#grass location: future_ncspm
#grass mapset: practice1


#execfile("objectiveFunctionClass.py")
#X = [0.1,0.05,0.1]
#c = evaluateFuturesParams()
#r = c.f(X)

        
        
		
		
		
		
	 	



