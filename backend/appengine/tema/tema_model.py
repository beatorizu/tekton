# -*-coding: utf-8-*-

from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.base import IntegerField
from gaeforms.ndb.form import ModelForm
from gaeforms.ndb.property import SimpleCurrency

__author__ = 'Bea'

class Tema(ndb.Model):
    titulo = ndb.StringProperty(required=True)
    descricao = ndb.StringProperty(required=True)

    @classmethod
    def query_ordenada_por_titulo(cls):
        return cls.query().order(Tema.titulo)

class TemaForm(ModelForm):
    _model_class = Tema
    _include = [Tema.titulo,Tema.descricao]

class Licao(ndb.Model):
    titulo = ndb.StringProperty(required=True)
    descricao = ndb.StringProperty(required=True)
    tema = ndb.KeyProperty(Tema, required=True)

    @classmethod
    def query_ordenada_por_titulo(cls):
        return cls.query().order(Licao.titulo)

    @classmethod
    def query_por_tema_ordenada_por_nome(cls, tema_selecionado):
        if isinstance(tema_selecionado, basestring):
            tema_selecionado = ndb.Key(Tema, int(tema_selecionado))
        return cls.query(cls.tema==tema_selecionado).order(cls.titulo)

class LicaoForm(ModelForm):
    _model_class = Licao
