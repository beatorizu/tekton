# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import ndb
from gaepermission.decorator import login_not_required
from routes.rest import lessons
from tekton.gae.middleware.redirect import RedirectResponse
from tema.tema_model import Tema, Licao
from tekton.router import to_path

__author__ = 'Bea'

@no_csrf
@login_not_required
def index(lesson_id):
    lesson = Licao.get_by_id(int(lesson_id))
    ctx = {'lesson':lesson, 'salvar_path': to_path(atualizar)}
    return TemplateResponse(ctx, 'lessons/home.html')

@no_csrf
@login_not_required
def atualizar(lesson_id, titulo, descricao, tema):
    lesson = Licao.get_by_id(int(lesson_id))
    lesson.titulo = titulo
    lesson.descricao = descricao
    lesson.tema = ndb.Key(Tema,int(tema))
    lesson.put()
    return RedirectResponse(lessons)