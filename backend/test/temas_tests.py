# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest.case import TestCase
from routes.temas import new
from base import GAETestCase
from tekton.gae.middleware.redirect import RedirectResponse

__author__ = 'Bea'

class NewTests(TestCase):
    def test_success(self):
        resposta = new.salvar(titulo = 'Kana', descricao = 'Kana descricao')
        self.assertEqual(resposta,RedirectResponse)
        resposta.context