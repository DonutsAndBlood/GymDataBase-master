SELECT  E.GRUPO_MUSCULAR, E.NOME_EXERCICIO, E.REPETICOES FROM EXERCICIOS E
INNER JOIN ALUNOS A ON E.CODIGO_EXERCICIO = A.CODIGO_EXERCICIO
WHERE GRUPO_MUSCULAR = :GRUPO_MUSCULAR
AND ROWNUM < 8
ORDER BY DBMS_RANDOM.VALUE