# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb

from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
from gaepermission.model import MainUser
from tema.tema_model import Revisao


@login_required
@no_csrf
def index(_logged_user):
    uid = _logged_user.key
    rewiews=Revisao.query_total_review(uid).fetch()
    total=0
    right=0
    wrong=0
    for review in rewiews:
        total+=1
        if review.status: right+=1
        else: wrong+=1
    properties={'total':total,'wrong':wrong,'right':right}
    return TemplateResponse(properties,'progresso/home.html')

