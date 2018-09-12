Inkrement
=========

Inkrement provides tools for incremental data analysis. You might find it most useful when the questions you have can be answered from a subset of your data. The tools may also be useful in determining if a partial view of your data can be used to draw conclusions, ie are differences in your data by orders of magnitude or is your data fairly homogeneous.  

Typical usage often looks like this:

    #!usr/bin/env python
	
	import inkrement
	
	import numpy as np
	
	x = np.random.normal(0, 1, 1000)
	y = np.random.normal(0, 1, 1000)
	
	inkrement.plot_lag(x, y, 10, 53, 8)
	
Output looks like this:  
![](https://github.com/Ecboxer/inkrement/docs/testplot.png)
	
Summary
=======

Matplotlib wrapper for incremental data analysis

Requirements
============

Matplotlib
