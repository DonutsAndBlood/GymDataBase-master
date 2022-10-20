SELECT NOME_ALUNO FROM ALUNOS
WHERE upper(pagamento) LIKE UPPER('%i%')
group by nome_aluno