-- Popular stg_prontuario com os dados em stg_hospital_a, stg_hospital_b e stg_hospital_c
INSERT INTO stg_prontuario.paciente (nome, dt_nascimento, cpf, nome_mae, dt_atualizacao)
SELECT nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM stg_hospital_a.paciente
UNION
SELECT nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM stg_hospital_b.paciente
UNION
SELECT nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM stg_hospital_c.paciente;
