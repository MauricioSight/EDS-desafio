-- POPULATE CONTEXT

INSERT INTO stg_hospital_a.paciente (nome, dt_nascimento, cpf, nome_mae)
VALUES ('José A', '2000-05-04', '07354536487', 'Maria');

INSERT INTO stg_hospital_a.paciente (nome, dt_nascimento, cpf, nome_mae)
VALUES ('Maria A', '2000-08-20', '07354566407', 'Roberta');

INSERT INTO stg_hospital_b.paciente (nome, dt_nascimento, cpf, nome_mae)
VALUES ('José B', '2000-05-04', '07354536487', 'Maria');

INSERT INTO stg_hospital_b.paciente (nome, dt_nascimento, cpf, nome_mae)
VALUES ('José B', '2000-05-04', '07354536687', 'Ana');

INSERT INTO stg_hospital_b.paciente (nome, dt_nascimento, cpf, nome_mae)
VALUES ('Maria B', '2000-08-20', '07354566407', 'Roberta');

INSERT INTO stg_hospital_c.paciente (nome, dt_nascimento, cpf, nome_mae)
VALUES ('José C', '2000-05-04', '07354556407', 'Jessica');

INSERT INTO stg_hospital_c.paciente (nome, dt_nascimento, cpf, nome_mae)
VALUES ('Maria C', '2000-08-20', '07354566407', 'Roberta');

INSERT INTO stg_hospital_c.paciente (nome, dt_nascimento, cpf, nome_mae)
VALUES ('Maria C Update 2', '2000-08-20', '07354566407', 'Roberta');

INSERT INTO stg_hospital_b.paciente (nome, dt_nascimento, cpf, nome_mae)
VALUES ('Maria B Update 2', '2000-08-20', '07354566407', 'Roberta');

INSERT INTO stg_hospital_a.paciente (nome, dt_nascimento, cpf, nome_mae)
VALUES ('José A Update 2', '2000-05-04', '07354536487', 'Maria');
