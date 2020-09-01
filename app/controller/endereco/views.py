from flask import render_template

from app.controller.endereco import endereco_bp


@endereco_bp.route('/enderecos/', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def enderecos():
    pass


@endereco_bp.route('/database/')
def database():
    with open('app/sql/DDL.sql') as f:
        ddl = '\n'.join([i.replace('\n', '') for i in f.readlines()])
    with open('app/sql/DML.sql') as f:
        dml = '\n'.join([i.replace('\n', '') for i in f.readlines()])

    return render_template('sql.html', ddl=ddl, dml=dml, dql='dql')
