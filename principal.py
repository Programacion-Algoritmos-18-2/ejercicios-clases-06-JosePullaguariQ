#Importamos el paquete donde este el modelo.py
from paquete.modelo import *

#p = PersonaEquipo()

#Creamos el primer objeto futbolista
futbolista = Futbolista("Antonio")

#Creamos el segundo objeto medico
medico = MedicoEquipo("Ramon")

#Creamos el tecer objeto presidente
presidente = PresidenteEquipo("Francisco")

#Creamos el cuarto objeto entrenador
entrenador = Entrenador("José")

#Creamos la lista con los objetos
lista = [futbolista, medico, presidente, entrenador]

#Creamos un for para recorrer la lista
for l in lista:
	l.entrenar()
