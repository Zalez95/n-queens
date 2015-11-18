#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Solucion al problema de las N-Reinas mediante mediante distintos
	algoritmos.
"""
__author__ = "Daniel Gonzalez"
__version__= "1.0"

import random

SIMBOLO_REINA = 'q'		# Simbolo que representara a un reina
SIMBOLO_POSICION = '='	# Simbolo que representara a una posicion no amenazada

class N_Reinas:
	"""
		Clase para calcular el problema de las N-Reinas mediante distintos
		algoritmos.

		Atributos:
			numeroN (int): numero de dimensiones del tablero (numeroN*numeroN)
				y de reinas que tenemos que introducir en ese tablero.
			numeroPiezasColocadas (int): numero de piezas que hemos tenido
				que colocar para obtener el resultado final.
	"""
	def __init__(self, numeroN):
		assert numeroN > 3, "El numero N (%i) ha de ser mayor de 3." %numeroN
		self.numeroN = numeroN
		self.numeroPiezasColocadas = 0

	def calculaReinasLV(self):
		"""
			Retorna la primera solucion encontrada al problema de las 
			n-reinas. El calculo se	realiza mediante un algoritmo 
			probabilista de las Vegas.
		"""
		flag = True
		while(flag):
			solucion = self.lasVegas()
			if solucion:
				flag = False
		return self.resToList(solucion, 0, 1)

	def lasVegas(self):
		"""
			Retorna un resultado correcto del problema de las n-reinas, 
			en caso de fallo retorna una lista vacia como resultado.
		"""
		listaReinas = []
		for fila in range(self.numeroN):
			posiciones = self.posicionesPosibles(listaReinas, fila)

			# Imprimir pasos por pantalla
			
			imprimeResultado(self.numeroN, self.resToList(listaReinas, 0, 1),
				SIMBOLO_REINA)
			raw_input("Presiona Enter para continuar.")
			print "posiciones: ",
			imprimeResultado(self.numeroN, self.resToList(posiciones, fila, 0), 
				SIMBOLO_POSICION)
			raw_input("Presiona Enter para continuar.")
			

			if posiciones:
				seleccion = random.randint(0, len(posiciones)-1)
				listaReinas.append(posiciones[seleccion])
				self.numeroPiezasColocadas += 1
			else:
				return posiciones					# Fallo
		return listaReinas							# Exito

	def calculaReinasBT(self, listaReinas):
		"""	
			Retorna la primera solucion encontrada al problema de las 
			n-reinas. El calculo se realiza mediante un algoritmo de 
			vuelta atras (BackTracking).

			Parametros:
				listaReinas ([int]): lista con las reinas calculadas hasta
					ahora, inicialmente ha de ser una lista vacia.
		"""
		if (len(listaReinas) == self.numeroN):
			return self.resToList(listaReinas, 0, 1)	# Caso Base (Exito)

		fila = len(listaReinas)
		posiciones = self.posicionesPosibles(listaReinas, fila)
		for i in range(len(posiciones)):
			
			# Imprimir pasos por pantalla
			"""
			imprimeResultado(self.numeroN, self.resToList(listaReinas, 0, 1),
				SIMBOLO_REINA)
			raw_input("Presiona Enter para continuar.")
			print "posiciones: ",
			imprimeResultado(self.numeroN, self.resToList(posiciones, fila, 0), 
				SIMBOLO_POSICION)
			raw_input("Presiona Enter para continuar.")
			"""

			listaReinas.append(posiciones[i])
			self.numeroPiezasColocadas += 1
			listaReinas = self.calculaReinasBT(listaReinas)
			if (len(listaReinas) == self.numeroN):
				return listaReinas						# Exito

		# Imprimir pasos por pantalla
		"""
		imprimeResultado(self.numeroN, self.resToList(listaReinas, 0, 1),
			SIMBOLO_REINA)
		raw_input("Presiona Enter para continuar.")
		imprimeResultado(self.numeroN, self.resToList(posiciones, fila, 0), 
			SIMBOLO_POSICION)
		raw_input("Presiona Enter para continuar.")
		"""

		if listaReinas:
			listaReinas.pop()
			return listaReinas						# Fallo (Vuelta atras)
		else:
			return listaReinas						# Solucion no encontrada

	def posicionesPosibles(self, listaReinas, fila):
		"""
			Retorna una lista con las posiciones no amenzadas por otras
			reinas en la fila actual.

			Parametros:
				listaReinas ([int]): lista con las posiciones de las reinas.
				fila (int): fila del tablero sobre la que queremos comprobar
					que posiciones no estan amenazadas.
		"""
		posiciones = []
		for columna in range(self.numeroN):
			if not self.amenaza(listaReinas, fila, columna):
				posiciones.append(columna)
		return posiciones

	def amenaza(self, listaReinas, fila, columna):
		"""
			Retorna si la posicion seleccionada esta amenzada (True)
			o no (False) por otras Reinas.

			Parametros:
				listaReinas ([int]): lista con las posiciones de las reinas.
				fila (int): fila de la posicion que queremos comprobar.
				columna (int): columna de la posicion que queremos comprobar.
		"""
		for i in range(len(listaReinas)):
			# Comprobacion de las columnas
			if (listaReinas[i] == columna):
				return True
			# Comprobacion de las diagonales
			if (listaReinas[i] - columna == i - fila):
				return True
			if (listaReinas[i] - columna == fila - i):
				return True
		return False

	def resToList(self, listaElementos, filaIni, incremento):
		"""
			Retorna una lista de la forma (fila, columna) a partir de una lista
			de columnas.

			Parametros:
				listaElementos ([int]): lista con las posiciones de los 
					elementos que queremos imprimir.
				filaIni (int): fila inicial
				incremento (int): numero en que se diferenciara la fila de
					dos elementos consecutivos.
		"""
		respuesta = []
		cont = filaIni
		if listaElementos:
			for i in range(len(listaElementos)):
				respuesta.append((cont,listaElementos[i]))
				cont += incremento
		print respuesta
		return respuesta

def imprimeResultado(numeroN, listaElementos, simbolo):
	"""
		Muestra por pantalla la posicion que ocupan los elementos indicados
		dentro de un tablero, siendo '-' una posicion vacia y simbolo una 
		posicion con un elemento.

		Parametros:
			numeroN (int): dimensiones del tablero.
			listaElementos ([int]): lista con las posiciones de los elementos
				que queremos imprimir.
			simbolo (char): simbolo que se quier imprimir en los lugares
				indicados por listaElementos.
	"""
	print "Tablero:"
	for fila in range(numeroN):
		print '|',
		for columna in range(numeroN):
			flag = False
			for i in range(len(listaElementos)):
				if ((fila == listaElementos[i][0]) and
						(columna == listaElementos[i][1])):
					flag = True
					i = len(listaElementos)
			if flag:
				print ' ' + simbolo,
			else:
				print " -",
		print " |"


def getNumero():
	"""
		Retorna el valor del numero N introducido por el usuario.
	"""
	flag = True
	while(flag):
		entrada = raw_input("Introduzca el valor de N.\n")
		try:
			numero = int(entrada)
			if (numero > 3):
				flag = False
			else:
				print "El numero ha de ser mayor de 3."
		except ValueError:
			print "Introduzca un entero."
	return numero

def main():
	n = getNumero()
	reinas = N_Reinas(n)
	solucion = reinas.calculaReinasLV()
	#solucion = reinas.calculaReinasBT([])
	imprimeResultado(n, solucion, SIMBOLO_REINA)
	print "Resultado: ", solucion
	print "Numero de piezas colocadas: ", reinas.numeroPiezasColocadas

if __name__ == "__main__":
	main()