# Extract Capacitance


import scipy.interpolate
from scipy.interpolate import UnivariateSpline

def extractCapacitance(capacitances, delays, target):
    if((target > capacitances[-1]) | (target < capacitances[0])):
        extrapolator = UnivariateSpline(capacitances, delays)
        return extrapolator([target])
    else:
        interpolateDelay = scipy.interpolate.interp1d(capacitances, delays)
        return interpolateDelay(target)
    
    
def main():
    capacitances = [20, 30, 40, 50, 80]
    delays = [10, 20, 30, 35, 50]
    targetCapacitance = 95
    
    print(extractCapacitance(capacitances,delays, targetCapacitance))
    
main()