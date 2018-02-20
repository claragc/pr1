#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Buscar una letra en elnombre de un fichero

import os

directorio=raw_input('Dime un directorio: ')
letra=raw_input('Dime una letra: ')

lista=os.listdir(directorio)

for fichero in lista:
	if fichero.count(letra)>0:
		print fichero
 

