#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Tramos de edad

x=int(raw_input('Dime el año de tu nacimiento : '))

y=2018-x


if y<17:
  print 'Eres menor de edad'
elif y>=18 and y<30:
  print 'Aún eres joven'
elif y>=31 and y<45:
  print 'Eres madurito'
else:
  print 'Viejuno!'


