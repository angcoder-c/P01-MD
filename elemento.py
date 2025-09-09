class Elemento:
    def __init__(self, valor: int | str):
        try:
            valor = int(valor)
        except ValueError:
            pass
        
        self.valor = valor
        self.type = type(valor)
    
    def __str__(self):
        return f'{self.valor}'
    
    def __repr__(self):
        return f'{self.valor}'