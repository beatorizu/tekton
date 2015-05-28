# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tema.tema_model import LicaoForm, Tema
from tekton.gae.middleware.redirect import RedirectResponse
from routes import lessons

__author__ = 'Bea'

@no_csrf
@login_not_required
def salvar(**propriedades):
    propriedades['tema']=ndb.Key(Tema,int(propriedades['tema']))
    form = LicaoForm(**propriedades)
    erros = form.validate()
    if not erros:
        lesson = form.fill_model()
        lesson.put()
        return RedirectResponse(lessons)
    ctx = {'temas':Tema.query_ordenada_por_titulo().fetch(),'lesson':propriedades,'erros':erros}
    return TemplateResponse(ctx,'lessons/form.html')