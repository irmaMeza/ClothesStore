# -*- coding: utf-8 -*-

class Dress:

    def __init__(self, sizes, styles, colors, brands, materials, longs):
        self.sizes = sizes
        self.styles = styles
        self.colors = colors
        self.brands= brands
        self.materials= materials
        self.longs = longs

    def getJson(self):
        return vars(self)

        