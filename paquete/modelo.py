import abc #Importamos el abc para clase abstracta

class PersonaEquipo(metaclass = abc.ABCMeta):#Creamos la clase
	def __init__(self, nom):
		self.nombre = nom

	#Definimos como clase abstracta
	__metaclass__ = abc.ABCMeta

	#Metodo abstracto sin implementar
	@abc.abstractmethod
	def entrenar():
		pass


class Entrenador(PersonaEquipo):#Creamos la subclase Entrenador que hereda de Persona Equipo
	def __init__(self, n):
		super(Entrenador, self).__init__(n)
		self.codigo_entrenador = " "
	
	#Metodos de agregar y obtener
	def agregar_codigo_entrenador(self, cod):
		self.codigo_entrenador = cod

	def obtener_codigo_entrenador(self):
		return self.codigo_entrenador

	#Metodo de entrenar implementado
	def entrenar(self):
		print("Yo: %s, entrenador soy director del entrenamiento\n"% self.nombre)


class Futbolista(PersonaEquipo):#Creamos la clase Futbolista que hereda de la clase Persona Equipo
	def __init__(self, n):
		super(Futbolista, self).__init__(n)
		self.posicion_campo = " "

	#Metodos de agregar y obtener
	def agregar_posicion_campo(self,pos):
		self.posicion_campo = pos

	def obtener_posicion_campo(self):
		return self.posicion_campo

	#Metodo de entrenar implementado
	def entrenar(self):
		print("Yo: %s, futbolista hago práctica en el entrenamiento\n"% self.nombre)


class MedicoEquipo(PersonaEquipo):#Creamos la clase MedicoEquipo que hereda de la clase Persona Equipo
	def __init__(self, n):
		super(MedicoEquipo, self).__init__(n)
		self.titulo = " "

	#Metodos de agregar y obtener
	def agregar_titulo(self,tit):
		self.titulo = tit

	def obtener_titulo(self):
		return self.titulo

	#Metodo de entrenar implementado
	def entrenar(self):
		print("Yo: %s, medico atiendo a los jugadores en el entrenamiento\n"% self.nombre)


class PresidenteEquipo(PersonaEquipo):#Creamos la clase Presidente Equipo que hereda de la clase Persona Equipo
	def __init__(self, n):
		super(PresidenteEquipo, self).__init__(n)
		self.numero_propiedades = " "

	#Metodos de agregar y obtener
	def agregar_numero_propiedades(self, num_propi):
		self.numero_propiedades = num_propi

	def obtener_numero_propiedades(self):
		return self.numero_propiedades

	#Metodo de entrenar implementado
	def entrenar(self):
		print("Yo: %s, presidente pongo el dinero para el entrenamiento\n"% self.nombre)