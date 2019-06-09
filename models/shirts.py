# -*- coding: utf-8 -*-

from flask import jsonify

class Shirt(object):

    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size

    def getJson(self):
        return jsonify( vars(self) )

