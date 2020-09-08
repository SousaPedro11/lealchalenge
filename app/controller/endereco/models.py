from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import backref, validates

from app.controller import Util, DAO
from app.controller.endereco import db


class Pais(db.Model):
    __tablename__ = 'pais'

    pkey = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
    tx_nome = db.Column(db.VARCHAR(80), nullable=False)
    tx_sigla = db.Column(db.VARCHAR(2), nullable=True, unique=True)

    def __init__(self, tx_nome, tx_sigla):
        self.pkey = Util.__generate_id__()
        self.tx_nome = tx_nome
        self.tx_sigla = tx_sigla

    @validates('tx_nome', 'tx_sigla')
    def convert_upper(self, key, value):
        return value.upper()

    @property
    def __dict_class__(self):
        return [
            {'Nome': self.tx_nome},
            {'Sigla': self.tx_sigla}
        ]

    @property
    def dict_fieldname(self):
        return {'Nome': 'tx_nome', 'Sigla': 'tx_sigla'}

    def __repr__(self):
        return f'{self.tx_nome} - {self.tx_sigla}'


class Estado(db.Model):
    __tablename__ = 'estado'

    pkey = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
    tx_nome = db.Column(db.VARCHAR(80), nullable=False)
    tx_sigla = db.Column(db.VARCHAR(3), nullable=True)
    fk_pais = db.Column(db.VARCHAR(36), db.ForeignKey('pais.pkey', name='FK_estado_pais'), nullable=False)

    def __init__(self, tx_nome):
        self.pkey = Util.__generate_id__()
        self.tx_nome = tx_nome

    # Relationship
    # Many to one
    pais = db.relationship('Pais', backref=backref('estados', lazy='select'), cascade_backrefs=False)

    __table_args__ = (
        UniqueConstraint('tx_nome', 'fk_pais', name='ak_estado'),
    )

    @validates('tx_nome', 'tx_sigla')
    def convert_upper(self, key, value):
        return value.upper()

    @property
    def __dict_class__(self):
        return [
            {'Nome': self.tx_nome},
            {'Sigla': self.tx_sigla},
            {'Pais': DAO.buscar_por_criterio(Pais, pkey=self.fk_pais)}
        ]

    @property
    def dict_fieldname(self):
        return {'Nome': 'tx_nome', 'Sigla': 'tx_sigla', 'Pais': 'fk_pais'}

    def __repr__(self):
        return f'{self.tx_nome} - {self.tx_sigla}'


class Cidade(db.Model):
    __tablename__ = 'cidade'

    pkey = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
    tx_nome = db.Column(db.VARCHAR(80), nullable=False)
    fk_estado = db.Column(db.VARCHAR(36), db.ForeignKey('estado.pkey', name='FK_cidade_estado'), nullable=False)

    def __init__(self, tx_nome):
        self.pkey = Util.__generate_id__()
        self.tx_nome = tx_nome

    # Relationship
    # Many to one
    estado = db.relationship('Estado', backref=backref('cidades', lazy='select'), cascade_backrefs=False)

    __table_args__ = (
        UniqueConstraint('tx_nome', 'fk_estado', name='ak_cidade'),
    )

    @validates('tx_nome')
    def convert_upper(self, key, value):
        return value.upper()

    @property
    def __dict_class__(self):
        return [
            {'Nome': self.tx_nome},
            {'Estado': DAO.buscar_por_criterio(Estado, pkey=self.fk_estado)}
        ]

    @property
    def dict_fieldname(self):
        return {'Nome': 'tx_nome', 'Estado': 'fk_estado'}

    def __repr__(self):
        return f'{self.tx_nome} - {self.estado.tx_sigla}'


class Bairro(db.Model):
    __tablename__ = 'bairro'

    pkey = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
    tx_nome = db.Column(db.VARCHAR(80), nullable=False)
    fk_cidade = db.Column(db.VARCHAR(36), db.ForeignKey('cidade.pkey', name='FK_bairro_cidade'), nullable=False)

    def __init__(self, tx_nome):
        self.pkey = Util.__generate_id__()
        self.tx_nome = tx_nome

    # Relationship
    # Many to one
    cidade = db.relationship('Cidade', backref=backref('bairros', lazy='select'), cascade_backrefs=False)

    __table_args__ = (
        UniqueConstraint('tx_nome', 'fk_cidade', name='ak_bairro'),
    )

    @validates('tx_nome')
    def convert_upper(self, key, value):
        return value.upper()

    @property
    def __dict_class__(self):
        return [
            {'Nome': self.tx_nome},
            {'Cidade': DAO.buscar_por_criterio(Cidade, pkey=self.fk_cidade)}
        ]

    @property
    def dict_fieldname(self):
        return {'Nome': 'tx_nome', 'Cidade': 'fk_cidade'}

    def __repr__(self):
        return f'{self.tx_nome} - {self.cidade.tx_nome}/{self.cidade.estado.tx_sigla}'


class Rua(db.Model):
    __tablename__ = 'rua'

    pkey = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
    tx_nome = db.Column(db.VARCHAR(80), nullable=False)
    tx_cep = db.Column(db.VARCHAR(10), nullable=False)
    fk_bairro = db.Column(db.VARCHAR(36), db.ForeignKey('bairro.pkey', name='FK_rua_bairro'), nullable=False)

    def __init__(self, tx_nome, tx_cep):
        self.pkey = Util.__generate_id__()
        self.tx_nome = tx_nome
        self.tx_cep = tx_cep

    # Relationship
    # Many to one
    bairro = db.relationship('Bairro', backref=backref('ruas', lazy=True), cascade_backrefs=False)

    __table_args__ = (
        UniqueConstraint('tx_nome', 'tx_cep', 'fk_bairro', name='ak_rua'),
    )

    @validates('tx_nome')
    def convert_upper(self, key, value):
        return value.upper()

    @property
    def __dict_class__(self):
        return [
            {'Nome': self.tx_nome},
            {'Cep': self.tx_cep},
            {'Bairro': DAO.buscar_por_criterio(Bairro, pkey=self.fk_bairro)}
        ]

    @property
    def dict_fieldname(self):
        return {'Nome': 'tx_nome', 'Cep': 'tx_cep', 'Bairro': 'fk_bairro'}

    def __repr__(self):
        return f'{self.tx_nome} - {self.bairro.tx_nome} - {self.bairro.cidade.tx_nome}/{self.bairro.cidade.estado.tx_sigla}'


class Endereco(db.Model):
    __tablename__ = 'endereco'

    pkey = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
    tx_numero = db.Column(db.VARCHAR(8), nullable=False, default='S/N')
    tx_complemento = db.Column(db.TEXT, nullable=True)
    fk_rua = db.Column(db.VARCHAR(36), db.ForeignKey('rua.pkey', name='FK_endereco_rua'), nullable=False)

    def __init__(self):
        self.pkey = Util.__generate_id__()

    # Relationship
    # Many to one
    rua = db.relationship('Rua', backref=backref('enderecos', lazy='select'), cascade_backrefs=False)

    __table_args__ = (
        UniqueConstraint('tx_numero', 'tx_complemento', 'fk_rua', name='ak_endereco'),
    )

    @validates('tx_numero', 'tx_complemento')
    def convert_upper(self, key, value):
        return value.upper()

    @property
    def __dict_class__(self):
        return [
            {'Numero': self.tx_numero},
            {'Complemento': self.tx_complemento},
            {'Rua': DAO.buscar_por_criterio(Rua, pkey=self.fk_rua)}
        ]

    @property
    def dict_fieldname(self):
        return {'Numero': 'tx_numero', 'Complemento': 'tx_complemento', 'Rua': 'fk_rua'}
