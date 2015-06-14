# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.lessons import rest
from tekton.router import to_path

__author__ = 'Bea'

@login_not_required
@no_csrf
def index():
    ctx = {'rest_list_path':to_path(rest.index),
           'rest_delete_path': to_path(rest.deletar),
           'rest_edit_path': to_path(rest.editar),
           'rest_list_tema_path': to_path(rest.listaTemas),
           'rest_new_path': to_path(rest.salvar)}
    return TemplateResponse(ctx, 'lessons/home.html')