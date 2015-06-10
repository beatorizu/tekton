# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse, JsonResponse
from tema.tema_model import LicaoForm, Licao
from google.appengine.ext import ndb

__author__ = 'Bea'

@login_not_required
@no_csrf
def index():
    form = LicaoForm()
    lessons = Licao.query_ordenada_por_titulo().fetch()
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