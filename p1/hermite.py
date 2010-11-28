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
    op = '1'
    while op != '0':

        os.system('clear')
        print "1.- Introduccion de Nube de Puntos"
        print "2.- Nube de Puntos"
        print "3.- Evaluacion del Polinomio Interpolador"
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
            global dd

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


        elif op != '0':
            print "[ERROR] Opcion invalida"

        if op != '0':
            print "\nPresione tecla para continuar ..."
            raw_input()



