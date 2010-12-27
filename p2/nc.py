#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
        $Id$
Description: Interfaz de usuario del programa que permite estimar integrales definidas mediantes las
             formulas de cuadratura compuestas de Newton-Cotes.
    $Author$ Lionel Aster Mena Garcia (alu3409) 78853601-X
      $Date$
  $Revision$
"""

import os
import math
from quadrature import *

def practFunction(x):
    return math.log(2 * x + 3)


if __name__ == '__main__':
    nc = None
    op = '1'
    while op != '0':
        os.system('clear')
        print "1.- Introduccion de Datos"
        print "2.- Determinar las formulas a usar"
        print "3.- Calculo de las estimaciones"
        print "4.- Mostrar estimaciones del error"
        print "0.- Salir"

        print "\n\t Opcion: ",
        op = raw_input()
        os.system('clear')

        if op == '1':
            print "Numero de nodos: ",
            nodes = int(raw_input())
            print "Extremos del intervalo [a,b]: "
            print "a: ",
            a = int(raw_input())
            print "b: ",
            b = int(raw_input())
            values = []
            print "Valores del integrando en los nodos: "
            for i in range(0, nodes):
                #print "X" + str(i) + " = ",
                #values.append(float(raw_input()))
                x = a + ((i * (float(b-a)/float(nodes - 1))))
                print "X" + str(i) + " =", practFunction(x)
                values.append(practFunction(x))
            # Construimos , con estos datos, el objeto que manipula las formulas de cuadratura de Newton-Cotes
            nc = NewtonCotes(a, b, nodes, values)
        elif op == '2':
            nc.whatForm()
        elif op == '3':
            nc.integralEstimate()
        elif op == '4':
            #print "Valor Real de la Integral:",
            #rvalue = float(raw_input())
            nc.errorEstimate(1.3756763480830)
        elif op != '0':
            print "[ERROR] Opcion invalida"

        if op != '0':
            print "\nPresione tecla para continuar ..."
            raw_input()