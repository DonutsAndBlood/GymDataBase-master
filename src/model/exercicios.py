class Exercicios:
    def __init__(
        self,
        codigo_exercicio: int = None,
        repeticoes: int = None,
        grupo_muscular: str = None,
        nome_exercicio: str = None,
    ):
        self.set_codigo_exercicio(codigo_exercicio)
        self.set_repeticoes(repeticoes)
        self.set_grupo_muscular(grupo_muscular)
        self.set_nome_exercicio(nome_exercicio)

    def set_codigo_exercicio(self, codigo_exercicio: int):
        self.codigo_exercicio = codigo_exercicio

    def set_repeticoes(self, repeticoes: int):
        self.repeticoes = repeticoes

    def set_grupo_muscular(self, grupo_muscular: str):
        self.grupo_muscular = grupo_muscular

    def set_nome_exercicio(self, nome_exercicio: str):
        self.nome_exercicio = nome_exercicio    

    def get_codigo_exercicio(self) -> int:
        return self.codigo_exercicio

    def get_repeticoes(self) -> int:
        return self.repeticoes

    def get_grupo_muscular(self) -> str:
        return self.grupo_muscular

    def get_nome_exercicio(self) -> str:
        return self.nome_exercicio

    def to_string(self) -> str:
        return f"""
        ___________________________________________________

        |Codigo do exercicio - {self.get_codigo_exercicio()}
        |Repeticoes - {self.get_repeticoes()}
        |Grupo muscular - {self.get_grupo_muscular()}
        ___________________________________________________"""