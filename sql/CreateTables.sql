CREATE TABLE Exercicios (
                Codigo_Exercicio NUMBER NOT NULL,
                Repeticoes NUMBER NOT NULL,
                Nome_Exercicio VARCHAR2(100) NOT NULL,
                Grupo_Muscular CHAR NOT NULL,
                CONSTRAINT EXERCICIOS_PK PRIMARY KEY (Codigo_Exercicio)
);


CREATE TABLE Alunos (
                Cpf VARCHAR2(11) NOT NULL,
                Codigo_Exercicio NUMBER NOT NULL,
                Nome_Aluno VARCHAR2(100) NOT NULL,
                Pagamento NUMBER(1) NOT NULL,
                Vencimento_Mensalidade DATE NOT NULL,
                Telefone NUMBER NOT NULL,
                CONSTRAINT ALUNOS_PK PRIMARY KEY (Cpf)
);


ALTER TABLE Alunos ADD CONSTRAINT EXERCICIOS_ALUNOS_FK
FOREIGN KEY (Codigo_Exercicio)
REFERENCES Exercicios (Codigo_Exercicio)
NOT DEFERRABLE;

CREATE SEQUENCE EXERCICIOS_CODIGO_EXERCICIO_SEQ;