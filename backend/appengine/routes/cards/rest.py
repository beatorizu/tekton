# -*- coding: utf-8 -*-
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required, login_not_required, permissions
from permission_app.model import ADMIN
from routes.cards import new, download
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from tekton.router import to_path
from tema.tema_model import Cartao, CartaoForm, LicaoForm, Licao
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse

__author__ = 'bea'


@no_csrf
@login_not_required
def index():
    query = Cartao.query_ordenada_por_frase()
    cards = query.fetch()
    for card in cards:
        key = card.key
        key_id = key.id()
    form = CartaoForm()

    def localized_card(card):
        card_dic = form.fill_with_model(card)
        return card_dic

    localized_cards = [localized_card(card) for card in cards]

    return JsonResponse(localized_cards)

@no_csrf
@login_not_required
def indexl(lid):
    query = Cartao.query_por_licao_ordenada_por_frase(lid)
    cards = query.fetch()
    for card in cards:
        key = card.key
        key_id = key.id()
    form = CartaoForm()
    def localized_card(card):
        card_dic = form.fill_with_model(card)
        return  card_dic

    localized_cards = [localized_card(card) for card in cards]

    return JsonResponse(localized_cards)

@no_csrf
@login_not_required
def listarLessons():
    form = LicaoForm()
    lessons = Licao.query_ordenada_por_titulo().fetch()
    for lesson in lessons:
        key = lesson.key
        key_id = key.id()
    lessons = [form.fill_with_model(l) for l in lessons]
    return JsonResponse(lessons)

@no_csrf
@login_not_required
def salvar(_resp, **propriedades):

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
@login_required
def rev(cid):
    form = CartaoForm()
    card = Cartao.get_by_id(int(cid))
    dct = form.fill_with_model(card)
    dct['audio_link'] = to_path(download,card.audio)

    ctx = {'cartao':dct}
    return JsonResponse(ctx)

@no_csrf
@permissions(ADMIN)
def deletar(card_id):
    key = ndb.Key(Cartao,int(card_id))
    key.delete()

@no_csrf
@login_not_required
def create(lid):
    ctx = {'rest_save_text_path': to_path(new.save),'licao':lid}
    return TemplateResponse(ctx,'cards/formpart1.html')

@no_csrf
@login_not_required
def chooseLesson():
    ctx = {'rest_list_path':to_path(listarLessons)}
    return TemplateResponse(ctx,'cards/formpart0.html')