# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from lesson_app.lesson_model import Lesson
from routes.lessons.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Lesson.query().get())
        redirect_response = save(description='description_string', title='title_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_lesson = Lesson.query().get()
        self.assertIsNotNone(saved_lesson)
        self.assertEquals('description_string', saved_lesson.description)
        self.assertEquals('title_string', saved_lesson.title)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['description', 'title']), set(errors.keys()))
        self.assert_can_render(template_response)
