INSERT INTO public.pais(pkey, tx_nome, sigla) VALUES
('d07582f5-e2ab-4e00-b1fc-9718e6da20c8', 'ALEMANHA', 'DE'),
('df6c7751-d664-4669-8cbb-c9b4e82f5f34', 'CHINA', 'CN'),
('d79771ed-8ff9-4451-abc5-85310b25b4a4', 'ESPANHA', 'ES'),
('971bd72c-4770-4018-ad9e-d0115e59a805', 'ESTADOS UNIDOS DA AMERICA', 'US'),
('26ecf951-749f-458d-8a0b-e8b0fd40fdd4', 'BRASIL', 'BR')
;

INSERT INTO public.estado(pkey, tx_nome, sigla, fk_pais) VALUES
('a0164ffa-1ade-4c66-9bff-b17b480612b8', 'BAHIA', 'BA', '26ecf951-749f-458d-8a0b-e8b0fd40fdd4'),
('089a30b2-50e3-4e71-90f5-88259c78defb', 'PARA', 'PA', '26ecf951-749f-458d-8a0b-e8b0fd40fdd4'),
('4f0bbc8b-5397-40c8-8434-85c3856ce2e9', 'TEXAS', 'TX', '971bd72c-4770-4018-ad9e-d0115e59a805'),
('5d43e95b-e078-4ab1-b63a-c7aaac7cb84c', 'BAVIERA', 'BY', 'd07582f5-e2ab-4e00-b1fc-9718e6da20c8'),
('d2c41ef5-db7c-4230-b18d-507e360e3ec8', 'GUIZHOU', 'GZ', 'df6c7751-d664-4669-8cbb-c9b4e82f5f34')
;