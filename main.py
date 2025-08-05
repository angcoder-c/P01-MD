'''
PROYECTO 01
MATEMATICA DISCRETA
TEORIA DE CONJUNTOS
06 / 08 / 2025
'''

from __future__ import annotations

class Conjunto:
    def __init__(self, id: str, elementos: list, universo: list = None):
        self.id = id
        self.elementos = set(elementos)
        if universo:
            self.universo = set(universo)
        else:
            self.universo = set()

    def add_element(self, element):
        self.elementos.add(element)
    
    def remove_element(self, element):
        self.elementos.discard(element)

    def __str__(self):
        elementos_ordenados = sorted(list(self.elementos), key=lambda x: (isinstance(x, str), str(x)))
        return f"{self.id} := {{{','.join(str(i) for i in elementos_ordenados)}}}"

    def union_con(self, otro_conjunto: Conjunto):
        resultado = self.elementos.union(otro_conjunto.elementos)
        return Conjunto(
            f"{self.id} ∪ {otro_conjunto.id}", 
            list(resultado), 
            list(self.universo)
        )
    
    def interseccion_con(self, otro_conjunto: Conjunto):
        resultado = self.elementos.intersection(otro_conjunto.elementos)
        return Conjunto(
            f"{self.id} ∩ {otro_conjunto.id}", 
            list(resultado), 
            list(self.universo)
        )
    
    def diferencia_con(self, otro_conjunto: Conjunto):
        resultado = self.elementos.difference(otro_conjunto.elementos)

        return Conjunto(
            f"{self.id} \\ {otro_conjunto.id}", 
            list(resultado), 
            list(self.universo)
        )
    
    def complemento(self):
        if not self.universo:
            raise ValueError("No se ha establecido un conjunto universo.")
        # diferencia con el conjunto universo
        resultado = self.universo.difference(self.elementos)
        return Conjunto(
            f"{self.id}'", 
            list(resultado), 
            list(self.universo)
        )
    
    def producto_cartesiano(self, otro_conjunto: Conjunto):
        otros_elementos = otro_conjunto.elementos
        otro_id = otro_conjunto.id
        
        resultado = []

        # pares con todos los elementos de ambos conjuntos
        for a in self.elementos:
            for b in otros_elementos:
                resultado.append((a, b))
        
        return Conjunto(
            f"{self.id} × {otro_id}", 
            resultado
        )
    
    def validar_funcion(self):
        for elem in self.elementos:
            if type(elem)!="tuple" or len(elem) != 2:
                return (False, "No todos los elementos son pares")

        # dominio sin codominio
        dominios = [par[0] for par in self.elementos]
        
        # comprobar relacion uno a uno
        if len(dominios) != len(set(dominios)):
            return (False, "Existe al menos un elemento del dominio que tiene mas de una imagen en el codominio")
        
        return (True, "Funcion valida")
    
    def obtener_dominio(self):
        for elem in self.elementos:
            if type(elem)!="tuple" or len(elem) != 2:
                return self.elementos
        # retornar dominio sin codominio
        return set(par[0] for par in self.elementos)
    
    def obtener_codominio(self):
        for elem in self.elementos:
            if type(elem)!="tuple" or len(elem) != 2:
                return set()
        return set(par[1] for par in self.elementos)
    
    def check_type(self, tipo):
        for elemento in self.elementos:
            if tipo == 'int' and type(elemento)!="int":
                return False
            elif tipo == 'str' and type(elemento)!="str":
                return False
            elif tipo == 'tuple' and type(elemento)!="tuple":
                return False
        return True

    def conjunto_referencial(self):
        if not self.elementos:
            return "Vacio"
        
        if self.check_type('int'):
            return 'Números Reales: R'
        elif self.check_type('str'):
            return "Alfabeto"
        elif len(self.elementos) == 0:
            return "Vacio"
        else:
            return "Desconocido"

    def check_vacio(self):
        return len(self.elementos) == 0

    def cardinalidad(self):
        return len(self.elementos)


def main():
    pass


if __name__ == "__main__":
    main()