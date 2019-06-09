# -*- coding: utf-8 -*-

from flask import jsonify

class Dress: 

    def __init__(self, size, style, color, brand, material, long):
        self.size = size
        self.style = style
        self.color = color
        self.brand = brand
        self.material = material
        self.long = long

    def getJson(self):
        return jsonify( vars(self) )

