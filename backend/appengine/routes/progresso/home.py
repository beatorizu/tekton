# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb

from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
from gaepermission.model import MainUser


@login_required
@no_csrf
def index(_logged_user):
    key = _logged_user.key
    # usar para relacionar com cartão
    user_id = key.id()
    print(ndb.Key(MainUser,int(user_id)))
    # print(user_id)
    return TemplateResponse()

