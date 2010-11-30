#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
        $Id$
Description: Representacion de un Nodo de con su derivada
    $Author$ Lionel Aster Mena Garcia (alu3409) 78853601-X
      $Date$
  $Revision$
"""

class Nodo:

    def __init__(self, x, y, der = None):
        """ Constructor que recibe las coordenadas del nodo (punto) y opcionalmente su derivada primera
        """
        self._x = x
        self._y = y
        self._derivada = der

    def getX(self):
        """ Obtiene la abcisa del nodo (punto)
        """
        return self._x

    def getY(self):
        """ Obtiene la ordenada del nodo (punto)
        """
        return self._y

    def getDer(self):
        """ Obtiene la derivada primera del nodo (punto)
        """
        return self._derivada

    def __str__(self):
        """ Representacion informal en string del nodo
        """
        return str(self._x)
