#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
        $Id$
Description: Implementacion de las formulas de cuadratura de Newton-Cotes (simples y compuestas):
             Trapecios, Simpson, Simpson 3/8 y Boole, y sus correspondientes estimaciones del error.
    $Author$ Lionel Aster Mena Garcia (alu3409) 78853601-X
      $Date$
  $Revision$
"""

from math import *

class NewtonCotes:
    TRAPEZOIDAL = 0
    SIMPSON     = 1
    SIMPSON3_8  = 2
    BOOLE       = 3

    def __init__(self, a, b, nodes, values):
        """ Constructor de la clase que implementa las formulas de cuadratura de Newton-Cotes
            Atributos:
                - _a = inicio del intervalo
                - _b = fin del intervalo
                - _nodes = numero de nodos
                - _values =  valores del integrando en los respetivos nodos (vector de valores)
                - _usedform = informa que formulas de cuadratura que se pueden usar con el numero nodos elegido
                - _estvalues = almacena el valor de los resultados obtenidos por cada formula de cuadratura
        """
        self._a = float(a)
        self._b = float(b)
        self._nodes = float(nodes)
        self._values = values
        self._usedform = [False, False, False, False]
        self._estvalues = [0, 0, 0, 0]

    def whatForm(self):
        """ Determina que formulas de cuadratura compuestas que se pueden usar.
            Modifica:
                - _usedform = Pone a Verdadero o Falso el vector para inidicar que formula se puede usar
        """
        #Determinamos el numero de intervalos
        interval = self._nodes - 1

        # Trapecios: siempre se puede emplear
        self._usedform[self.TRAPEZOIDAL] = True

        # Simpson: se puede usar cuando el numero de intervalos sea par
        if interval % 2 == 0:
            self._usedform[self.SIMPSON] = True
        else:
            self._usedform[self.SIMPSON] = False

        # Simpson 3/8: se puede usar cuando el numero de intervalos sea multiplo de 3
        if interval % 3 == 0:
            self._usedform[self.SIMPSON3_8] = True
        else:
            self._usedform[self.SIMPSON3_8] = False

        # Boole: se puede usar cuando el numero de intervalos sea multiplo de 4
        if interval % 3 == 0:
            self._usedform[self.BOOLE] = True
        else:
            self._usedform[self.BOOLE] = False

        print "Se pueden usar las siguientes formulas de cuadratura compuestas:"
        print "\t-Trapezoidal"
        for i in range(1, self.BOOLE + 1):
            if self._usedform[i]:
                if i == self.SIMPSON:
                    print "\t-Simpson"
                elif i == self.SIMPSON3_8:
                    print "\t-Simpson 3/8"
                else:
                    print "\t-Boole"

    def trapezoidal(self):
        """ Realiza el calculo de la regla de los Trapecios Compuesta
        """
        # calculamos el h = (b-a)/n
        h = (self._b - self._a) / (self._nodes - 1)
        # Calculamos f(a) + f(b) / 2
        temp = (self._values[0] + self._values[-1]) / 2.0
        # para luego sumarle el resto de los f(xi)
        for v in self._values[1:-1]:
            temp += v
        # almacenamos el valor para ser usado al mostrar estimaciones de error
        self._estvalues[self.TRAPEZOIDAL] = h * temp
        return self._estvalues[self.TRAPEZOIDAL]

    def simpson(self):
        """ Realiza el calculo de la regla de Simpson Compuesta
        """
        # calculamos el h = (b-a)/n
        h = (self._b - self._a) / (self._nodes - 1)
        # Sumamos nodos pares e impares por separado excepto los extremos
        pair = 0
        impair = 0
        for i in xrange(1,len(self._values) - 1,2):
            impair += self._values[i]
        for i in xrange(2,len(self._values) - 1,2):
            pair += self._values[i]

        #se multiplica los impares por 4 y los pares por 2 y se suman junto a los extremos
        temp =  self._values[0] + self._values[-1] + (2 * pair) + (4 * impair)
        # almacenamos el valor para ser usado al mostrar estimaciones de error
        self._estvalues[self.SIMPSON] = (h / 3.0) * temp
        return self._estvalues[self.SIMPSON]

    def simpson3_8(self):
        """ Realiza el calculo de la regla de Simpson 3/8 Compuesta
        """
        # calculamos el h = (b-a)/n
        h = (self._b - self._a) / (self._nodes - 1)
        # Sumamos nodos por separado excepto los extremos
        temp1 = 0
        temp2 = 0
        temp3 = 0
        for i in xrange(1,len(self._values) - 1,3):
            temp1 += self._values[i]
        for i in xrange(2,len(self._values) - 1,3):
            temp2 += self._values[i]
        for i in xrange(3,len(self._values) - 1,3):
            temp3 += self._values[i]

        #se multiplica por los correspondientes pesos
        temp =  self._values[0] + self._values[-1] + (3 * temp1) + (3 * temp2) + (2 * temp3)
        # almacenamos el valor para ser usado al mostrar estimaciones de error
        self._estvalues[self.SIMPSON3_8] = h * (3.0 / 8.0) * temp
        return self._estvalues[self.SIMPSON3_8]

    def boole(self):
        """ Realiza el calculo de la regla de Boole Compuesta
        """
        # calculamos el h = (b-a)/n
        h = (self._b - self._a) / (self._nodes - 1)
        # Sumamos nodos por separado excepto los extremos
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        for i in xrange(1,len(self._values) - 1,4):
            temp1 += self._values[i]
        for i in xrange(2,len(self._values) - 1,4):
            temp2 += self._values[i]
        for i in xrange(3,len(self._values) - 1,4):
            temp3 += self._values[i]
        for i in xrange(4,len(self._values) - 1,4):
            temp4 += self._values[i]

        #se multiplica por los correspondientes pesos
        temp =  (7 * self._values[0]) + (7 * self._values[-1]) + (32 * temp1) + (12 * temp2) + (32 * temp3) + (14 * temp4)
        # almacenamos el valor para ser usado al mostrar estimaciones de error
        self._estvalues[self.BOOLE] = h * (2.0 / 45.0) * temp
        return self._estvalues[self.BOOLE]

    def integralEstimate(self):
        """ Aplica las formulas de cuadratura indicadas para dar una estimacion del valor de la integral
        """
        print "Trapecios:", self.trapezoidal()

        # Solo se usaran las reglas previamente determinadas
        if self._usedform[self.SIMPSON]:
            print "Simpson:", self.simpson()

        if self._usedform[self.SIMPSON3_8]:
            print "Simpson 3/8:", self.simpson3_8()

        if self._usedform[self.BOOLE]:
            print "Boole:", self.boole()

    def errorEstimate(self, rvalue):
        """ En base a las estimaciones obtenidas muestra los errores reales y estimaciones del error para cada
            formula de cuadratura
        """
        # Pedimos las cotas superiores de las derivadas correspondientes a cada formula de cuadratura
        suplevels = [0, 0, 0, 0]
        for i in range(0, self.BOOLE + 1):
            if self._usedform[i]:
                if i == self.TRAPEZOIDAL:
                    print "Cota Superior para Trapecio: ",
                    suplevels[self.TRAPEZOIDAL] = float(raw_input()) #4.0/9.0
                elif i == self.SIMPSON:
                    print "Cota Superior para Simpson: ",
                    suplevels[self.SIMPSON] = float(raw_input()) #32.0/27.0
                elif i == self.SIMPSON3_8:
                    print "Cota Superior para Simpson 3/8: ",
                    suplevels[self.SIMPSON3_8] = float(raw_input()) #32.0/27.0
                else:
                    print "Cota Superior para Boole: ",
                    suplevels[self.BOOLE] = float(raw_input()) #2560.0 / 243.0


        # calculamos el h = (b-a)/n
        n = float(self._nodes - 1)
        h = (self._b - self._a) / n

        # Calculamos estimacion del error para los Trapezoidal
        error = fabs((n * pow(h, 3) * suplevels[self.TRAPEZOIDAL]) / 12.0)
        print "\n** Trapecios **"
        print "Aproximacion =", self._estvalues[self.TRAPEZOIDAL]
        print "Estimacion del Error: ", error
        print "Error Real =", fabs(rvalue - self._estvalues[self.TRAPEZOIDAL])

        # Calculamos estimacion del error para Simpson
        if self._usedform[self.SIMPSON]:
            error = fabs(((n/2.0) * pow(h, 5) * suplevels[self.SIMPSON]) / 90.0)
            print "\n** Simpson **"
            print "Aproximacion =", self._estvalues[self.SIMPSON]
            print "Estimacion del Error: ", error
            print "Error Real =", fabs(rvalue - self._estvalues[self.SIMPSON])

        # Calculamos estimacion del error para Simpson 3/8
        if self._usedform[self.SIMPSON3_8]:
            error = fabs((3*(n/3.0) * pow(h, 5) * suplevels[self.SIMPSON3_8]) / 80.0)
            print "\n** Simpson 3/8 **"
            print "Aproximacion =", self._estvalues[self.SIMPSON3_8]
            print "Estimacion del Error: ", error
            print "Error Real =", fabs(rvalue - self._estvalues[self.SIMPSON3_8])

        # Calculamos estimacion del error para Boole
        if self._usedform[self.BOOLE]:
            error = fabs((8*(n/4.0) * pow(h, 7) * suplevels[self.BOOLE]) / 945.0)
            print "\n** Boole **"
            print "Aproximacion =", self._estvalues[self.BOOLE]
            print "Estimacion del Error: ", error
            print "Error Real =", fabs(rvalue - self._estvalues[self.BOOLE])
