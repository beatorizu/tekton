# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest.case import TestCase

__author__ = 'Bea'


def soma(param, param1):
    return 3


class OperacoesTests(TestCase):
    def test_soma(self):
        resultado = soma(2,2)
        self.assertEqual(4, resultado)
        
    def test_balt(self):
        pass