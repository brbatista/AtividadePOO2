class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, matricula):
        super().__init__(nome, sobrenome)
        self.matricula = matricula

    def get_matricula(self): 
        return self.matricula
      
    def set_matricula(self, matricula): 
        self.matricula = matricula 