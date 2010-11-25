#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
        $Id$
Description: Implementacion del metodo de Hermite para interpolacion polinomica
    $Author$ Lionel Aster Mena Garcia (alu3409) 78853601-X
      $Date$
  $Revision$
"""

import os

if __name__ == '__main__':

    op = '1'
    while op != '0':

        os.system('clear')
        print "1.- Introduccion de datos"
        print "2.- Evaluacion del polinomio interpolador"
        print "3.- Expresion del Polinomio Interpolador"
        print "0.- Salir"

        print "\n\t Opcion: ",
        op = raw_input()
        os.system('clear')

        if op == '1':
            print "opcion ", op
            raw_input()
        elif op == '2':
            print "opcion ", op
            raw_input()
        elif op == '3':
            print "opcion ", op
            raw_input()
        elif op != '0':
            print "[ERROR] Opcion invalida"
            raw_input()



