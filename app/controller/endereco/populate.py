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
    belem = DAO.buscar_por_criterio(models.Cidade, tx_nome='belem')
    ananindeua = DAO.buscar_por_criterio(models.Cidade, tx_nome='ananindeua')
    salvador = DAO.buscar_por_criterio(models.Cidade, tx_nome='salvador')
    austin = DAO.buscar_por_criterio(models.Cidade, tx_nome='austin')
    marituba = DAO.buscar_por_criterio(models.Cidade, tx_nome='marituba')

    # BAIRROS
    aguas_brancas = DAO.buscar_por_criterio(models.Bairro, tx_nome='aguas brancas')
    montese = DAO.buscar_por_criterio(models.Bairro, tx_nome='montese')
    canudos = DAO.buscar_por_criterio(models.Bairro, tx_nome='canudos')
    levilandia = DAO.buscar_por_criterio(models.Bairro, tx_nome='levilandia')
    parque_verde = DAO.buscar_por_criterio(models.Bairro, tx_nome='parque verde')

    # RUAS
    dois_de_junho = DAO.buscar_por_criterio(models.Rua, tx_nome='dois de junho', tx_cep='66077150')
    dois_de_junho_2 = DAO.buscar_por_criterio(models.Rua, tx_nome='dois de junho', tx_cep='67033060')
    br316 = DAO.buscar_por_criterio(models.Rua, tx_nome='br 316', tx_cep='67030010')

    # ENDERECOS
    lv_br = DAO.buscar_por_criterio(models.Endereco, tx_numero='S/N', tx_complemento='KM 6')
    ddj = DAO.buscar_por_criterio(models.Endereco, tx_numero='650')
    ddj2 = DAO.buscar_por_criterio(models.Endereco, tx_numero='45')


@endereco_bp.before_app_first_request
def seed():
    __endereco__()
