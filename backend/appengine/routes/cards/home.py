# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.cards import rest
from tekton.router import to_path

__author__ = 'bea'

@login_not_required
@no_csrf
def index():
    ctx = {'rest_list_path': to_path(rest.index),
           'rest_new_path': to_path(rest.salvar)}
    return TemplateResponse(ctx, 'cards/home.html')
