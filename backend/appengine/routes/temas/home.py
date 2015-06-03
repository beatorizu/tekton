# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.temas import edit, rest
from routes.temas.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tema.tema_model import Tema
from tekton.router import to_path
from google.appengine.ext import ndb

__author__ = 'Bea'

@login_not_required
@no_csrf
def index():
    query = Tema.query_ordenada_por_titulo()
    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)
    temas = query.fetch()
    for tema in temas:
        key = tema.key
        key_id = key.id()
        tema.edit_path = to_path(edit_path_base, key_id)
        tema.deletar_path = to_path(deletar_path_base, key_id)
    #'temas/rest/salvar'
    ctx = {'salvar_path': to_path(salvar),'temas':temas, 'rest_new_path': to_path(rest.salvar)}
    return TemplateResponse(ctx, 'temas/home.html')

@login_not_required
@no_csrf
def deletar(tema_id):
    key = ndb.Key(Tema, int(tema_id))
    key.delete()
    return RedirectResponse(to_path(index))