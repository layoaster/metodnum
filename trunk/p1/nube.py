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

    def __init__(self, numn = 5):
        """ Constructor de la clase que por defecto ingresa la nube de puntos del problema de la practica
        """
        self._numn = numn
        self._ncond = 0
        self._nube = []

        #Datos de el problema de la practica
        self._nube.append(Nodo(0, 0.0, 75.0))
        self._nube.append(Nodo(3, 225.0))
        self._nube.append(Nodo(5, 383.0))
        self._nube.append(Nodo(8, 623.0))
        self._nube.append(Nodo(13, 993.0, 72.0))

    def setNube(self):
        """ Se ingresan los puntos pidiendo por teclado las coordenadas y derivada primera de cada uno de los puntos de la nube
        """
        self._nube = []
        for i in range(0, self._numn):

            print "***********"
            print "X" + str(i) + " = ",
            x = int(raw_input())
            print "Y" + str(i) + " = ",
            y = float(raw_input())
            print "¿Derivada Primera? [s/n]: ",
            op = raw_input()
            if op == 's':
                print "Y'" + str(i) + " = ",
                der = float(raw_input())
            else:
                der = None

            self._nube.append(Nodo(x, y, der))

    def imprimeNube(self):
        """ Imprime en forma de vectores los datos de cada punto en la nube
        """
        print str("Xi").center(4),
        for i in range(0, self._numn):
            print str(self._nube[i].getX()).ljust(6),
        print ""

        print str("Yi").center(4),
        for i in range(0, self._numn):
            print str(self._nube[i].getY()).ljust(6),
        print ""

        print str("Y'i").center(4),
        for i in range(0, self._numn):
            if self._nube[i].getDer() != None:
                print str(self._nube[i].getDer()).ljust(6),
            else:
                print str(" ").ljust(6),

        print ""

    def nodeList(self):
        """ Construye la lista de nodos necesaria para calcular las diferencias divididas
        """
        lnodes = []

        for n in self._nube:
            lnodes.append(n)
            if n.getDer():
                lnodes.append(n)

        return lnodes

    def getNumNodes(self):
        """ Devuelve el numero de puntos (nodos) que conforman la nube
        """
        return self._numn



