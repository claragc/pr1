# -*- coding: utf-8 -*-

import sys

def saludar(saludo):
	print saludo

def iniciales(nombre,ape1,ape2): 
	iniciales=nombre[0]+'.'+ape1[0]+'.'+ape2[0]+'.'
	return "Tus inciales son: "+iniciales.upper()

def iniciales_arbitrario(nombre,ape1,*ape2):
        iniciales=nombre[0]+'.'+ape1[0]
	for apellido in ape2:
		iniciales=iniciales+'.'+apellido[0]
        return "Tus inciales son: "+iniciales.upper()

