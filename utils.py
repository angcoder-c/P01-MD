import re 
from relacion import Relacion
from elemento import Elemento

def parseInput (inputStr: str):
    inputStr = inputStr.strip()

    # regex de tuplas
    pares = re.findall(r"\(([^,]+),\s*([^)]+)\)", inputStr)
    if pares:
        return [
            Relacion(
                a.strip(), 
                b.strip()
            ).__str__() for a, b in pares
        ]
    else:
        # elementos simples
        elementos = [
            x.strip() 
            for x in inputStr.split(",") 
            if x.strip()
        ]
        return elementos
    
def parse (inputStr: str):
    inputStr = inputStr.strip()

    # regex de tuplas
    pares = re.findall(r"\(([^,]+),\s*([^)]+)\)", inputStr)
    if pares:
        return [
            Relacion(
                a.strip(), 
                b.strip()
            ) for a, b in pares
        ]
    else:
        # elementos simples
        elementos = [
            x.strip() 
            for x in inputStr.split(",") 
            if x.strip()
        ]
        return [Elemento(e) for e in elementos]
    
def check_types(element: Relacion | Elemento):
    if type(element) == 'Relacion':
        return [
            str(element.a.valor), 
            str(element.b.valor)
        ]
    return [str(element.valor)]