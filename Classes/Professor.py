from Classes.Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, sobrenome, codigo):
        super().__init__(nome, sobrenome)
        self.codigo = codigo

    def get_codigo(self): 
        return self.codigo
      
    def set_codigo(self, codigo): 
        self.codigo = codigo

    def mostrar_informacoes(self):
        print("Nome: "+self.nome + ", Sobrenome: " + self.sobrenome+", Código: " + self.codigo)