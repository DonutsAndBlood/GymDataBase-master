from model.exercicios import Exercicio, Exercicios
from conexion.oracle_queries import OracleQueries

class Controller_Exercicios:
    def __init__(self):
        pass

    def cadastrar_exercicio(self) -> Exercicios:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        nome_exercicio = input("Nome do novo exercicio: ")
        repeticoes = input("Número de repetições: ")
        grupo_muscular= input("Grupo muscular treinado: ")   

        oracle.write(f"inset into exercicios values ('EXERCICIOS_CODIGO_EXERCICIO_SEQ.NEXTVAL,{repeticoes},'{nome_exercicio}','{grupo_muscular}')")
        
        df_exercicio = oracle.sqlToDataFrame(
            f"select codigo_exercicio, nome_exercicio from exercicios where nome_exercicio = '{nome_exercicio}'")
        novo_exercicio = Exercicios(df_exercicio.codigo_exercicio.values[0],df_exercicio.repeticoes.values[0],df_exercicio.grupo_muscular.values[0],df_exercicio.nome_exercicio.values[0])
        print(novo_exercicio.to_string())
        return novo_exercicio

    def atualizar_exercicios(self):
        oracle = OracleQueries(can_write= True)
        oracle.connect()

        codigo_exercicio = int(input("Insira o código do exercício a ser alterado"))

        if not self.verifica_existencia_exercicio(oracle, codigo_exercicio):
            print("1 - Nome\n 2 - Repetições")
            aux = int(input("Insira qual atributo irá ser alterado"))      
            if aux == 1:
                novo_nome = input("Insira o novo nome: ")
                oracle.write(f"update exercicios set nome_exercicio = '{novo_nome}' where codigo_exercicio = {codigo_exercicio}")
                df_exercicio = oracle.sqlToDataFrame(f"Select codigo_exercicio, nome_exercicio, repeticoes, grupo_muscular from exercicioss where codigo_exercicio = {codigo_exercicio}")
                exercicio_atualizado = Exercicios(df_exercicio.codigo_exercicio.values[0], df_aluno.repeticoes.values[0],df_aluno.grupo_muscular.values[0], df_aluno.nome_exercicio.values[0])
                print(exercicio_atualizado.to_string())
                return exercicio_atualizado
            elif aux == 2:
                novo_repeticoes = input("Insira o novo número de repetições: ")
                oracle.write(f"update exercicios set repeticoes = '{novo_repeticoes}' where codigo_exercicio = {codigo_exercicio}")
                df_aluno = oracle.sqlToDataFrame(f"Select codigo_exercicio, nome_exercicio, repeticoes, grupo_muscular from exercicioss where codigo_exercicio = {codigo_exercicio}")
                exercicio_atualizado = Exercicios(df_exercicio.codigo_exercicio.values[0], df_aluno.repeticoes.values[0],df_aluno.grupo_muscular.values[0], df_aluno.nome_exercicio.values[0])
                print(exercicio_atualizado.to_string())
                return exercicio_atualizado


    def excluir_exercicio(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        self.listar_exercicios
        codigo_exercicio = int(input("Codigo do exercicio a ser excluído: "))

        if not self.verifica_existencia_exercicio(oracle, codigo_exercicio):

            df_exercicio = oracle.sqlToDataFrame(f"select codigo_exercicio, nome_exercicio, repeticoes, grupo_muscular from exercicios where codigo_exercicio = {codigo_exercicio}")
            oracle.write(f"delete from exercicios where codigo_exercicio = {codigo_exercicio}")
            codigo_excluido = Exercicios(df_exercicio.codigo_exercicio.values[0], df_exercicio.repeticoes.values[0],df_exercicio.grupo_muscular.values[0],df_exercicio.nome_exercicio.values[0])
            print("Exercicio removido com sucesso!")
            print(codigo_excluido.to_string())
        else:
            print(f"O codigo {codigo_exercicio} não existe.")

    def verifica_existencia_exercicio(self,oracle: OracleQueries,codigo_exercicio: int = None) -> bool:
        df_exercicio = oracle.sqlToDataFrame(f"select codigo_exercicio, nome_exercicio from exercicios where codigo_exercicio = {codigo_exercicio} f")
        return df_exercicio.empty

    def listar_exercicios(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select e.codigo_exercicio
                    , e.nome_exercicio 
                from exercicios e
                order by e.nome_exercicio
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))