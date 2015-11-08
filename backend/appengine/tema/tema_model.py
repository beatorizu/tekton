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
    _include = [Licao.titulo,Licao.descricao,Licao.tema]

class Cartao(ndb.Model):
    frase = ndb.StringProperty(required=True)
    resposta = ndb.StringProperty(required=True)
    imagem = ndb.KeyProperty()
    audio = ndb.KeyProperty()
    licao = ndb.KeyProperty(Licao)
    kanji = ndb.StringProperty(required=True)
    alternativa0 = ndb.StringProperty(required=True)
    alternativa1 = ndb.StringProperty(required=True)
    alternativa2 = ndb.StringProperty(required=True)

    @classmethod
    def query_ordenada_por_frase(cls):
        return cls.query().order(Cartao.frase)
    @classmethod
    def query_por_licao_ordenada_por_frase(cls, lid):
        if isinstance(lid, basestring):
            lid = ndb.Key(Licao, int(lid))
        return cls.query(cls.licao==lid).order(cls.frase)

class CartaoForm(ModelForm):
    _model_class = Cartao
    _include = [Cartao.frase,Cartao.resposta,Cartao.alternativa0,Cartao.alternativa1,Cartao.alternativa2,Cartao.licao,Cartao.imagem,Cartao.audio,Cartao.kanji]
