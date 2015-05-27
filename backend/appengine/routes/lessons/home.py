# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from tema.tema_model import Tema, Licao, LicaoForm

__author__ = 'Bea'

@login_not_required
@no_csrf
def index(tema_selecionado = None):
    ctx = {'temas':Tema.query_ordenada_por_titulo().fetch(),
           'salvar_path':to_path(salvar),
           'pesquisar_path:':to_path(index)}
    if tema_selecionado is None:
        ctx['lessons'] = Licao.query_ordenada_por_titulo().fetch()
        ctx['tema_selecionado'] = None
    else:
        ctx['tema_selecionado'] = Tema.get_by_id(int(tema_selecionado))
        ctx['lessons'] = Licao.query_por_tema_ordenada_por_nome(tema_selecionado)
    return TemplateResponse(ctx,'lessons/home.html')

@login_not_required
@no_csrf
def salvar(**propriedades):
    propriedades['tema']=ndb.Key(Tema,int(propriedades['tema']))
    form = LicaoForm(**propriedades)
    erros = form.validate()
    if not erros:
        lesson = form.fill_model()
        lesson.put()
        return RedirectResponse(index)
    ctx = {'tema':propriedades, 'erros':erros}
    return TemplateResponse(ctx,'lessons/home.html')