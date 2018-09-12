name = 'inkrement'

def plot_lag(x, y, n, group = 0, lag = 0):
    """Scatter plot of group-th n elements of data and lag * n elements previous"""
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
    
    l = lag
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
        axs.scatter(data_x, data_y, color=blues[-1-i])
        
    patches = []
    for i in range(l + 1): #Create legend patches
        patches.append(matplotlib.patches.Patch(color=blues[-1-i], label='{0} [{1}:{2}], {3} [{1}:{2}]'.format('x', (group - i) * n, (group - i + 1) * n, 'y')))
    matplotlib.pyplot.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)

