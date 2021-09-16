# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 18:28:58 2021

@author: micha
"""

#Ejercicio 2:
    
datos_2021=[1,2,3,4,5,6,7,100,91,110,900,21,33,32,2,48,10,13,13,16,15,1302]

def numpares(datos_2021):
    pares=[]
    
    for q in datos_2021:
        if q % 2 == 0:
            pares.append(q)
            
    return(pares)

def numimpares(datos_2021):
    impares=[]
    
    for s in datos_2021:
        if s % 2 != 0:
            impares.append(s)
            
    return(impares)

def valoresA(datos_2021):
    valA=[]
    val=[]
    
    for a in datos_2021:
        if a not in val:
            val.append(a)
        else:
            valA.append(a)
    return(valA)
    
    
resultado= numpares(datos_2021)
resultado2= numimpares(datos_2021)
resultado3= valoresA(datos_2021)
tupla1=tuple(resultado)
tupla2=tuple(resultado2)
tupla3=tuple(resultado3)

print(f"Los números pares de la tupla son:{tupla1}")
print(f"Los números impares de la tupla son:{tupla2}")
print(f"Los números atípicos de la tupla son:{tupla3}, porque se repiten.")

print(type (tupla1))
print(type (tupla2))
print(type (tupla3))



            
    

        
      