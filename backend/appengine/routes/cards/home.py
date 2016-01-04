# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.api.users import is_current_user_admin

from config.template_middleware import TemplateResponse

from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.cards import rest, rev, new
# from routes.cards.new import save
from tekton.router import to_path

__author__ = 'bea'


@no_csrf
@login_not_required
def index(lid=''):
    admin=0
    if is_current_user_admin():admin=1
    ctx = {'rest_delete_path': to_path(rest.deletar),
           'lid': lid,
           'admin':admin}
    if lid is '':
        ctx['rest_new_path'] = to_path(rest.chooseLesson)
        ctx['rest_list_path'] = to_path(rest.index)
    else:
        ctx['rest_new_path'] = to_path(rest.create,lid)
        ctx['rest_list_path'] = to_path(rest.indexl,lid)
    return TemplateResponse(ctx, 'cards/home.html')
