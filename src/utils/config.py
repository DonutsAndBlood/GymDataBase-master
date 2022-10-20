MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Alunos
2 - Relatório de Exercicios
3 - Relatório de ALunos por tipo de Grupo muscular
4 - Gerar ficha de exercicio diária
5 - Relatório de alunos Inadimplentes
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - ALunos
2 - Exercicios
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