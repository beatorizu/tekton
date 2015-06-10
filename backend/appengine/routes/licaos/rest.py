# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse
from licao_app import licao_facade

@login_not_required
def index():
    cmd = licao_facade.list_licaos_cmd()
    licao_list = cmd()
    licao_form = licao_facade.licao_form()
    licao_dcts = [licao_form.fill_with_model(m) for m in licao_list]
    return JsonResponse(licao_dcts)

@login_not_required
def new(_resp, **licao_properties):
    cmd = licao_facade.save_licao_cmd(**licao_properties)
    return _save_or_update_json_response(cmd, _resp)

@login_not_required
def edit(_resp, id, **licao_properties):
    cmd = licao_facade.update_licao_cmd(id, **licao_properties)
    return _save_or_update_json_response(cmd, _resp)

@login_not_required
def delete(_resp, id):
    cmd = licao_facade.delete_licao_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)

@login_not_required
def _save_or_update_json_response(cmd, _resp):
    try:
        licao = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    licao_form = licao_facade.licao_form()
    return JsonResponse(licao_form.fill_with_model(licao))

