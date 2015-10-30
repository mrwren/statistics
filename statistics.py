# Module statistics.py

__all__ = ['mean', 'median', 'median_low', 'median_high', 'mode', 'variance', 
		   'pvariance', 'stdev', 'pstdev']

# Function		Description
# ------------	-----------------------------------
# mean 			Arithmetic mean(average) of data.
# median 		Median(middle value) of data.
# median_low 	Low median of data.
# median_high 	High median of data.
# mode 			Mode(most common value) of data.
# variance		Variance of data.
# pvariance		Population variance of data.
# stdev			Standard deviation of data.
# pstdev		Population standard deviation of data.

def mean(data):
	# Return the arithmetic mean of numeric data

	# >>> statistics.mean([1, 2, 2, 3, 4])
	# 2.4

	return sum(data) * 1.0 / len(data)

def median(data):
	# Return the median(middle value) of numeric data

	# >>> statistics.median([1, 2, 4])
	# 2
	# >> statistics.median([1, 2, 3, 4])
	# 2.5

	sort = sorted(data)
	i = (len(data) - 1) // 2
	if (len(data) % 2): return sort[i]
	else: return(sort[i] + sort[i + 1]) / 2.0

def median_low(data):
	# Return the low median of numeric data

	# >>> statistics.median_low([1, 2, 4])
	# 2
	# >>> statistics.median_low([1, 2, 3, 4])
	# 2

	sort = sorted(data)
	i = len(data)
	if i % 2 == 1: return sort[i // 2]
	else: return sort[i // 2 - 1]

def median_high(data):
	# Return the high median of numeric data

	# >>> statistics.median_high([1, 2, 4])
	# 2
	# >>> statistics.median_high([1, 2, 3, 4])
	# 3

	sort = sorted(data)
	i = len(data)
	return sort[i // 2]

def mode(data):
	# Return the most common data point from numeric or nominal(non-numeric) data.

	# statistics.mode([1, 2, 2, 2, 3, 3, 4])
	# [2]
	# statistics.mode(["int", "string", "float", "float"])
	# ['float']

	most = max([data.count(d) for d in data])
	return list({d for d in data if data.count(d) == most})

def variance(data):
	# Return the variance of data.

	# >>> statistics.variance([1, 2, 3, 4])
	# 1,66666666666667

	 m = mean(data)
	 var = 0
	 for i in data:
	 	var += (i - m) ** 2
	 var /= len (data) -1
	 return var

def pvariance(data):
	# Return the population variance of data.

	# >>> statistics.variance([1, 2, 3, 4])
	# 1.25

	var = 0
	m = mean(data)
	for i in data:
		var += (i - m) ** 2
	return var / len(data)

def stdev(data):
	# Return the square root of the variance.

	# >>> statistics.stdev([1, 2, 3, 4])
	# 1,2909944487358056

	return variance(data) ** 0.5

def pstdev(data):
	# Return the square root of the population variance.

	# >>> statistics.pstdev([1, 2, 3, 4])
	# 1,118033988749895

	var = 0
	m = mean(data)
	for i in data:
		var += (i - m) ** 2
	var /= len(data)
	return var ** 0.5
