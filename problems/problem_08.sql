-- Média da quantidade de diagnósticos dos atendimento do tipo 'U'
SELECT AVG(atd.dtg_count)
FROM (
    SELECT atd.id, COUNT(*) dtg_count
    FROM atendimento atd
        LEFT OUTER JOIN diagnostico dtg
        ON atd.id = dtg.atendimento_id
    WHERE atd.tipo = 'U'
    GROUP BY atd.id
) AS atd;
