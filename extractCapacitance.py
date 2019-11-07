# Extract Capacitance


import scipy.interpolate
from scipy.interpolate import UnivariateSpline

def getDelay(capacitances, delays, target):
    # For an output pin, the target capacitance would be 0 so return the 3rd value
    if(target == 0):
        return delays[2]
    else:
        if((target > capacitances[-1]) | (target < capacitances[0])):
            extrapolator = UnivariateSpline(capacitances, delays)
            return max(extrapolator([target]), 0)
        else:
            interpolateDelay = scipy.interpolate.interp1d(capacitances, delays)
            return max(interpolateDelay(target), 0)
    
"""    
def main():
    capacitances = [0.04,0.08,0.16,0.4]
    delays = [0.187081,0.195719,0.216861,0.348891]
    targetCapacitance = 0.0101035
    
    print(getCapacitance(capacitances,delays, targetCapacitance))
    
main()
"""