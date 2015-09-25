# -*- coding: utf-8 -*-
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from tema.tema_model import Cartao, CartaoForm

__author__ = 'bea'


@login_not_required
@no_csrf
def index():
    query = Cartao.query_ordenada_por_frase()
    cards = query.fetch()
    for card in cards:
        key = card.key
        key_id = key.id()
    form = CartaoForm()
    cards = [form.fill_with_model(c) for c in cards]

    return JsonResponse(cards)

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = CartaoForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)
    card = form.fill_model()
    card.put()
    dct = form.fill_with_model(card)
    log.info(dct)
    return JsonUnsecureResponse(dct)