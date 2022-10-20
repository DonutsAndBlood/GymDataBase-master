from distutils.file_util import copy_file
from model.alunos import Alunos
from conexion.oracle_queries import OracleQueries


class Controller_Alunos:
    def __init__(self):
        pass

    def cadastrar_aluno(self) -> Alunos:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("Digite o numero de cpf: ")

        if self.verifica_existencia_aluno(oracle, cpf):
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            pagamento = input("Pagamento (A para adimplente e I para inadimplente): ")
            vencimento_mensalidade = input("Dia de vencimento da mensalidade: ")

            oracle.write(f"insert into alunos values ('{cpf}', '{nome}', '{pagamento}',{vencimento_mensalidade}, null ,{telefone})")

            df_aluno = oracle.sqlToDataFrame(
                f"select cpf, alunos_exercicios, nome_aluno, telefone, pagamento, vencimento_mensalidade from alunos where cpf = '{cpf}'")


##INSERT INTO ALUNOS VALUES ('167.636.337.89','BRAYAN BAUT','i',13,null,27997863543);

            nome = df_aluno.nome_aluno.values[0]
            cpf = df_aluno.cpf.values[0]
            pagamento = df_aluno.pagamento.values[0]
            vencimento = df_aluno.vencimento_mensalidade.values[0]
            telefone = df_aluno.telefone.values[0]
            exercicio = df_aluno.alunos_exercicios.values[0]

            novo_aluno = Alunos(nome,cpf,pagamento,vencimento,telefone,exercicio)
            print(novo_aluno.to_string())
            return novo_aluno
        else:
            print(f"O CPF {cpf} não existe.")
            return None
    
    def atualizar_alunos(self):
        oracle = OracleQueries(can_write= True)
        oracle.connect()

        cpf = int(input("Insira o CPF do cliente a ser alterado"))

        if not self.verifica_existencia_aluno(oracle, cpf):
            print("1 - Nome\n 2 - Telefone")
            aux = int(input("Insira qual atributo irá ser alterado"))      
            if aux == 1:
                novo_nome = input("Insira o novo nome: ")
                oracle.write(f"update alunos set nome_aluno = '{novo_nome}' where cpf = {cpf}")
                df_aluno = oracle.sqlToDataFrame(f"Select cpf, nome_aluno, pagamento, vencimento_mensalidade, telefone from alunos where cpf = {cpf}")
                aluno_atualizado = Alunos(df_aluno.nome_aluno.values[0], df_aluno.cpf.values[0],df_aluno.pagamento.values[0], df_aluno.vencimento_mensalidade.values[0],df_aluno.telefone.values[0])
                print(aluno_atualizado.to_string())
                return aluno_atualizado
            elif aux == 2:
                while True:
                    novo_telefone = input("Insira o novo telefone: ")
                    if (len(str(novo_telefone))) > 11:
                        print("Telefone inválido")
                    else:
                         oracle.write(f"update alunos set telefone = '{novo_telefone}' where cpf = {cpf}")
                         df_aluno = oracle.sqlToDataFrame(f"Select cpf, nome_aluno, pagamento, vencimento_mensalidade, telefone from alunos where cpf = {cpf}")
                         aluno_atualizado = Alunos(df_aluno.nome_aluno.values[0], df_aluno.cpf.values[0],df_aluno.pagamento.values[0], df_aluno.vencimento_mensalidade.values[0],df_aluno.telefone.values[0])
                         print(aluno_atualizado.to_string())
                         return aluno_atualizado

    def excluir_aluno(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        self.listar_alunos(oracle, need_connect=True)
        cpf = input("CPF do aluno a ser excluído: ")

        if not self.verifica_existencia_aluno(oracle, cpf):
            df_aluno = oracle.sqlToDataFrame(f"select cpf, nome_aluno, telefone, pagamento, vencimento_mensalidade, alunos_exercicios from alunos where cpf = '{cpf}'")
            oracle.write(f"delete from alunos where cpf = '{cpf}'")

            nome = df_aluno.nome_aluno.values[0]
            cpf = df_aluno.cpf.values[0]
            pagamento = df_aluno.pagamento.values[0]
            vencimento = df_aluno.vencimento_mensalidade.values[0]
            telefone = df_aluno.telefone.values[0]
            exercicio = df_aluno.alunos_exercicios.values[0]

            aluno_excluido = Alunos(nome,cpf,pagamento,vencimento,telefone,exercicio)
            print("Aluno removido com sucesso!")
            print(aluno_excluido.to_string())
        else:
            print(f"O CPF {cpf} não existe.")

    def verifica_existencia_aluno(self,oracle: OracleQueries,cpf: str = None) -> bool:
        df_aluno = oracle.sqlToDataFrame(f"select cpf, nome_aluno, telefone, pagamento, vencimento_mensalidade, alunos_exercicios from alunos where cpf = '{cpf}'")
        return df_aluno.empty


    def listar_alunos(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select a.cpf
                    , a.nome_aluno 
                from alunos a
                order by a.nome_aluno
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))