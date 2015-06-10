# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from licao_app.licao_model import Licao
from routes.licaos.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Licao.query().get())
        redirect_response = save(titulo='titulo_string', descricao='descricao_string', tema='tema_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_licao = Licao.query().get()
        self.assertIsNotNone(saved_licao)
        self.assertEquals('titulo_string', saved_licao.titulo)
        self.assertEquals('descricao_string', saved_licao.descricao)
        self.assertEquals('tema_string', saved_licao.tema)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['titulo', 'descricao', 'tema']), set(errors.keys()))
        self.assert_can_render(template_response)
