"""
Vamos supor que precisamos criar um programa para cadastrar alunos em uma escola, armazenando informações como nome, idade e nota. Podemos utilizar um dicionário para representar cada aluno, onde a chave será o número de matrícula e o valor será outro dicionário contendo as informações do aluno.
"""
class Escola:
    def __init__(self):
        self.alunos = {}  

    def cadastrar_aluno(self, matricula, nome, idade, nota):
        
        if matricula in self.alunos:
            print("Matrícula já cadastrada.")
        else:
            
            aluno_info = {"nome": nome, "idade": idade, "nota": nota}
            
            self.alunos[matricula] = aluno_info
            print("Aluno cadastrado com sucesso.")

    def exibir_alunos(self):
        for matricula, info in self.alunos.items():
            print(f"Matrícula: {matricula}")
            print(f"Nome: {info['nome']}")
            print(f"Idade: {info['idade']}")
            print(f"Nota: {info['nota']}")
            print("--------------------")


escola = Escola()


escola.cadastrar_aluno(101, "João", 15, 8.5)
escola.cadastrar_aluno(102, "Maria", 16, 9.0)


escola.exibir_alunos()
