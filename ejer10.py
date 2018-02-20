#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pedir nombre y apellidos y sacar las iniciales

import sys

if len(sys.argv) != 4:
	print "Numero incorrecto de argumentos"
	exit()


print "Tus inciales son: "+sys.argv[1][0].upper()+'.'+sys.argv[2][0].upper()+'.'+sys.argv[3][0].upper()

