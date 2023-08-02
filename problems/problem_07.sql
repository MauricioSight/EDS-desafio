-- Criar tabela diagnostico e atendimento
DROP TABLE IF EXISTS diagnostico;
DROP TABLE IF EXISTS atendimento;

-- (I=Internação, U=Urgência e A=Ambulatório)
DROP TYPE IF EXISTS atendimento_tipo;
CREATE TYPE atendimento_tipo AS ENUM ('I', 'U', 'A');

-- Relação 1:N com Diagnostico
CREATE TABLE atendimento (
    id SERIAL PRIMARY KEY,
    tipo atendimento_tipo
);

-- Relação N:1 com Atendimento
CREATE TABLE diagnostico (
    id SERIAL PRIMARY KEY,
    atendimento_id INTEGER NOT NULL,
    CONSTRAINT fk_diagnostico
        FOREIGN KEY(atendimento_id) 
	    REFERENCES atendimento(id)
);
