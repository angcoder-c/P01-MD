'''
PROYECTO 01
MATEMATICA DISCRETA
TEORIA DE CONJUNTOS
06 / 08 / 2025
SEGUNDA ENTREGA: 10 / 09 / 2025
    - Composicion de relaciones
'''

from __future__ import annotations

class Conjunto:
    universo_global = set()

    def __init__(self, id: str, elementos: list):
        self.id = id
        self.elementos = set(elementos)

        Conjunto.universo_global.update(self.elementos)

    def add_element(self, element):
        self.elementos.add(element)
        Conjunto.universo_global.add(element)

    
    def remove_element(self, element):
        self.elementos.discard(element)

    def __str__(self):
        elementos_ordenados = sorted(list(self.elementos))
        return f"{self.id} = {{{','.join(str(i) for i in elementos_ordenados)}}}"

    def union_con(self, otro_conjunto: Conjunto):
        resultado = self.elementos.union(otro_conjunto.elementos)
        return Conjunto(
            f"{self.id} ∪ {otro_conjunto.id}", 
            list(resultado)
        )
    
    def interseccion_con(self, otro_conjunto: Conjunto):
        resultado = self.elementos.intersection(otro_conjunto.elementos)
        return Conjunto(
            f"{self.id} ∩ {otro_conjunto.id}", 
            list(resultado)
        )
    
    def diferencia_con(self, otro_conjunto: Conjunto):
        resultado = self.elementos.difference(otro_conjunto.elementos)

        return Conjunto(
            f"{self.id} \\ {otro_conjunto.id}", 
            list(resultado)
        )
    
    def complemento(self):
        # diferencia con el conjunto universo
        resultado = Conjunto.universo_global.difference(self.elementos)
        return Conjunto(f"{self.id}'", list(resultado))
    
    def producto_cartesiano(self, otro_conjunto: Conjunto):
        otros_elementos = otro_conjunto.elementos
        otro_id = otro_conjunto.id
        
        resultado = []

        # pares con todos los elementos de ambos conjuntos
        for a in self.elementos:
            for b in otros_elementos:
                resultado.append(f'{a}-{b}')
        
        return Conjunto(
            f"{self.id} × {otro_id}", 
            resultado
        )
    
    def validar_funcion(self):
        tempelem = [tuple(elem.split('-')) for elem in self.elementos]
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
        tempelem = [tuple(elem.split('-')) for elem in self.elementos]
        for elem in tempelem:
            if not isinstance(elem, tuple) or len(elem) != 2:
                return self.elementos
        # retornar dominio sin codominio
        return set(par[0] for par in tempelem)
    
    def obtener_codominio(self):
        tempelem = [tuple(elem.split('-')) for elem in self.elementos]
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
            return 'Números Enteros: ℤ'
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
            if '-' in str(elem):
                par = str(elem).split('-')
                if len(par) == 2:
                    pares_r.append((par[0], par[1]))
            
        # procesar la relacion s
        for elem in otra_relacion.elementos:
            if '-' in str(elem):
                par = str(elem).split('-')
                if len(par) == 2:
                    pares_s.append((par[0], par[1]))
            
        # composicion de la forma (a,b) o (c,d) = (a,d)
        composicion = []
        # (a,b) en s
        for (a, b) in pares_s:
            # (c,d) en R
            for (c, d) in pares_r:
                if b == c:
                    composicion.append(f"{a}-{d}")
            
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
            par_reflexivo = f"{elemento}-{elemento}"
            if par_reflexivo not in self.elementos:
                return False
        return True

    def es_simetrica(self):
        """Verifica si la relación es simétrica"""
        for elemento in self.elementos:
            if '-' in str(elemento):
                a, b = str(elemento).split('-')
                par_simetrico = f"{b}-{a}"
                if par_simetrico not in self.elementos:
                    return False
        return True

    def es_transitiva(self):
        """Verifica si la relación es transitiva"""
        pares = []
        for elem in self.elementos:
            if '-' in str(elem):
                par = str(elem).split('-')
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
            if '-' in str(elem):
                par = str(elem).split('-')
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
    
def mostrar_universo():
    elementos = sorted(Conjunto.universo_global)
    return "{" + ", ".join(str(e) for e in elementos) + "}"

def main():
    conjuntos = {}
    op=''

    while op != '0':
        op = input("""
        ======================
        BIENVENIDO
        ======================
        Nota: 
            elementos separados por comas (1,2,3)
            conjuntos por pares separados por guiones (1-2, 3-4, 5-6)
        ++++++++++++++++++++++
        ======================
        (1) Definir conjunto
        (2) Agregar elemento a conjunto
        (3) Union
        (4) Interseccion
        (5) Diferencia
        (6) Complemento
        (7) Producto cartesiano
        (8) Validar funcion
        (9) Obtener dominio y codominio
        (10) Conjunto referencial
        (11) Cardinalidad
        (12) Composicion de relaciones
        (13) Potencia de una relacion
        (14) Ver conjuntos
        (15) Propiedades de una relacion
        (16) Mostrar Conjunto Universo 
        (0) Salir
        
        >>>  """)


        if op == '1':
            id = input("Nombre: ")
            elementos = input("Elementos: ").split(',')
            conjuntos[id] = Conjunto(id, elementos)  
            print(f"Conjunto {id} definido correctamente.")

        if op == '2':
            id = input("Destino: ")
            if id in conjuntos:
                elemento = input("Elemento a agregar: ")
                conjuntos[id].add_element(elemento)
                print(f"Elemento agregado. {conjuntos[id]}")
            else:
                print("Conjunto no encontrado.")

        if op == '3':
            a = input("Conjunto A: ")
            b = input("Conjunto B: ")
            if a in conjuntos and b in conjuntos:
                resultado = conjuntos[a].union_con(conjuntos[b])
                print(resultado)
            else:
                print("Conjunto no existente.")

        if op == '4':
            a = input("Conjunto A: ")
            b = input("Conjunto B: ")
            if a in conjuntos and b in conjuntos:
                resultado = conjuntos[a].interseccion_con(conjuntos[b])
                print(resultado)
            else:
                print("Conjunto no existente.")

        if op == '5':
            a = input("Conjunto A: ")
            b = input("Conjunto B: ")
            if a in conjuntos and b in conjuntos:
                resultado = conjuntos[a].diferencia_con(conjuntos[b])
                print(resultado)
            else:
                print("Conjunto no existente.")

        if op == '6':
            id = input("Conjunto: ")
            if id in conjuntos:
                try:
                    resultado = conjuntos[id].complemento()
                    print(resultado)
                except ValueError as e:
                    print(f"ERROR: {e}")
            else:
                print("Conjunto no encontrado.")

        if op == '7':
            a = input("Conjunto A: ")
            b = input("Conjunto B: ")
            if a in conjuntos and b in conjuntos:
                resultado = conjuntos[a].producto_cartesiano(conjuntos[b])
                print(resultado)
            else:
                print("Conjunto no existente.")

        if op == '8':
            id = input("Conjunto: ")
            if id in conjuntos:
                valido, mensaje = conjuntos[id].validar_funcion()
                print(mensaje)
            else:
                print("Conjunto no encontrado.")

        if op == '9':
            id = input("Conjunto de pares: ")
            if id in conjuntos:
                dominio = conjuntos[id].obtener_dominio()
                codominio = conjuntos[id].obtener_codominio()
                print(f"Dominio: {dominio}")
                print(f"Codominio: {codominio}")
            else:
                print("Conjunto no encontrado.")

        if op == '10':
            id = input("Conjunto: ")
            if id in conjuntos:
                ref = conjuntos[id].conjunto_referencial()
                print(f"Conjunto referencial: {ref}")
            else:
                print("Conjunto no encontrado.")

        if op == '11':
            id = input("Conjunto: ")
            if id in conjuntos:
                print(f"Cardinalidad: {conjuntos[id].cardinalidad()}")
            else:
                print("Conjunto no encontrado.")
        
        if op == '12':
            a = input("Relacion R: ")
            b = input("Relacion S: ")

            # si estan en el conjunto
            if a in conjuntos and b in conjuntos:
                try:
                    resultado = conjuntos[a].composicion_relaciones(conjuntos[b])
                    print(f"Composicion R o S: {resultado}")

                except Exception as e:
                    print(f"ERROR: {e}")
            else:
                print("Relacion no existente")
        
        if op == '13':
            print("Potencia R^n\n==============")
            id = input("Relacion: ")
            if id in conjuntos:
                try:
                    n = int(input("n: "))
                    resultado = conjuntos[id].potencia_relacion(n)
                    print(f"R^{n}: {resultado}")

                except Exception as e:
                    print(f"ERROR: {e}")
            else:
                print("Relacion no existente.")
        if op == '14':
            for items in conjuntos.items():
                print(f"{items[0]} = {items[1].elementos}  | U = ", end='')
                mostrar_universo()
                
        if op == '15':  # Analizar propiedades de relación
            id = input("Relación a analizar: ")
            if id in conjuntos:
                relacion = conjuntos[id]
                
                # Preguntar por conjunto base para reflexividad
                base_id = input("Conjunto base para reflexividad (opcional): ")
                conjunto_base = conjuntos[base_id] if base_id in conjuntos else None
                
                print(f"\nPropiedades de {id}:")
                print(f"Reflexiva: {relacion.es_reflexiva(conjunto_base)}")
                print(f"Simétrica: {relacion.es_simetrica()}")
                print(f"Transitiva: {relacion.es_transitiva()}")
                print(f"Antisimétrica: {relacion.es_antisimetrica()}")
                if conjunto_base:
                    print(f"Relación de equivalencia: {relacion.es_relacion_equivalencia(conjunto_base)}")
            else:
                print("Relación no encontrada.")

        if op == '16':
            print("U = " + mostrar_universo())

        if op == '0':
            print("Bye")



if __name__ == "__main__":
    main()