#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
        $Id$
Description: representacion de la nube de puntos (encapsula el conjunto de nodos)
    $Author$ Lionel Aster Mena Garcia (alu3409) 78853601-X
      $Date$
  $Revision$
"""
from nodo import *

class Nube:

    def __init__(self, numn):
        self._numn = numn
        self._ncond = 0
        self._nube = []

    def setNube(self):
        for i in range(0, self._numn):
            print "Xi = ",
            x = float(raw_input())
            print "Yi = ",
            y = float(raw_input())
            print "¿Derivada Primera? [s/n]: ",
            op = raw_input()
            if op == 's':
                print "Y'= ",
                der = float(raw_input())
            else:
                der = None

            self._nube.append(Nodo(x, y, der))

    def imprimeNube(self):
        print str("Xi").center(4),
        for i in range(0, self._numn):
            print str(self._nube[i].getX()).center(6),
        print ""

        print str("Yi").center(4),
        for i in range(0, self._numn):
            print str(self._nube[i].getY()).center(6),
        print ""

        print str("Y'i").center(4),
        for i in range(0, self._numn):
            if self._nube[i].getDer() != None:
                print str(self._nube[i].getDer()).center(6),
            else:
                print str(" ").center(6),

        print ""


