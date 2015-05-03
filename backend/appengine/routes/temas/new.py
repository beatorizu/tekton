# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from routes import temas
from tekton.gae.middleware.redirect import RedirectResponse
from tema.tema_model import TemaForm, Tema

__author__ = 'Bea'

def salvar(**kwargs):
    form = TemaForm(**kwargs)
    erros = form.validate()
    if not erros:
        propriedades = form.normalize()
        tema = Tema(**propriedades)
        tema.put()
        return RedirectResponse(temas)
    else:
        ctx = {'tema':kwargs, 'erros':erros}
        return TemplateResponse(ctx, '/temas/form.html')