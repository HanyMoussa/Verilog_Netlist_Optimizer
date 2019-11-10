# Extract Capacitance


import scipy.interpolate
from scipy.interpolate import UnivariateSpline

#a function that takes the capacitance array and the delays array
#it interpolates/extrapolates to obtain the delay corresponding to a target capacitance
def getDelay(capacitances, delays, target, cload):
    # For an output pin, the target capacitance would be 0 so return the 3rd value
    if(target == 0):
        target = (cload/1000)  #use cload in pf not fF
    
    if((target > capacitances[-1])): #extrapolation needed
        slope = (delays[-1] - delays[-2])/(capacitances[-1] - capacitances[-2])
        c = delays[-1] - slope * capacitances[-1]
        return slope*target + c
    elif (target < capacitances[0]):  #extrapolation needed
        slope = (delays[1] - delays[0])/(capacitances[1] - capacitances[0])
        c = delays[0] - slope * capacitances[0]
        return slope*target + c
    else: #interpolation needed
        interpolateDelay = scipy.interpolate.interp1d(capacitances, delays)
        return max(interpolateDelay(target), 0)
    