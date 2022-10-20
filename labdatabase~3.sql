select codigo_exercicio, nome_exercicio, repeticoes, grupo_muscular from exercicios where nome_exercicio = 'polichinelo';

select cpf, nome_aluno, telefone, pagamento, vencimento_mensalidade, alunos_exercicios from alunos where cpf = '167.636.337-85';

select e.codigo_exercicio
                    , e.nome_exercicio 
                from exercicios e
                order by e.nome_exercicio;
select cpf, nome_aluno, telefone, pagamento, vencimento_mensalidade, alunos_exercicios from alunos where cpf = '167.636.337-85';