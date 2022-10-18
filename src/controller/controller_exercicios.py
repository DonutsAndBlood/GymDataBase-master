from model.exercicios import Exercicio, Exercicios
from conexion.oracle_queries import OracleQueries

class Controller_Exercicios:
    def __init__(self):
        pass

    def cadastrar_exercicio(self) -> Exercicio:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_exercicio = input("Exercicio(Novo): ")

        if self.verifica_existencia_exercicio(oracle, codigo_exercicio):
            codigo_exercicio = input("Codigo (Novo): ")
            oracle.write(f"inset into alunos values ('{codigo_exercicio}', '{codigo_exercicio}')")

            df_exercicio = oracle.sqlToDataFrame(
                f"select codigo_exercicio, nome_exercicio from exercicios where codigo_exercicio = '{codigo_exercicio}'")
            novo_exercicio = Exercicios(df_exercicio.codigo_exercicio.values[0],df_exercicio.nome_exercicio.values[0])
            print(novo_exercicio.to_string())
            return novo_exercicio
        else:
            print(f"O Codigo {codigo_exercicio} não existe.")
            return None

    def excluir_exercicio(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_exercicio = int(input("Codigo do exercicio a ser excluído: "))

        if not self.verifica_existencia_exercicio(oracle, codigo_exercicio):
            df_aluno = oracle.sqlToDataFrame(f"select codigo_exercicio, nome_exercicio from exercicios where codigo_exercicio = {codigo_exercicio}")
            oracle.write(f"delete from alunos where codigo_exercicio = {codigo_exercicio}")
            codigo_excluido = Exercicios(df_aluno.codigo_exercicio.values[0], df_aluno.nome_exercicio.values[0])
            print("Exercicios removido com sucesso!")
            print(codigo_excluido.to_string())
        else:
            print(f"O codigo {codigo_exercicio} não existe.")

    def verifica_existencia_exercicio(self,oracle: OracleQueries,codigo_exercicio: int = None) -> bool:
        df_exercicio = oracle.sqlToDataFrame(f"select codigo_exercicio, nome_exercicio from exercicios where codigo_exercicio = {codigo_exercicio} f")
        return df_exercicio.empty
