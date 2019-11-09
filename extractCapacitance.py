# Extract Capacitance


import scipy.interpolate
from scipy.interpolate import UnivariateSpline

def getDelay(capacitances, delays, target):
    # For an output pin, the target capacitance would be 0 so return the 3rd value
    if(target == 0):
        return delays[2]
    else:
        if((target > capacitances[-1])):
            slope = (delays[-1] - delays[-2])/(capacitances[-1] - capacitances[-2])
            c = delays[-1] - slope * capacitances[-1]
            return slope*target + c
        elif (target < capacitances[0]):
            slope = (delays[1] - delays[0])/(capacitances[1] - capacitances[0])
            c = delays[0] - slope * capacitances[0]
            return slope*target + c
        else:
            interpolateDelay = scipy.interpolate.interp1d(capacitances, delays)
            return max(interpolateDelay(target), 0)
    