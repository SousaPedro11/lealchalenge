from flask import render_template, request, flash, redirect, url_for

from app.controller import DAO
from app.controller.endereco import endereco_bp
from app.controller.endereco.models import Pais, Estado, Cidade, Bairro, Rua, Endereco


@endereco_bp.route('/endereco/', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def home():
    return render_template('endereco_home.html')


@endereco_bp.route('/database/')
def database():
    with open('app/sql/DDL.sql') as f:
        ddl = '\n'.join([i.replace('\n', '') for i in f.readlines()])
    with open('app/sql/DML.sql') as f:
        dml = '\n'.join([i.replace('\n', '') for i in f.readlines()])
    with open('app/sql/DQL.sql') as f:
        dql = '\n'.join([i.replace('\n', '') for i in f.readlines()])

    return render_template('sql.html', ddl=ddl, dml=dml, dql=dql)


@endereco_bp.route('/endereco/cadastrar/<objeto>/', methods=['GET', 'POST'])
def cadastro(objeto, tabela=None, tabela2=None):
    if objeto == 'pais':
        tabela = DAO.buscar_todos(Pais, Pais.tx_nome, Pais.tx_sigla)
    elif objeto == 'estado':
        tabela = DAO.buscar_todos_por_join(Estado, Pais, Pais.tx_nome, Estado.tx_nome, Estado.tx_sigla,
                                           Estado.fk_pais == Pais.pkey)
    elif objeto == 'cidade':
        tabela = DAO.buscar_todos_por_join(Cidade, Estado, Estado.tx_nome, Cidade.tx_nome,
                                           Cidade.fk_estado == Estado.pkey)
    elif objeto == 'bairro':
        tabela = DAO.buscar_todos_por_join(Bairro, Cidade, Cidade.tx_nome, Bairro.tx_nome,
                                           Bairro.fk_cidade == Cidade.pkey)
    elif objeto == 'rua':
        tabela = DAO.buscar_todos_por_join(Rua, Bairro, Bairro.tx_nome, Rua.tx_nome, Rua.tx_cep,
                                           Rua.fk_bairro == Bairro.pkey)
    elif objeto == 'endereco':
        tabela = DAO.buscar_todos_por_join(Endereco, Rua, Rua.tx_nome, Endereco.tx_numero,
                                           Endereco.fk_rua == Rua.pkey)

    if not (len(tabela) > 0):
        if objeto == 'pais':
            tabela2 = Pais('', '')
        elif objeto == 'estado':
            tabela2 = Estado('')
        elif objeto == 'cidade':
            tabela2 = Cidade('')
        elif objeto == 'bairro':
            tabela2 = Bairro('')
        elif objeto == 'rua':
            tabela2 = Rua('', '')
        elif objeto == 'endereco':
            tabela2 = Endereco()
    return render_template('endereco_cadastro.html', objeto=objeto, table=tabela, tabela2=tabela2)


@endereco_bp.route('/endereco/editar/<objeto>/<id>/', methods=['GET', 'POST'])
def editar(objeto, id):
    string = objeto.capitalize()
    registro = DAO.buscar_por_criterio(globals()[string], pkey=id)
    registro_pai = None
    for r in registro.__dict_class__:
        for k, v in r.items():
            if '__dict__' in dir(v):
                registro_pai = DAO.buscar_todos(globals()[v.__class__.__name__])

    hold = hash(frozenset(vars(registro).items()))
    if request.method == 'POST':
        for x in registro.dict_fieldname:
            attr = registro.dict_fieldname[x]
            attr_val = request.form[x]
            setattr(registro, attr, attr_val)
        hregistro = hash(frozenset(vars(registro).items()))
        if hold == hregistro:
            flash('Sem alterações')
        else:
            DAO.transacao(registro)
            flash('Alterações efetuadas com sucesso!')
        return redirect(url_for('endereco_bp.cadastro', objeto=objeto))
    return render_template('endereco_editar.html', registro=registro, registro_pai=registro_pai, objeto=objeto)


@endereco_bp.route('/endereco/deletar/<objeto>/<id>/', methods=['GET', 'POST'])
def deletar(objeto, id):
    string = objeto.capitalize()
    registro = DAO.buscar_por_criterio(globals()[string], pkey=id)
    has_child = False
    for v in registro.__mapper__.relationships.values():
        if v.back_populates == objeto:
            has_child = len(getattr(registro, v.key)) > 0
    if has_child:
        flash(f'{registro} possui dependentes. Não pode ser excluído!')
        return redirect(url_for('endereco_bp.cadastro', objeto=objeto))
    else:
        if request.method == 'POST':
            DAO.deletar(registro)
            flash(f'{registro} removido com sucesso!')
            return redirect(url_for('endereco_bp.cadastro', objeto=objeto))
    return render_template('endereco_deletar.html', registro=registro, objeto=objeto)
