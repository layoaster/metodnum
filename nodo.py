#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
        $Id$
Description: Representacion de un Nodo de con su derivada
    $Author$ Lionel Aster Mena Garcia (alu3409) 78853601-X
      $Date$
  $Revision$
"""

def Nodo:

    def __init__(self, x, y, der = None):
        self._x
        self._y
        self._derivada = der

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getDer(self):
        return self._derivada