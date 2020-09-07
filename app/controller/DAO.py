from flask_sqlalchemy import SQLAlchemy

root_db = SQLAlchemy(session_options={'autoflush': False})


def transacao(objeto):
    local_object = root_db.session.merge(objeto)
    root_db.session.add(local_object)
    root_db.session.commit()
    root_db.session.close()


def buscar_por_criterio(table, **filtros):
    return table.query.filter_by(**filtros).first()


def buscar_por_criterio_bool(table, *filtros):
    return table.query.filter(*filtros).first()


def busca_join_composto_com_criterio(table1, table2, table3, *filtro):
    return table1.query.join(table2).join(table3).filter(*filtro).add_entity(table2).add_entity(table3).first()


def buscar_por_join(table1, table2, *filtro):
    return table1.query.join(table2).filter(*filtro).add_entity(table2).first()


def buscar_todos(table, *order_by):
    return table.query.order_by(*order_by).all()


def buscar_todos_por_criterio(table, **filtros):
    return table.query.filter_by(**filtros).all()


# tabela = Estado.query.join(Pais).filter(Estado.fk_pais == Pais.pkey).order_by(Pais.tx_nome, Estado.tx_nome,
#                                                                               Estado.tx_sigla).all()
def buscar_todos_por_join(table1, table2, *order_by, **filtro):
    return table1.query.join(table2).filter(**filtro).order_by(*order_by).all()


def deletar(objeto):
    root_db.session.delete(objeto)
    root_db.session.commit()
    root_db.session.close()
