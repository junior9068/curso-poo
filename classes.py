
class Gato:
    """Classe para trabalhar com gatos"""
    def __init__(self, nome):
        self.nome = nome
        print(f"Seu gato se chama {self.nome}")

    def get_nome(self):
        a = self.nome
        return a


class TesteManipulacao():
    """Classe para exemplificar o uso do getter e setter"""
    def __init__(self, valor):
        self.x = valor
   

    def get_valor(self):
        """ Método getter para retornar o valor do atributo x"""
        return self.x


    def set_valor(self, v):
        """ Método setter para atribuir um novo o valor ao atributo x"""
        self.x = v


