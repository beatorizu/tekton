# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse
from tema.tema_model import LicaoForm

__author__ = 'Bea'

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = LicaoForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)
    licao = form.fill_model()
    licao.put()
    dct = form.fill_with_model(licao)
    log.info(dct)
    return JsonUnsecureResponse(dct)
