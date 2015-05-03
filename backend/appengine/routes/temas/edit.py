# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes import temas
from tekton.gae.middleware.redirect import RedirectResponse
from tema.tema_model import Tema
from tekton.router import to_path

__author__ = 'Bea'

@no_csrf
def index(tema_id):
    tema = Tema.get_by_id(int(tema_id))
    ctx = {'tema':tema, 'salvar_path': to_path(atualizar)}
    return TemplateResponse(ctx, '/temas/form.html')

def atualizar(tema_id, titulo):
    tema = Tema.get_by_id(int(tema_id))
    tema.titulo = titulo
    tema.put()
    return RedirectResponse(temas)