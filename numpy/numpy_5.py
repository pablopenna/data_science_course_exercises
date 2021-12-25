import numpy as np

arr_hol_temps = np.array([3.1, 3.3, 6.2, 9.2, 13.1, 15.6, 17.9, 17.5, 14.5, 10.7, 6.7, 3.7])

# Mean
myMean = np.mean(arr_hol_temps)
print(f"Mean. {myMean}")

# Months which temperature has been higher than the mean
overAvgMonths = arr_hol_temps > myMean
print(f"blah blah months blah blah average blah blah: {overAvgMonths}")

# Get closer to average value
overAvgValues = arr_hol_temps[arr_hol_temps>myMean]
closerToMeanFromAbove = overAvgValues.min()
underAvgValues = arr_hol_temps[arr_hol_temps<myMean]
closerToMeanFromBelow = overAvgValues.max()
###blah blah you know the drill, get the diff to the average and get closer
monthCloser = np.where(arr_hol_temps==closerToMeanFromAbove)[0]

print(f"Closer to mean value:{closerToMeanFromAbove}")
print(f"Closer to mean month:{monthCloser}")

# the good way
arr_diff= np.abs(myMean - arr_hol_temps)
monthCloser = np.argmin(arr_diff)
closerValue = arr_diff[monthCloser]
