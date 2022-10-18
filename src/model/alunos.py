from model.exercicios import Exercicios


class Alunos:
    def __init__(
        self,
        nome_aluno: str = None,
        cpf: str = None,
        pagamento: int = None,
        vencimento_mensalidade: str = None,
        telefone: int = None,
        exercicio: Exercicios=None


    ):
        self.set_nome_aluno(nome_aluno)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_pagamento(pagamento)
        self.set_vencimento_mensalidade(vencimento_mensalidade)
        self.set_exercicio(exercicio)

    def set_nome_aluno(self, nome_aluno: str):
        self.set_nome_aluno = nome_aluno

    def set_cpf(self, cpf: str):
        self.set_cpf = cpf

    def set_telefone(self, telefone: int):
        self.set_telefone = telefone

    def set_pagamento(self, pagamento: int):
        self.pagamento = pagamento

    def set_vencimento_mensalidade(self, vencimento_mensalidade: str):
        self.set_vencimento_mensalidade = vencimento_mensalidade

    def set_exercicio(self) -> Exercicios:
        return self.exercicio

    def get_nome_aluno(self) -> str:
        return self.nome_aluno

    def get_cpf(self) -> str:
        return self.set_cpf

    def get_telefone(self) -> str:
        return self.telefone

    def get_pagamento(self) -> int:
        return self.pagamento

    def get_vencimento_mensalidade(self) -> str:
        return self.vencimento_mensalidade

    def get_exercicio(self) -> Exercicios:
        return self.exercicio

    def to_string(self):
        return f"nome.aluno: {self.get_nome_aluno()} | cpf: {self.get_cpf()}| telefone:{self.get_telefone()} | pagamento:{self.get_pagamento()} | vencimento: {self.get_vencimento_mensalidade()} | exercicio: Prod.: {self.get_exercicio().get_nome_exercicio()}"
