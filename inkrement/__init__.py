name = 'inkrement'

def plot_lag(x, y, n, group = 0, lag = 0):
    """Scatter plot of group-th n elements of data and lag * n elements previous
    
    Parameters
    ----------
    x : independent variable
    
    y : dependent variable
    
    n : number of elements to plot in each batch
    
    group : index of final batch of data
    
    lag : number of batches before group-th to be plotted
    
    Output
    ------
    Scatterplot with labelled legend
    """
    import matplotlib.pyplot
    import matplotlib.patches

    blues = ['#f7fbff',
             '#deebf7',
             '#c6dbef',
             '#9ecae1',
             '#6baed6',
             '#4292c6',
             '#2171b5',
             '#08519c',
             '#08306b']
    
    l = int(lag)
    if l < 0:
        print('lag **kwarg should be an int between 0 and 8')
        raise
    if l > 8:
        print('max recommended lag **kwarg is 8')
        l = 8
    fig, axs = matplotlib.pyplot.subplots()
    data_x = x[group * n:(group+1) * n]
    data_y = y[group * n:(group+1) * n]
    axs.scatter(data_x, data_y, color=blues[-1])
    axs.set_xlabel('x')
    axs.set_ylabel('y')
    for i in range(l): #Plot lagged groups in lighter color
        data_x = x[(group - i - 1) * n:(group - i) * n]
        data_y = y[(group - i - 1) * n:(group - i) * n]
        axs.scatter(data_x, data_y, color=blues[-2-i])
        
    patches = []
    for i in range(l + 1): #Create legend patches
        patches.append(matplotlib.patches.Patch(color=blues[-1-i], label='{0} [{1}:{2}], {3} [{1}:{2}]'.format('x', (group - i) * n, (group - i + 1) * n, 'y')))
    matplotlib.pyplot.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)

def inc_hist_cdf(x, n, start = 0, inc = 0, bins = 20):
    """
    Plots cumulative histograms of the group-th n * (i + 1) elements of x for 0 <= i <= lag
    
    Parameters
    ----------
    x : data
    
    n : number of observations to include in the first batch and to increase by in each subsequent batch
    
    start : start index of first batch of data
    
    inc : number of batches to be plotted
    
    bins : number of bins for each cumulative histogram
    
    Output
    ------
    Overayed histograms for (inc + 1) * n observations beginning at start
    """
    import matplotlib.pyplot
    import matplotlib.patches

    blues = ['#f7fbff',
             '#deebf7',
             '#c6dbef',
             '#9ecae1',
             '#6baed6',
             '#4292c6',
             '#2171b5',
             '#08519c',
             '#08306b']
    
    inc = int(inc)
    if inc < 0:
        print('inc **kwarg should be an int between 0 and 8')
        raise
    if inc > 8:
        print('max recommended lag **kwarg is 8')
        inc = 8
    
    fig, axs = matplotlib.pyplot.subplots()
    axs.hist(x[start:(start + n)], bins, histtype = 'step', cumulative = True, density = True, color = blues[-(inc + 1)])
    axs.set_xlabel('x')
    axs.set_ylabel('density')
    for i in range(inc):
        data_x = x[start:(start + n * (i + 2))]
        axs.hist(data_x, bins, histtype = 'step', cumulative = True, density = True, color = blues[-inc + i])
        
    patches = []
    for i in range(inc + 1): #Create legend patches
        patches.append(matplotlib.patches.Patch(color=blues[-(inc + 1) + i], label='{0} [{1}:{2}]'.format('x', start, start + n * (i + 1))))
    matplotlib.pyplot.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)