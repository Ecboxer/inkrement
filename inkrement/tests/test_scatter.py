import inkrement
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import cleanup

@cleanup
def test_create_figure():
    """
    Simple test that creates a figure using pyplot.
    """
    fig = plt.figure()
