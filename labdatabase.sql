select count(1) as total_alunos from alunos;

select count(1) as total_exercicios from exercicios;

select e.codigo_exercicio
     , e.nome_exercicio 
  from exercicios e
 order by e.nome_exercicio;
 
drop table alunos;
drop table exercicios;
drop sequence codigo_exercicios_seq;