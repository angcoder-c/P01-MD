'''
PROYECTO 01
MATEMATICA DISCRETA
TEORIA DE CONJUNTOS
06 / 08 / 2025
SEGUNDA ENTREGA: 10 / 09 / 2025
    - Composicion de relaciones
'''

from __future__ import annotations
from elemento import Elemento
from relacion import Relacion
from utils import parseInput
from conjunto import Conjunto

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
        (0) Salir
        
        >>>  """)


        if op == '1':
            id = input("Nombre: ")
            elementsInput = input("Elementos: ")
            elementos = parseInput(elementsInput)
            universo = input("Universo (opcional): ").strip()
            universo = [
                x.strip()
                for x in universo.split(",")
            ] if universo else None

            conjuntos[id] = Conjunto(id, elementos, universo)
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
                print(f"{items[0]} = {items[1].elementos}  |  U = {items[1].universo}")
                
        if op == '15':  # Analizar propiedades de relación
            id = input("Relación a analizar: ")
            if id in conjuntos:
                relacion = conjuntos[id]
                
                # Preguntar por conjunto base para reflexividad
                base_id = input("Conjunto base para reflexividad (opcional): ")
                conjunto_base = conjuntos[base_id] if base_id in conjuntos else None
                
                print(f"\nPropiedades de {id}:")
                print(f"Reflexiva: {relacion.es_reflexiva(conjunto_base)}")
                print(f"Simetrica: {relacion.es_simetrica()}")
                print(f"Transitiva: {relacion.es_transitiva()}")
                print(f"Antisimetrica: {relacion.es_antisimetrica()}")
                if conjunto_base:
                    print(f"Relacion de equivalencia: {relacion.es_relacion_equivalencia(conjunto_base)}")
            else:
                print("Relacion no encontrada.")
        if op == '0':
            print("Bye")



if __name__ == "__main__":
    main()