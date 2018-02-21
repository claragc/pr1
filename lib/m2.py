# -*- coding: utf-8 -*-

import os

def crea_dir(directorio):
	if os.access(directorio,0):
		return 1
	else:
		os.mkdir(directorio)
		return 0

# Listar nombre y tamaño de ficheros de un directorio 
def nom_tam(directorio):
	if not os.access(directorio,0):
		print "Directorio inexistente"
		exit()
	lista=os.listdir(directorio)
	for file in lista:
		f1=directorio+'/'+file
		if os.path.isfile(f1):
			print file +'--->'+str(os.path.getsize(f1))
