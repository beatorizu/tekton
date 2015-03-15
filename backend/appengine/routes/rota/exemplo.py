from __future__ import absolute_import, unicode_literals
from tekton import router

__author__ = 'Bea'

# -*- coding: utf-8 -*-
import gaecookie.decorator
from gaepermission.decorator import login_not_required
from tekton import router

@login_not_required
@gaecookie.decorator.no_csrf
def index(_handler):
    path = router.to_path(funcao)
    _handler.redirect(path)

@login_not_required
@gaecookie.decorator.no_csrf
def funcao(_resp):
    _resp.write("Bea's funcao")