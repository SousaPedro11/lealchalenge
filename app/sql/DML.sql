INSERT INTO public.pais(pkey, tx_nome, tx_sigla) VALUES
('d07582f5-e2ab-4e00-b1fc-9718e6da20c8', 'ALEMANHA', 'DE'),
('df6c7751-d664-4669-8cbb-c9b4e82f5f34', 'CHINA', 'CN'),
('d79771ed-8ff9-4451-abc5-85310b25b4a4', 'ESPANHA', 'ES'),
('971bd72c-4770-4018-ad9e-d0115e59a805', 'ESTADOS UNIDOS DA AMERICA', 'US'),
('26ecf951-749f-458d-8a0b-e8b0fd40fdd4', 'BRASIL', 'BR')
;

INSERT INTO public.estado(pkey, tx_nome, tx_sigla, fk_pais) VALUES
('a0164ffa-1ade-4c66-9bff-b17b480612b8', 'BAHIA', 'BA', '26ecf951-749f-458d-8a0b-e8b0fd40fdd4'),
('089a30b2-50e3-4e71-90f5-88259c78defb', 'PARA', 'PA', '26ecf951-749f-458d-8a0b-e8b0fd40fdd4'),
('4f0bbc8b-5397-40c8-8434-85c3856ce2e9', 'TEXAS', 'TX', '971bd72c-4770-4018-ad9e-d0115e59a805'),
('5d43e95b-e078-4ab1-b63a-c7aaac7cb84c', 'BAVIERA', 'BY', 'd07582f5-e2ab-4e00-b1fc-9718e6da20c8'),
('d2c41ef5-db7c-4230-b18d-507e360e3ec8', 'GUIZHOU', 'GZ', 'df6c7751-d664-4669-8cbb-c9b4e82f5f34')
;

INSERT INTO public.cidade(pkey, tx_nome, fk_estado) VALUES
('25d38bd9-e1cc-4543-9756-44083fb9022d', 'BELEM', '089a30b2-50e3-4e71-90f5-88259c78defb'),
('2aa190bc-16c6-4fe1-9c4f-e4f91e9ef442', 'ANANINDEUA', '089a30b2-50e3-4e71-90f5-88259c78defb'),
('4e86f926-50f1-4404-a033-3f2e29b45d1b', 'SALVADOR', 'a0164ffa-1ade-4c66-9bff-b17b480612b8'),
('d1a35fbc-148a-41d0-8ef1-ae8cc3d636fe', 'AUSTIN', '4f0bbc8b-5397-40c8-8434-85c3856ce2e9'),
('f6e06d73-8dc1-4e05-80d3-fcc025cfba9d', 'MARITUBA', '089a30b2-50e3-4e71-90f5-88259c78defb')
;

INSERT INTO public.bairro(pkey, tx_nome, fk_cidade) VALUES
('bad2952b-edc5-4865-8490-848136d02b5f', 'AGUAS BRANCAS', '2aa190bc-16c6-4fe1-9c4f-e4f91e9ef442'),
('752e76cd-e7e9-4c3d-9530-e2c9f382e9fd', 'MOSTESE', '25d38bd9-e1cc-4543-9756-44083fb9022d'),
('40946fd2-b3f2-480f-a292-aef99de9f66c', 'CANUDOS', '25d38bd9-e1cc-4543-9756-44083fb9022d'),
('4a90efab-39cf-4322-9f6d-15a1b661d507', 'PARQUE VERDE', 'f6e06d73-8dc1-4e05-80d3-fcc025cfba9d'),
('74a8f007-2c17-4d4a-bf3f-c64c1994298f', 'LEVILANDIA', '2aa190bc-16c6-4fe1-9c4f-e4f91e9ef442')
;

INSERT INTO public.rua(pkey, tx_nome, tx_cep, fk_bairro) VALUES
('8ffc3a88-99cf-4d81-8ada-89c35a7b0769', 'DOIS DE JUNHO', '66077150', '752e76cd-e7e9-4c3d-9530-e2c9f382e9fd'),
('cab7545f-625d-4473-afa1-9aeba46a406a', 'DOIS DE JUNHO', '67033060', 'bad2952b-edc5-4865-8490-848136d02b5f'),
('aeb03145-10c7-4bb1-89ff-9aca9dd3e008', 'BR 316', '67030010', '74a8f007-2c17-4d4a-bf3f-c64c1994298f')
;

INSERT INTO public.endereco(pkey, tx_numero, tx_complemento, fk_rua) VALUES
('e56a0144-a9ee-4e1c-a16f-76f4e5b770e8', 'S/N', 'KM 6', 'aeb03145-10c7-4bb1-89ff-9aca9dd3e008'),
('76ba4d99-0c67-44af-8710-5529ba2eb5a6', '650', '', 'cab7545f-625d-4473-afa1-9aeba46a406a'),
('08682890-4c3a-4255-967b-e8e77659b8cf', '45', '', '8ffc3a88-99cf-4d81-8ada-89c35a7b0769')
;
