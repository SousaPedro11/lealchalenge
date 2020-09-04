SELECT b.tx_nome from public.bairro b
INNER JOIN public.cidade c ON c.pkey = b.fk_cidade AND c.tx_nome ILIKE 'belem'
INNER JOIN public.estado e ON e.pkey = c.fk_estado AND e.tx_nome ILIKE 'para'
INNER JOIN public.pais p ON p.pkey = e.fk_pais AND p.tx_nome ILIKE 'brasil'
;