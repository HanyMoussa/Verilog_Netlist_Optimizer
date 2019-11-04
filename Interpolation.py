"""
Created on Mon Nov  4 12:52:11 2019

@author: Ramez Moussa
"""
import scipy.interpolate

# Always consider the 3rd value for the input transition
capacitances = [20, 30, 40, 40]
delays = [10, 20, 30, 35]

targetCapacitance = 16

interpolateDelay = scipy.interpolate.interp1d(capacitances, delays)
print(interpolateDelay(targetCapacitance));