# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from licao_app import licao_facade
from routes.licaos import new, edit
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    cmd = licao_facade.list_licaos_cmd()
    licaos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    licao_form = licao_facade.licao_form()

    def localize_licao(licao):
        licao_dct = licao_form.fill_with_model(licao)
        licao_dct['edit_path'] = router.to_path(edit_path, licao_dct['id'])
        licao_dct['delete_path'] = router.to_path(delete_path, licao_dct['id'])
        return licao_dct

    localized_licaos = [localize_licao(licao) for licao in licaos]
    context = {'licaos': localized_licaos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context, 'licaos/licao_home.html')


def delete(licao_id):
    licao_facade.delete_licao_cmd(licao_id)()
    return RedirectResponse(router.to_path(index))

