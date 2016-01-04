# -*- coding: utf-8 -*-
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
from routes.cards.rest import rev
from tekton.router import to_path
from tema.tema_model import CartaoForm
from routes.cards import rest

__author__ = 'bea'

@no_csrf
@login_required
def index(cid=''):
    ctx = {'rest_rev_path': to_path(rev,cid)}
    return TemplateResponse(ctx, 'cards/rev.html')