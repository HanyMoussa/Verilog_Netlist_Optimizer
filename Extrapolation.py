# A module that extrapolates the delay if it is out of the range in the table

from scipy.interpolate import UnivariateSpline

capacitances = [20, 30, 40, 50]
delays = [10, 20, 30, 35]

extrapolator = UnivariateSpline(capacitances, delays)
targetCapacitance = 16
extrapolatedDelay = extrapolator([targetCapacitance]);
print(extrapolatedDelay)
