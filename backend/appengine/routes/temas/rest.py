# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse, JsonResponse
from tema.tema_model import LicaoForm, TemaForm, Tema

__author__ = 'Bea'

@login_not_required
@no_csrf
def index():
    query = Tema.query_ordenada_por_titulo()
    temas = query.fetch()
    for tema in temas:
        key = tema.key
        key_id = key.id()
    form = TemaForm()
    temas = [form.fill_with_model(t) for t in temas]

    return JsonResponse(temas)

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = TemaForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)
    tema = form.fill_model()
    tema.put()
    dct = form.fill_with_model(tema)
    log.info(dct)
    return JsonUnsecureResponse(dct)

@login_not_required
@no_csrf
def deletar(tema_id):
    key = ndb.Key(Tema, int(tema_id))
    key.delete()