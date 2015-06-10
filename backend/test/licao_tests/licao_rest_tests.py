# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from licao_app.licao_model import Licao
from routes.licaos import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Licao)
        mommy.save_one(Licao)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        licao_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'titulo', 'descricao', 'tema']), set(licao_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Licao.query().get())
        json_response = rest.new(None, titulo='titulo_string', descricao='descricao_string', tema='tema_string')
        db_licao = Licao.query().get()
        self.assertIsNotNone(db_licao)
        self.assertEquals('titulo_string', db_licao.titulo)
        self.assertEquals('descricao_string', db_licao.descricao)
        self.assertEquals('tema_string', db_licao.tema)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['titulo', 'descricao', 'tema']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        licao = mommy.save_one(Licao)
        old_properties = licao.to_dict()
        json_response = rest.edit(None, licao.key.id(), titulo='titulo_string', descricao='descricao_string', tema='tema_string')
        db_licao = licao.key.get()
        self.assertEquals('titulo_string', db_licao.titulo)
        self.assertEquals('descricao_string', db_licao.descricao)
        self.assertEquals('tema_string', db_licao.tema)
        self.assertNotEqual(old_properties, db_licao.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        licao = mommy.save_one(Licao)
        old_properties = licao.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, licao.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['titulo', 'descricao', 'tema']), set(errors.keys()))
        self.assertEqual(old_properties, licao.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        licao = mommy.save_one(Licao)
        rest.delete(None, licao.key.id())
        self.assertIsNone(licao.key.get())

    def test_non_licao_deletion(self):
        non_licao = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_licao.key.id())
        self.assertIsNotNone(non_licao.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

