# -*- coding: utf-8 -*-

class Shirt(object):

    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size

    def getJson(self):
        return vars(self)

        