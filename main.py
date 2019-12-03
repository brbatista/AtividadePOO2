from Pessoa import Pessoa
from Aluno import Aluno
from Professor import Professor


pessoa = Pessoa("nome_pessoa", "sobrenome_pessoa")
aluno = Aluno("nome_aluno", "sobrenome_aluno", "matricula")
professor = Professor("nome_professor", "sobrenome_professor", "codigo_professor")


pessoa.mostrar_informacoes()
aluno.mostrar_informacoes()
professor.mostrar_informacoes()
