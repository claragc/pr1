# -*- coding: utf-8 -*-

import os

def crea_dir(directorio)
	if os.access(directorio,0):
		return 1
	else:
		os.mkdir(directorio
		return 0
