#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pedir nombre y ponerlo en mayúsculas

#import os
import sys

if len(sys.argv) != 2:
	print "Numero incorrecto de argumentos"
	exit()
print sys.argv[0]
print sys.argv[1]
print "Tu nombre en mayúsculas es: "+sys.argv[1].upper()

