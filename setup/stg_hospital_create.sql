-- Schemas
CREATE SCHEMA IF NOT EXISTS stg_hospital_a;
CREATE SCHEMA IF NOT EXISTS stg_hospital_b;
CREATE SCHEMA IF NOT EXISTS stg_hospital_c;

CREATE SCHEMA IF NOT EXISTS stg_prontuario;

-- Tables
DROP TABLE IF EXISTS stg_hospital_a.paciente;
DROP TABLE IF EXISTS stg_hospital_b.paciente;
DROP TABLE IF EXISTS stg_hospital_c.paciente;

CREATE TABLE stg_hospital_a.paciente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR,
    dt_nascimento DATE,
    cpf BIGINT,
    nome_mae VARCHAR,
    dt_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stg_hospital_b.paciente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR,
    dt_nascimento DATE,
    cpf BIGINT,
    nome_mae VARCHAR,
    dt_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stg_hospital_c.paciente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR,
    dt_nascimento DATE,
    cpf BIGINT,
    nome_mae VARCHAR,
    dt_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
