SELECT A.NOME_ALUNO, E.GRUPO_MUSCULAR, COUNT(*) AS ALUNOS
FROM ALUNOS A
INNER JOIN EXERCICIOS E ON E.CODIGO_EXERCICIO = A.CODIGO_EXERCICIO
GROUP BY A.NOME_ALUNO, E.GRUPO_MUSCULAR;