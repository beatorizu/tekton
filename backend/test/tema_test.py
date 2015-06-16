# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

__author__ = 'Bea'

from base import GAETestCase
from config.template_middleware import TemplateResponse
from routes.temas import new
from tekton.gae.middleware.redirect import RedirectResponse
from tema.tema_model import Tema

class NewTeste(GAETestCase):
    def test_sucesso(self):
        resposta = new.salvar(titulo='titulo',descricao='descricao')
        self.assertIsInstance(resposta, RedirectResponse)
        self.assertEqual('/temas',resposta.context)
        temas = Tema.query().fetch()
        self.assertEqual(1,len(temas))
        tema = temas[0]
        self.assertEqual('titulo',tema.titulo)
        self.assertEqual('descricao',tema.descricao)

    def test_validacao(self):
        resposta = new.salvar()
        self.assertIsInstance(resposta,TemplateResponse)
        self.assert_can_render(resposta)
        self.assertIsNone(Tema.query().get())
        self.maxDiff = True
        self.assertDictEqual({u'tema':{},u'erros':{'titulo':u'Required field','descricao':u'Required field'}},resposta.context)