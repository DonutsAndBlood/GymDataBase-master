CREATE TABLE Exercicios (
                Codigo_Exercicio NUMBER NOT NULL,
                Repeticoes NUMBER NOT NULL,
                Nome_Exercicio VARCHAR2 NOT NULL,
                Grupo_Muscular CHAR NOT NULL,
                CONSTRAINT EXERCICIOS_PK PRIMARY KEY (Codigo_Exercicio)
);


CREATE TABLE Alunos (
                Cpf VARCHAR2 NOT NULL,
                Codigo_Exercicio NUMBER NOT NULL,
                Nome_Aluno VARCHAR2 NOT NULL,
                Pagamento NUMBER NOT NULL,
                Vencimento_Mensalidade DATE NOT NULL,
                Telefone NUMBER NOT NULL,
                CONSTRAINT CODIGO_ALUNO PRIMARY KEY (Cpf)
);


ALTER TABLE Alunos ADD CONSTRAINT EXERCICIOS_ALUNOS_FK
FOREIGN KEY (Codigo_Exercicio)
REFERENCES Exercicios (Codigo_Exercicio)
NOT DEFERRABLE;

CREATE SEQUENCE ALUNOS_CODIGO_ALUNO_SEQ;
