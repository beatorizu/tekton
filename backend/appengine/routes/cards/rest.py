# -*- coding: utf-8 -*-
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from tema.tema_model import Cartao, CartaoForm, LicaoForm, Licao

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
def listarLessons():
    form = LicaoForm()
    lessons = Licao.query_ordenada_por_titulo().fetch()
    for lesson in lessons:
        key = lesson.key
        key_id = key.id()
    lessons = [form.fill_with_model(l) for l in lessons]
    return JsonResponse(lessons)

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