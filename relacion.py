from elemento import Elemento

class Relacion:
    def __init__(self, a: int | str, b: int | str):
        self.a = Elemento(a)
        self.b = Elemento(b)
    
    def __str__(self):
        return f'({self.a.valor}, {self.b.valor})'
    
    def __repr__(self):
        return f'({self.a.valor}, {self.b.valor})'