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

