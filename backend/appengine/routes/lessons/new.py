# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from tema.tema_model import LicaoForm, Tema
from tekton.gae.middleware.redirect import RedirectResponse
from routes import lessons

__author__ = 'Bea'

def savar(**propriedades):
    propriedades['tema'] = ndb.Key(Tema, int(propriedades['tema']))
    form = LicaoForm(**propriedades)
    erros = form.validate()
    if erros:
        return
    licao = form.fill_model()
    licao.put()
    return RedirectResponse(lessons)