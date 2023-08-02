-- Pacientes duplicados
SELECT * 
FROM stg_prontuario.paciente
WHERE cpf in (
    SELECT cpf
    FROM stg_prontuario.paciente 
    GROUP BY cpf
    HAVING count(cpf) > 1
);
