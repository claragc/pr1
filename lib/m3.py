# -*- coding: utf-8 -*-

import os

#Recibe directorio y tamaño y quieres listar los ficheros mas grandes de ese tamaño
def mayor_tam(directorio,tam):
	if not os.access(directorio,0):
		print 'Directorio inexistente'
		exit()
	if tam[-1].upper() not in ('K','M','G'):
		print 'Solo puede ser en K, M o G'
		exit()
	t=int(tam[:-1])
	if tam[-1]=='K':
		t=t*1024
	elif tam[-1]=='M':
		t=t*1024*1024
	else:
		t*1024*1024*1024
	lista=os.listdir(directorio)
	for file in lista:
		f1=directorio+'/'+file
		if os.path.isfile(f1):
			if os.path.getsize(f1)>t:
				print file + '--->'+str(os.path.getsize(f1))

# Sacar contenido de ficheros
def cat(fichero):
	if not os.access(fichero,0):
		print "Fichero no existe"
		exit()
	if not os.path.isfile(fichero):
		print "No es un fichero"
		exit()
	archivo=open(fichero,"r")
	contenido=archivo.read()
	print contenido
	archivo.close()

# Funcion grep
def grep(fichero,texto):
	if not os.access(fichero,0):
		print "Fichero no existe"
		exit()
	if not os.path.isfile(fichero):
		print "No es un fichero"
		exit()
	archivo=open(fichero,"r")
	while True:
		linea=archivo.readline()
		if not linea:
			break
		if linea.count(texto)>0:
			print linea
	archivo.close()

# Funcion copiar archivo
def cp(f1,f2):
	arc1=open(f1,"r")
	arc2=open(f2,"w")
	lineas=arc1.readlines()
	for lin in lineas:
		arc2.write(lin)
	arc1.close()
	arc2.close()

# Funcion cp grep -> copia del f1 al f2 las lineas que tengan el texto "texto" en modo append
def cp_grep(f1,f2,texto):
	fd1=open(f1,"r")
	fd2=open(f2,"a")
	while True:
		linea=fd1.readline()
		if not linea:
			break
		if linea.count(texto)>0:
			fd2.write(linea)
	fd1.close()
	fd2.close()
