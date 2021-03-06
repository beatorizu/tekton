# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.temas import rest
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse, JsonResponse
from tekton.router import to_path
from tema.tema_model import LicaoForm, Licao, Tema, TemaForm
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse

__author__ = 'Bea'

@login_not_required
@no_csrf
def listaTemas():
    temas = Tema.query_ordenada_por_titulo().fetch()
    for tema in temas:
        key = tema.key
        key_id = key.id()
    form = TemaForm()
    temas = [form.fill_with_model(t) for t in temas]

    return JsonResponse(temas)

@login_not_required
@no_csrf
def index():
    form = LicaoForm()
    lessons = Licao.query_ordenada_por_titulo().fetch()
    for lesson in lessons:
        key = lesson.key
        key_id = key.id()
    lessons = [form.fill_with_model(l) for l in lessons]
    return JsonResponse(lessons)

@login_not_required
@no_csrf
def indext(tid):
    query = Licao.query_por_tema_ordenada_por_nome(tid)
    lessons = query.fetch()
    for lesson in lessons:
        key = lesson.key
        key_id = key.id()
    form = LicaoForm()
    lessons = [form.fill_with_model(l) for l in lessons]

    return JsonResponse(lessons)

@login_not_required
@no_csrf
def deletar(lesson_id):
    key = ndb.Key(Licao,int(lesson_id))
    key.delete()

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = LicaoForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)
    propriedades['tema'] = ndb.Key(Tema, int(propriedades['tema']))
    form = LicaoForm(**propriedades)
    licao = form.fill_model()
    licao.put()
    dct = form.fill_with_model(licao)
    log.info(dct)
    return JsonUnsecureResponse(dct)

@login_not_required
@no_csrf
def editar(_resp, **propriedades):
    form = LicaoForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)
    licao = ndb.Key(Licao, int(propriedades['lesson_id'])).get()
    licao.titulo = propriedades['titulo']
    licao.descricao = propriedades['descricao']
    licao.put()
    dct = form.fill_with_model(licao)
    log.info(dct)
    return JsonUnsecureResponse(dct)

@login_not_required
@no_csrf
def criar(lesson_id):
    ctx = {'lesson_id':lesson_id}
    return TemplateResponse(ctx, '/cards/home.html')