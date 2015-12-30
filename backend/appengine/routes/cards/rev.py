# -*- coding: utf-8 -*-
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from tema.tema_model import CartaoForm
from routes.cards import rest

__author__ = 'bea'

@no_csrf
def index(cid):
    card = rest.rev(cid)
    ctx = {'cartao': card}
    return TemplateResponse(ctx, 'cards/rev.html')