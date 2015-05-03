# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from lesson_app.lesson_model import Lesson
from routes.lessons.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Lesson)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        lesson = mommy.save_one(Lesson)
        redirect_response = delete(lesson.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(lesson.key.get())

    def test_non_lesson_deletion(self):
        non_lesson = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_lesson.key.id())
        self.assertIsNotNone(non_lesson.key.get())

