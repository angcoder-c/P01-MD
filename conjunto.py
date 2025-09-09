from __future__ import annotations
from elemento import Elemento
from relacion import Relacion
from utils import parse, check_types

class Conjunto:
    def __init__(self, id: str, elementos: list, universo: list = None):
        self.id = id
        self.elementos = set(elementos)
        if universo:
            elements = [
                item for e in map(
                    check_types, 
                    parse(','.join(elementos))
                ) 
                for item in e
            ]
            self.universo = set(universo + elements)
        else:
            self.universo = set()

    def add_element(self, element: Relacion | Elemento):
        if type(element) == 'Relacion':
            self.universo.add(element.a.valor)
            self.universo.add(element.b.valor)
            self.elementos.add(element.__str__())
        else:
            self.universo.add(element.valor)
            self.elementos.add(element.valor)
    
    def remove_element(self, element: Relacion | Elemento):
        if type(element) == 'Relacion':
            self.universo.discard(element.a.valor)
            self.universo.discard(element.b.valor)
            self.elementos.add(element.__str__())
        else:
            self.universo.discard(element.valor)
            self.elementos.discard(element.valor)

    def __str__(self):
        elementos_ordenados = sorted(list(self.elementos))
        return f"{self.id} = {{{','.join(str(i) for i in elementos_ordenados)}}}"

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
                resultado.append(f'({a},{b})')
        
        return Conjunto(
            f"{self.id} × {otro_id}", 
            resultado
        )
    
    def validar_funcion(self):
        tempelem = [
            tuple(
                elem
                .replace('(', '')
                .replace(')', '')
                .split(',')
            ) 
            for elem in self.elementos
        ]

        for elem in tempelem:
            if not isinstance(elem, tuple) or len(elem) != 2:
                return (False, "No todos los elementos son pares")

        # dominio sin codominio
        dominios = [par[0] for par in tempelem]
        
        # comprobar relacion uno a uno
        if len(dominios) != len(set(dominios)):
            return (False, "Existe al menos un elemento del dominio que tiene mas de una imagen en el codominio")
        
        return (True, "Funcion valida")
    
    def obtener_dominio(self):
        tempelem = [
            tuple(
                elem
                .replace('(', '')
                .replace(')', '')
                .split(',')
            ) 
            for elem in self.elementos
        ]

        for elem in tempelem:
            if not isinstance(elem, tuple) or len(elem) != 2:
                return self.elementos
        # retornar dominio sin codominio
        return set(par[0] for par in tempelem)
    
    def obtener_codominio(self):
        tempelem = [
            tuple(
                elem
                .replace('(', '')
                .replace(')', '')
                .split(',')
            ) 
            for elem in self.elementos
        ]

        for elem in tempelem:
            if not isinstance(elem, tuple) or len(elem) != 2:
                return set()
        return set(par[1] for par in tempelem)
    
    def check_type(self, tipo):
        for elemento in self.elementos:
            try:
                if tipo == 'int':
                    int(elemento)
                elif tipo == 'str':
                    str(elemento)
                else:
                    return False
            except:
                return False
        return True



    def conjunto_referencial(self):
        if not self.elementos:
            return "Vacio"
        
        if self.check_type('int'):
            return 'Numeros reales: R'
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
    
    def composicion_relaciones(self, otra_relacion: Conjunto):
        # r es self y s es otra_relacion de tuplas
        pares_r = []
        pares_s = []
            
        # parsear relaciones a tuplas
        for elem in self.elementos:
            if ',' in str(elem):
                par = str(elem).replace('(', '').replace(')', '').split(',')
                if len(par) == 2:
                    pares_r.append((par[0].strip(), par[1].strip()))
            
        # procesar la relacion s
        for elem in otra_relacion.elementos:
            if ',' in str(elem):
                par = str(elem).replace('(', '').replace(')', '').split(',')
                if len(par) == 2:
                    pares_s.append((par[0].strip(), par[1].strip()))
            
        # composicion de la forma (a,b) o (c,d) = (a,d)
        composicion = []
        # (a,b) en s
        for (a, b) in pares_s:
            # (c,d) en R
            for (c, d) in pares_r:
                if b == c:
                    composicion.append(f"({a},{d})")
            
        return Conjunto(
            f"({self.id} o {otra_relacion.id})",
            composicion
        )
    
    def potencia_relacion(self, n: int):
        # potencia de la forma R^n = R^(n-1) o R

        if n <= 0:
            raise ValueError("La potencia debe ser positiva")
        
        if n == 1:
            return Conjunto(
                f"{self.id}^1",
                list(self.elementos)
            )
        
        # calcular R^n
        resultado = Conjunto(f"{self.id}_temp", list(self.elementos))
        
        for i in range(2, n + 1):
            resultado = resultado.composicion_relaciones(self)
            resultado.id = f"{self.id}^{i}"
        
        return resultado
    
    def es_reflexiva(self, conjunto_base: Conjunto = None):
        """Verifica si la relación es reflexiva"""
        if not conjunto_base:
            # Si no se proporciona conjunto base, usar el dominio
            dominio = self.obtener_dominio()
        else:
            dominio = conjunto_base.elementos
        
        for elemento in dominio:
            par_reflexivo = f"({elemento},{elemento})"
            if par_reflexivo not in self.elementos:
                return False
        return True

    def es_simetrica(self):
        """Verifica si la relación es simétrica"""
        for elemento in self.elementos:
            if ',' in str(elemento):
                a, b = str(elemento).replace('(', '').replace(')', '').split(',')
                par_simetrico = f"({b},{a})"
                if par_simetrico not in self.elementos:
                    return False
        return True

    def es_transitiva(self):
        """Verifica si la relación es transitiva"""
        pares = []
        for elem in self.elementos:
            if ',' in str(elem):
                par = str(elem).replace('(', '').replace(')', '').split(',')
                if len(par) == 2:
                    pares.append((par[0], par[1]))
        
        for (a, b) in pares:
            for (c, d) in pares:
                if b == c:  # Si (a,b) y (b,d) existen
                    if (a, d) not in pares:  # Entonces (a,d) debe existir
                        return False
        return True

    def es_antisimetrica(self):
        """Verifica si la relación es antisimétrica"""
        pares = []
        for elem in self.elementos:
            if ',' in str(elem):
                par = str(elem).replace('(', '').replace(')', '').split(',')
                if len(par) == 2:
                    pares.append((par[0], par[1]))
        
        for (a, b) in pares:
            if a != b and (b, a) in pares:
                return False
        return True

    def es_relacion_equivalencia(self, conjunto_base: Conjunto = None):
        """Verifica si es relación de equivalencia"""
        return (self.es_reflexiva(conjunto_base) and 
                self.es_simetrica() and 
                self.es_transitiva())