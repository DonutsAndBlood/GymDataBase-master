from conexion.oracle_queries import OracleQueries

class Relatorios:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("src/sql/relatorio_exercicio_favorito.sql") as f:
            self.query_relatorio_exercicio_favorito = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("src/sql/relatorio_alunos.sql") as f:
            self.query_relatorio_alunos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("src/sql/relatorio_exercicios.sql") as f:
            self.query_relatorio_exercicios = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("src/sql/relatorio_quant_pagamentos.sql") as f:
            self.query_relatorio_quant_pagamentos = f.read()

    def get_relatorio_exercicio_favorito(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_exercicio_favorito))
        input("Pressione Enter para Sair do Relatório de preferidos")

    def get_relatorio_alunos(self):

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_alunos))
        input("Pressione Enter para Sair do Relatorio de alunos")

    def get_relatorio_exercicios(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_exercicios))
        input("Pressione Enter para Sair do Relatório de exercícios")

    def get_relatorio_quant_pagamentos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_quant_pagamentos))
        input("Pressione Enter para Sair do Relatório de quantidade de inadimplentes")
