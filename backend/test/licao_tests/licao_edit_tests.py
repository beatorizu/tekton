# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from licao_app.licao_model import Licao
from routes.licaos.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        licao = mommy.save_one(Licao)
        template_response = index(licao.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        licao = mommy.save_one(Licao)
        old_properties = licao.to_dict()
        redirect_response = save(licao.key.id(), titulo='titulo_string', descricao='descricao_string', tema='tema_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_licao = licao.key.get()
        self.assertEquals('titulo_string', edited_licao.titulo)
        self.assertEquals('descricao_string', edited_licao.descricao)
        self.assertEquals('tema_string', edited_licao.tema)
        self.assertNotEqual(old_properties, edited_licao.to_dict())

    def test_error(self):
        licao = mommy.save_one(Licao)
        old_properties = licao.to_dict()
        template_response = save(licao.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['titulo', 'descricao', 'tema']), set(errors.keys()))
        self.assertEqual(old_properties, licao.key.get().to_dict())
        self.assert_can_render(template_response)
