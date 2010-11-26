#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
        $Id$
Description: Implementacion del metodo de Hermite para interpolacion polinomica
    $Author$ Lionel Aster Mena Garcia (alu3409) 78853601-X
      $Date$
  $Revision$
"""

from nube import *
import os

if __name__ == '__main__':

    nube = None
    op = '1'
    while op != '0':

        os.system('clear')
        print "1.- Introduccion de Nube de Puntos"
        print "2.- Nube de Puntos"
        print "3.- Evaluacion del Polinomio Interpolador"
        print "4.- Expresion del Polinomio Interpolador"
        print "0.- Salir"

        print "\n\t Opcion: ",
        op = raw_input()
        os.system('clear')

        if op == '1':
            print "Numero de Nodos: ",
            n = int(raw_input())
            nube = Nube(n)
            nube.setNube()
            raw_input()
        elif op == '2':
            nube.imprimeNube()
            raw_input()
        elif op == '3':
            print "opcion ", op
            raw_input()
        elif op == '4':
            print "opcion ", op
            raw_input()
        elif op != '0':
            print "[ERROR] Opcion invalida"
            raw_input()



