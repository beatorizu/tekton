# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse, JsonResponse
from tema.tema_model import LicaoForm, TemaForm

__author__ = 'Bea'

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = TemaForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)
    tema = form.fill_model()
    tema.put()
    dct = form.fill_with_model(tema)
    log.info(dct)
    return JsonUnsecureResponse(dct)
