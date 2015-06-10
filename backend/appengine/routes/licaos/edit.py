# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from licao_app import licao_facade
from routes import licaos
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(licao_id):
    licao = licao_facade.get_licao_cmd(licao_id)()
    licao_form = licao_facade.licao_form()
    context = {'save_path': router.to_path(save, licao_id), 'licao': licao_form.fill_with_model(licao)}
    return TemplateResponse(context, 'licaos/licao_form.html')


def save(licao_id, **licao_properties):
    cmd = licao_facade.update_licao_cmd(licao_id, **licao_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'licao': licao_properties}

        return TemplateResponse(context, 'licaos/licao_form.html')
    return RedirectResponse(router.to_path(licaos))

