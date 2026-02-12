""" 
Write a program that reports descriptive statistics for numbers on the 
command line. Your program should report the following values: 

The number of values, the min and max values, mean and standard deviation, 
and the median value. 
"""

import math
import sys

def stats(): 
	nums = [float(x) for x in sys.argv[1:]]

	count = len(nums)

	maximum = max(nums)
	minimum = min(nums)

	mean = sum(nums) / count
	
	variance = sum((x-mean) ** 2 for x in nums) / count
	stdev = math.sqrt(variance)

	nums_sorted = sorted(nums)
	
	mid = count // 2
	
	if count % 2 == 1: 
		median = nums_sorted[mid]
	else: 
		median = (nums_sorted[mid - 1] + nums_sorted[mid]) / 2
 
	print('Count:', count)
	print('Min:', minimum)
	print('Max:', maximum)
	print('Mean:', mean)
	print('Standard Deviation:', stdev)
	print('Median:', median)

stats()