Inkrement
=========

Inkrement provides tools for incremental data analysis. You might find it most useful when the questions you have can be answered from a subset of your data. The tools may also be useful in determining if a partial view of your data can be used to draw conclusions, ie are differences in your data by orders of magnitude or is your data fairly homogeneous.  

Typical scatterplot usage looks like this:

    #!usr/bin/env python
	
	import inkrement
	
	import numpy as np
	
	x = np.random.normal(0, 1, 1000)
	y = np.random.normal(0, 1, 1000)
	
	inkrement.plot_lag(x, y, n=10, group=53, lag=8)
	
Output looks like this:  

![Example Plot](https://github.com/Ecboxer/inkrement/blob/master/docs/testplot.png)

Cumulative Histogram usage looks like:

	#!usr/bin/env python
	
	import inkrement
	
	import numpy as np
	
	x = np.random.normal(0, 1, 1000)
	
	inkrement.inc_hist_cdf(x, n=25, start=167, inc=8, bins=15)
	
Output looks like this:  

![Example Plot](https://github.com/Ecboxer/inkrement/blob/master/docs/histcdf.png)

Summary
=======

Matplotlib wrapper for incremental data visualization in python

Requirements
============

Matplotlib
