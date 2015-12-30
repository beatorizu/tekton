# -*- coding: utf-8 -*-
from routes import cards
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.cards import upload
from tekton.router import to_path
from tema.tema_model import Cartao, CartaoForm, LicaoForm, Licao
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse

from tekton.gae.middleware.redirect import RedirectResponse

__author__ = 'bea'


@no_csrf
def save(**kwargs):

    form = CartaoForm(**kwargs)
    erros = form.validate()
    if not erros:
        kwargs = form.normalize()
        card = Cartao(**kwargs)
        cartao = card.put()
        id = cartao.id()
        return RedirectResponse(to_path(upload,id))
    else:
        ctx = {'card':kwargs,'errors':erros}
        return TemplateResponse(ctx,'cards/formpart1.html')