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


def difDividida(lnodes):
    """ Calcula las diferencias divididas del Polinomio Interpolador de Hermite
    """
    xi = lnodes[0]
    xk = lnodes[-1]
    if len(lnodes) > 2:
        if xi.getX() == xk.getX():
            return xi.getDer()
        else:
            tmp1 = difDividida(lnodes[1:])
            tmp2 = difDividida(lnodes[:-1])
            tmp = tmp1 - tmp2
            tmp = tmp / (xk.getX() - xi.getX())
            #Almaceno el resultado parcial necesario
            dd[len(lnodes) - 3] = tmp2
            return tmp
    else:
        if xi.getX() == xk.getX():
            return xi.getDer()
        else:
            tmp = xk.getY() - xi.getY()
            tmp = tmp / (xk.getX() - xi.getX())
            return tmp

if __name__ == '__main__':


    nube = Nube()
    dd = None
    global dd
    op = '1'
    while op != '0':

        os.system('clear')
        print "1.- Introduccion de Nube de Puntos"
        print "2.- Nube de Puntos"
        print "3.- Evaluacion del Polinomio Interpolador"
        print "4.- En que tiempo se llega a los 280 km/h"
        print "0.- Salir"

        print "\n\t Opcion: ",
        op = raw_input()
        os.system('clear')

        if op == '1':
            print "Numero de Nodos: ",
            n = int(raw_input())
            nube.setNube()

        elif op == '2':
            nube.imprimeNube()

        elif op == '3':
            #Lista de nodos de tamaño m (siendo m el numero de condiciones)
            nl = nube.nodeList()
            #variable global para almacenar las diferencias divididas
            dd = [None] * (len(nl) - 1)

            print "Calculando diferencias divididas ..."
            dd[-1] = difDividida(nl)
            print "Expresion del Polinomio Interporlador:"

            print "f(x) = ", nl[0].getY(),
            for i in range(0, len(nl) - 1):
                print "+", dd[i],
                for j in range(0, i+1):
                    print "(X-" + str(nl[j].getX()) + ")",
            print ""

            print "Valor de X = ",
            x = float(raw_input())
            resultado = nl[0].getY()
            for i in range(0, len(nl) - 1):
                tmp = dd[i]
                for j in range(0, i+1):
                    tmp *= (x - nl[j].getX())
                resultado += tmp
            print "f(x) = ", resultado

        elif op == '4':
            #obtenemos las diferencias divididas del el polinomio interpolador
            dd = [None] * (len(nube.nodeList()) - 1)
            dd[-1] = difDividida(nube.nodeList())
            #velocidad a comprobar
            v = (280 * 1000) / 3600
            #Result es la derivada del Polinomio Interpolador de la Practica
            x = 0.0
            while x <= 13:
                result = dd[0]
                result += dd[1] * 2 * x
                result += dd[2] * ((3 * pow(x, 2)) - (6 *x))
                result += dd[3] * ((4 * pow(x, 3)) - (24 * pow(x, 2)) + (30 * x))
                result += dd[4] * ((5 * pow(x, 4)) - (64 * pow(x, 3)) + (237 * pow(x, 2)) - (240 * x))
                result += dd[5] * ((6 * pow(x, 5)) - (145 * pow(x, 4)) + (1148 * pow(x, 3)) - (3441 * pow(x, 2)) + (3120 * x))
                if result >= v:
                    print "La velocidad de 280 km/h se alcanza a los: ", x, "segundos"
                    break
                x += 0.001

        elif op != '0':
            print "[ERROR] Opcion invalida"

        if op != '0':
            print "\nPresione tecla para continuar ..."
            raw_input()



