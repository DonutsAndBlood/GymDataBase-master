MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Carregar templates
6 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Alunos
2 - Relatório de Exercicios
3 - Relatório de Exercicios Favoritos
4 - Relatório de Alunos Inadimplentes
0 - Sair
"""

MENU_ENTIDADES = """Escolha a entidade
1 - Alunos
2 - Exercicio
"""

QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=5):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")