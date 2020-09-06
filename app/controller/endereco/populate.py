from app.controller import DAO
from app.controller.endereco import models, endereco_bp


def __endereco__():
    # PAISES
    brasil = DAO.buscar_por_criterio(models.Pais, tx_sigla='BR')
    alemanha = DAO.buscar_por_criterio(models.Pais, tx_sigla='DE')
    china = DAO.buscar_por_criterio(models.Pais, tx_sigla='CN')
    espanha = DAO.buscar_por_criterio(models.Pais, tx_sigla='ES')
    estados_unidos = DAO.buscar_por_criterio(models.Pais, tx_sigla='US')

    if not brasil:
        brasil = models.Pais('brasil', 'br')
        DAO.transacao(brasil)
    if not alemanha:
        alemanha = models.Pais('alemanha', 'de')
        DAO.transacao(alemanha)
    if not china:
        china = models.Pais('china', 'cn')
        DAO.transacao(china)
    if not espanha:
        espanha = models.Pais('espanha', 'es')
        DAO.transacao(espanha)
    if not estados_unidos:
        estados_unidos = models.Pais('estados unidos da america', 'us')
        DAO.transacao(estados_unidos)

    # ESTADOS
    bahia = DAO.buscar_por_criterio(models.Estado, tx_nome='BAHIA', tx_sigla='BA', fk_pais=brasil.pkey)
    para = DAO.buscar_por_criterio(models.Estado, tx_nome='PARA', tx_sigla='PA', fk_pais=brasil.pkey)
    texas = DAO.buscar_por_criterio(models.Estado, tx_nome='TEXAS', tx_sigla='TX', fk_pais=estados_unidos.pkey)
    baviera = DAO.buscar_por_criterio(models.Estado, tx_nome='BAVIERA', tx_sigla='BY', fk_pais=alemanha.pkey)
    guizhou = DAO.buscar_por_criterio(models.Estado, tx_nome='GUIZHOU', tx_sigla='GZ', fk_pais=china.pkey)

    if not bahia:
        bahia = models.Estado('bahia')
        bahia.tx_sigla = 'ba'
        bahia.pais = brasil
        DAO.transacao(bahia)
    if not para:
        para = models.Estado('para')
        para.tx_sigla = 'pa'
        para.pais = brasil
        DAO.transacao(para)
    if not texas:
        texas = models.Estado('texas')
        texas.tx_sigla = 'tx'
        texas.pais = estados_unidos
        DAO.transacao(texas)
    if not baviera:
        baviera = models.Estado('baviera')
        baviera.tx_sigla = 'by'
        baviera.pais = alemanha
        DAO.transacao(baviera)
    if not guizhou:
        guizhou = models.Estado('guizhou')
        guizhou.tx_sigla = 'gz'
        guizhou.pais = china
        DAO.transacao(china)

    # CIDADES
    belem = DAO.buscar_por_criterio(models.Cidade, tx_nome='BELEM', fk_estado=para.pkey)
    ananindeua = DAO.buscar_por_criterio(models.Cidade, tx_nome='ANANINDEUA', fk_estado=para.pkey)
    salvador = DAO.buscar_por_criterio(models.Cidade, tx_nome='SALVADOR', fk_estado=bahia.pkey)
    austin = DAO.buscar_por_criterio(models.Cidade, tx_nome='AUSTIN', fk_estado=texas.pkey)
    marituba = DAO.buscar_por_criterio(models.Cidade, tx_nome='MARITUBA', fk_estado=para.pkey)

    if not belem:
        belem = models.Cidade('belem')
        belem.estado = para
        DAO.transacao(belem)
    if not ananindeua:
        ananindeua = models.Cidade('ananindeua')
        ananindeua.estado = para
        DAO.transacao(ananindeua)
    if not salvador:
        salvador = models.Cidade('salvador')
        salvador.estado = bahia
        DAO.transacao(salvador)
    if not austin:
        austin = models.Cidade('austin')
        austin.estado = texas
        DAO.transacao(austin)
    if not marituba:
        marituba = models.Cidade('marituba')
        marituba.estado = para
        DAO.transacao(marituba)

    # BAIRROS
    aguas_brancas = DAO.buscar_por_criterio(models.Bairro, tx_nome='AGUAS BRANCAS', fk_cidade=ananindeua.pkey)
    montese = DAO.buscar_por_criterio(models.Bairro, tx_nome='MONTESE', fk_cidade=belem.pkey)
    canudos = DAO.buscar_por_criterio(models.Bairro, tx_nome='CANUDOS', fk_cidade=belem.pkey)
    levilandia = DAO.buscar_por_criterio(models.Bairro, tx_nome='LEVILANDIA', fk_cidade=ananindeua.pkey)
    parque_verde = DAO.buscar_por_criterio(models.Bairro, tx_nome='PARQUE VERDE', fk_cidade=marituba.pkey)

    if not aguas_brancas:
        aguas_brancas = models.Bairro('aguas brancas')
        aguas_brancas.cidade = ananindeua
        DAO.transacao(aguas_brancas)
    if not montese:
        montese = models.Bairro('montese')
        montese.cidade = belem
        DAO.transacao(montese)
    if not canudos:
        canudos = models.Bairro('canudos')
        canudos.cidade = belem
        DAO.transacao(canudos)
    if not levilandia:
        levilandia = models.Bairro('levilandia')
        levilandia.cidade = ananindeua
        DAO.transacao(levilandia)
    if not parque_verde:
        parque_verde = models.Bairro('parque verde')
        parque_verde.cidade = marituba
        DAO.transacao(parque_verde)

    # RUAS
    dois_de_junho_bel = DAO.buscar_por_criterio(models.Rua, tx_nome='DOIS DE JUNHO', tx_cep='66077150',
                                                fk_bairro=montese.pkey)
    dois_de_junho_an = DAO.buscar_por_criterio(models.Rua, tx_nome='DOIS DE JUNHO', tx_cep='67033060',
                                               fk_bairro=aguas_brancas.pkey)
    br316 = DAO.buscar_por_criterio(models.Rua, tx_nome='BR 316', tx_cep='67030010', fk_bairro=levilandia.pkey)

    if not dois_de_junho_bel:
        dois_de_junho_bel = models.Rua('dois de junho', '66077150')
        dois_de_junho_bel.bairro = montese
        DAO.transacao(dois_de_junho_bel)
    if not dois_de_junho_an:
        dois_de_junho_an = models.Rua('dois de junho', '67033060')
        dois_de_junho_an.bairro = aguas_brancas
        DAO.transacao(dois_de_junho_an)
    if not br316:
        br316 = models.Rua('BR 316', '67030010')
        br316.bairro = levilandia
        DAO.transacao(br316)

    # ENDERECOS
    lv_br = DAO.buscar_por_criterio(models.Endereco, tx_numero='S/N', tx_complemento='KM 6', fk_rua=br316.pkey)
    ddj = DAO.buscar_por_criterio(models.Endereco, tx_numero='650', fk_rua=dois_de_junho_an.pkey)
    ddj2 = DAO.buscar_por_criterio(models.Endereco, tx_numero='45', fk_rua=dois_de_junho_bel.pkey)

    if not lv_br:
        lv_br = models.Endereco()
        lv_br.tx_complemento = 'km 6'
        lv_br.rua = br316
        DAO.transacao(lv_br)
    if not ddj:
        ddj = models.Endereco()
        ddj.tx_numero = '650'
        ddj.rua = dois_de_junho_an
        DAO.transacao(ddj)
    if not ddj2:
        ddj2 = models.Endereco()
        ddj2.tx_numero = '45'
        ddj2.rua = dois_de_junho_bel
        DAO.transacao(ddj2)


@endereco_bp.before_app_first_request
def seed():
    __endereco__()
