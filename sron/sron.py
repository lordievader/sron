#!/usr/bin/env python3
"""Colormaps based on https://personal.sron.nl/~pault/
"""
from matplotlib.colors import LinearSegmentedColormap


class Colormap():
    """Base colormap.
    """
    name = 'SRON'
    colorscheme = [
        '#FFFFFF',  # white
        '#DDAA33',  # yellow
        '#BB5566',  # red
        '#004488',  # blue
        '#000000'   # black
    ]
    colormap = None

    def __init__(self, number_of_patches=4):
        """Creates a color map.
        """
        self.number_of_patches = number_of_patches
        self.generate()

    def __call__(self, value):
        if self.colormap is None:
            self.generate()

        return self.colormap(value)

    def generate(self):
        self.colormap = LinearSegmentedColormap.from_list(
            self.name,
            self.colorscheme,
            N=self.number_of_patches)


class BrightColormap(Colormap):
    def __init__(self, number_of_patches):
        self.number_of_patches = number_of_patches
        self.colorscheme = [
            '#4477AA',  # blue
            '#66CCEE',  # cyan
            '#228833',  # green
            '#CCBB44',  # yellow
            '#EE6677',  # red
            '#AA3377',  # purple
            '#BBBBBB',  # grey
        ]
        self.generate()


class VibrantColormap(Colormap):
    def __init__(self, number_of_patches):
        self.number_of_patches = number_of_patches
        self.colorscheme = [
            '#0077BB',  # blue
            '#33BBEE',  # cyan
            '#009988',  # teal
            '#EE7733',  # orange
            '#CC3311',  # red
            '#EE3377',  # magenta
            '#BBBBBB',  # grey
        ]
        self.generate()


class MutedColormap(Colormap):
    def __init__(self, number_of_patches):
        self.number_of_patches = number_of_patches
        self.colorscheme = [
            '#332288',  # indigo
            '#88CCEE',  # cyan
            '#44AA99',  # teal
            '#117733',  # green
            '#999933',  # olive
            '#DDCC77',  # sand
            '#CC6677',  # rose
            '#882255',  # wine
            '#AA4499',  # purple
            '#DDDDDD',  # pale grey
        ]
        self.generate()
