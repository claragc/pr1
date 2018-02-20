#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Buscar ficheros .sh en un directorio

import os

directorio=raw_input('Dime un directorio: ')

lista=os.listdir(directorio)

for fichero in lista:
	if fichero[-3:] == '.sh':
		print fichero
 

