# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from lesson_app.lesson_model import Lesson
from routes.lessons import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Lesson)
        mommy.save_one(Lesson)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        lesson_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'description', 'title']), set(lesson_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Lesson.query().get())
        json_response = rest.new(None, description='description_string', title='title_string')
        db_lesson = Lesson.query().get()
        self.assertIsNotNone(db_lesson)
        self.assertEquals('description_string', db_lesson.description)
        self.assertEquals('title_string', db_lesson.title)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['description', 'title']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        lesson = mommy.save_one(Lesson)
        old_properties = lesson.to_dict()
        json_response = rest.edit(None, lesson.key.id(), description='description_string', title='title_string')
        db_lesson = lesson.key.get()
        self.assertEquals('description_string', db_lesson.description)
        self.assertEquals('title_string', db_lesson.title)
        self.assertNotEqual(old_properties, db_lesson.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        lesson = mommy.save_one(Lesson)
        old_properties = lesson.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, lesson.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['description', 'title']), set(errors.keys()))
        self.assertEqual(old_properties, lesson.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        lesson = mommy.save_one(Lesson)
        rest.delete(None, lesson.key.id())
        self.assertIsNone(lesson.key.get())

    def test_non_lesson_deletion(self):
        non_lesson = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_lesson.key.id())
        self.assertIsNotNone(non_lesson.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

