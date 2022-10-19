from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_alunos = config.QUERY_COUNT.format(tabela="alunos")
        self.qry_total_exercicios = config.QUERY_COUNT.format(tabela="exercicios")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Brayan Bautz, Breno Sandrini, Caio Occhi, Victor Lima"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_total_alunos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_alunos).values[0]

    def get_total_exercicios(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_exercicios).values[0]


    def get_updated_screen(self):
        return f"""
        ########################################################
        #                       SUPER GYM                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - Alunos:          {str(self.get_total_alunos())}
        # #      2 - Exercicios:      {str(self.get_total_exercicios())}   
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """