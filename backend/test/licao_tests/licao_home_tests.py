# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from licao_app.licao_model import Licao
from routes.licaos.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Licao)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        licao = mommy.save_one(Licao)
        redirect_response = delete(licao.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(licao.key.get())

    def test_non_licao_deletion(self):
        non_licao = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_licao.key.id())
        self.assertIsNotNone(non_licao.key.get())

