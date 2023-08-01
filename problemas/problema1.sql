-- Criar tabela PACIENTE em stg_prontuario
DROP TABLE IF EXISTS stg_prontuario.paciente;

CREATE TABLE stg_prontuario.paciente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR,
    dt_nascimento DATE,
    cpf BIGINT,
    nome_mae VARCHAR,
    dt_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
