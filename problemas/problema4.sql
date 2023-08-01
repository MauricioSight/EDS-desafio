-- Pacientes duplicados mais recentes
SELECT prontuario.*
FROM stg_prontuario.paciente prontuario
    INNER JOIN (
        SELECT cpf, MAX(dt_atualizacao) dt_atualizacao
        FROM stg_prontuario.paciente 
        GROUP BY cpf
        HAVING count(cpf) > 1
    ) duplicatas
    ON prontuario.cpf = duplicatas.cpf
WHERE prontuario.dt_atualizacao = duplicatas.dt_atualizacao;
