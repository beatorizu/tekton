# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from lesson_app.lesson_model import Lesson
from routes.lessons.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        lesson = mommy.save_one(Lesson)
        template_response = index(lesson.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        lesson = mommy.save_one(Lesson)
        old_properties = lesson.to_dict()
        redirect_response = save(lesson.key.id(), description='description_string', title='title_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_lesson = lesson.key.get()
        self.assertEquals('description_string', edited_lesson.description)
        self.assertEquals('title_string', edited_lesson.title)
        self.assertNotEqual(old_properties, edited_lesson.to_dict())

    def test_error(self):
        lesson = mommy.save_one(Lesson)
        old_properties = lesson.to_dict()
        template_response = save(lesson.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['description', 'title']), set(errors.keys()))
        self.assertEqual(old_properties, lesson.key.get().to_dict())
        self.assert_can_render(template_response)
