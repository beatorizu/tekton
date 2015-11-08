# -*- coding: utf-8 -*-
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from tema.tema_model import Cartao, CartaoForm, LicaoForm, Licao
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse

__author__ = 'bea'



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

@no_csrf
def indexl(lid):
    query = Cartao.query_por_licao_ordenada_por_frase(lid)
    cards = query.fetch()
    for card in cards:
        key = card.key
        key_id = key.id()
    form = CartaoForm()
    cards = [form.fill_with_model(c) for c in cards]

    return JsonResponse(cards)

@no_csrf
def listarLessons():
    form = LicaoForm()
    lessons = Licao.query_ordenada_por_titulo().fetch()
    for lesson in lessons:
        key = lesson.key
        key_id = key.id()
    lessons = [form.fill_with_model(l) for l in lessons]
    return JsonResponse(lessons)

@no_csrf
def salvar(_resp, **propriedades):
    #img_url
    #sound - to_path(id,filename)
    #form action="path/to/method"
    #get_serving_url - blobcomands
    #blob_model

    form = CartaoForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)

    propriedades['licao'] = ndb.Key(Licao, int(propriedades['licao']))
    card = form.fill_model()

    card.put()
    dct = form.fill_with_model(card)
    log.info(dct)
    return JsonUnsecureResponse(dct)

@no_csrf
def rev(cid):
    cards = Cartao.query(Cartao.key == ndb.Key(Cartao, int(cid))).fetch()
    for c in cards:
        key = c.key
    form = CartaoForm()
    cards = [form.fill_with_model(c) for c in cards]
    ctx = {'cartao':cards[0]}
    return JsonResponse(ctx)

@no_csrf
def deletar(card_id):
    key = ndb.Key(Cartao,int(card_id))
    key.delete()