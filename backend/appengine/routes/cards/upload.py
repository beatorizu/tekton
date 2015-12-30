# -*- coding: utf-8 -*-
from google.appengine.api.app_identity import get_default_gcs_bucket_name
from google.appengine.ext import blobstore

from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from blob_app import blob_facade
from routes import cards
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from tema.tema_model import Cartao

__author__ = 'bea'


@no_csrf
def index(cartao):
    success_url = to_path(save)
    bucket = get_default_gcs_bucket_name()
    url = blobstore.create_upload_url(success_url, gs_bucket_name=bucket)
    ctx = {'upload_url': url,
               'cartao': cartao}
    return TemplateResponse(ctx, 'cards/formpart2.html')

@no_csrf
def save(_handler,cartao,audio):
    blob_infos = _handler.get_uploads('audio')[0]
    cartao = Cartao.get_by_id(int(cartao))
    cartao.audio = blob_infos.key()
    cartao.put()
    path = to_path(cards)
    return RedirectResponse(path)