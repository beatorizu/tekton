from __future__ import absolute_import, unicode_literals

__author__ = 'Bea'

# -*- coding: utf-8 -*-
import gaecookie.decorator
from gaepermission.decorator import login_not_required


@login_not_required
@gaecookie.decorator.no_csrf
def index(_resp):
    return TemplateResponse()