-- CRIAR TABELAS

CREATE TABLE IF NOT EXISTS public.pais(
    pkey VARCHAR(36) PRIMARY KEY NOT NULL,
    tx_nome VARCHAR(80) NOT NULL,
    sigla VARCHAR(2) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.estado(
    pkey VARCHAR(36) PRIMARY KEY NOT NULL,
    tx_nome VARCHAR(80) NOT NULL,
    sigla VARCHAR(3) NOT NULL,
    fk_pais VARCHAR(36) NOT NULL,
    CONSTRAINT ak_estado UNIQUE (tx_nome, fk_pais)
);

CREATE TABLE IF NOT EXISTS public.cidade(
    pkey VARCHAR(36) PRIMARY KEY NOT NULL,
    tx_nome VARCHAR(80) NOT NULL,
    fk_estado VARCHAR(36) NOT NULL,
    CONSTRAINT ak_cidade UNIQUE (tx_nome, fk_estado)
);

CREATE TABLE IF NOT EXISTS public.bairro(
    pkey VARCHAR(36) PRIMARY KEY NOT NULL,
    tx_nome VARCHAR(80) NOT NULL,
    fk_cidade VARCHAR(36) NOT NULL,
    CONSTRAINT ak_bairro UNIQUE (tx_nome, fk_cidade)
);

CREATE TABLE IF NOT EXISTS public.rua(
    pkey VARCHAR(36) PRIMARY KEY NOT NULL,
    tx_nome VARCHAR(80) NOT NULL,
    tx_cep VARCHAR(10) NOT NULL,
    fk_bairro VARCHAR(36) NOT NULL,
    CONSTRAINT ak_rua UNIQUE (tx_nome, tx_cep, fk_bairro)
);

CREATE TABLE IF NOT EXISTS public.endereco(
    pkey VARCHAR(36) PRIMARY KEY NOT NULL,
    tx_numero VARCHAR(8),
    tx_complemento TEXT,
    fk_rua VARCHAR(36) NOT NULL,
    CONSTRAINT ak_endereco UNIQUE (tx_numero, fk_rua)
);

-- FKs

ALTER TABLE public.estado
ADD CONSTRAINT FK_estado_pais FOREIGN KEY (fk_pais)
REFERENCES public.pais(pkey)
ON UPDATE NO ACTION
ON DELETE NO ACTION
;

ALTER TABLE public.cidade
ADD CONSTRAINT FK_cidade_estado FOREIGN KEY (fk_estado)
REFERENCES public.estado(pkey)
ON UPDATE NO ACTION
ON DELETE NO ACTION
;

ALTER TABLE public.bairro
ADD CONSTRAINT FK_bairro_cidade FOREIGN KEY (fk_cidade)
REFERENCES public.cidade(pkey)
ON UPDATE NO ACTION
ON DELETE NO ACTION
;

ALTER TABLE public.rua
ADD CONSTRAINT FK_rua_bairro FOREIGN KEY (fk_bairro)
REFERENCES public.bairro(pkey)
ON UPDATE NO ACTION
ON DELETE NO ACTION
;

ALTER TABLE public.endereco
ADD CONSTRAINT FK_endereco_rua FOREIGN KEY (fk_rua)
REFERENCES public.rua(pkey)
ON UPDATE NO ACTION
ON DELETE NO ACTION
;
