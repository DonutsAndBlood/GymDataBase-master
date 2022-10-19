CREATE TABLE Exercicios (
                Codigo_Exercicio NUMBER NOT NULL,
                Repeticoes NUMBER NOT NULL,
                Nome_Exercicio VARCHAR2(100) NOT NULL,
                Grupo_Muscular CHAR(1) NOT NULL,
                CONSTRAINT EXERCICIOS_PK PRIMARY KEY (Codigo_Exercicio)
);


CREATE TABLE Alunos (
                Cpf VARCHAR2(15) NOT NULL,
                Nome_Aluno VARCHAR2(100) NOT NULL,
                Pagamento CHAR NOT NULL,
                Vencimento_Mensalidade DATE NOT NULL,
                Alunos_Exercicios NUMBER(3),
                Telefone NUMBER(11) NOT NULL,
                CONSTRAINT CODIGO_ALUNO PRIMARY KEY (Cpf)
);

ALTER TABLE Alunos ADD CONSTRAINT EXERCICIOS_ALUNOS_FK
FOREIGN KEY (alunos_exercicios)
REFERENCES Exercicios (Codigo_Exercicio)
NOT DEFERRABLE;

CREATE SEQUENCE CODIGO_EXERCICIOS_SEQ;

COMMIT;
