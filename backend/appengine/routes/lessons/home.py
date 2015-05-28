# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from permission_app.model import ADMIN
from routes.lessons.new import salvar
from tekton.router import to_path
from tema.tema_model import Tema, Licao

__author__ = 'Bea'

@login_not_required
@no_csrf
def index(tema_selecionado = None):
    ctx = {'temas':Tema.query_ordenada_por_titulo().fetch(),
           'salvar_path':to_path(salvar),
           'pesquisar_path':to_path(index)}
    if tema_selecionado is None:
        ctx['tema_selecionado'] = None
    else:
        ctx['tema_selecionado'] = Tema.get_by_id(int(tema_selecionado))
    return TemplateResponse(ctx,'lessons/home.html')

def pesquisar():
    ctx = {'temas':Tema.query_ordenada_por_titulo().fetch(),
           }
    if tema_selecionado is None:
         ctx['lessons'] = Licao.query_ordenada_por_titulo().fetch()
         ctx['tema_selecionado'] = None
    else:
         ctx['tema_selecionado'] = Tema.get_by_id(int(tema_selecionado))
         ctx['lessons'] = Licao.query_por_tema_ordenada_por_nome(tema_selecionado)
-   return TemplateResponse(ctx,'lessons/home.html')