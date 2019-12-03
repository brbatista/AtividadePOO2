class Cliente(object):
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def get_nome(self): 
        return self.nome 
      
    def set_nome(self, nome): 
        self.nome = nome 

    def get_sobrenome(self): 
        return self.sobrenome 
      
    def set_sobrenome(self, sobrenome): 
        self.sobrenome = sobrenome 