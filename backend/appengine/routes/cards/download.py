# -*- coding: utf-8 -*-
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required

__author__ = 'bea'


@no_csrf
@login_required
def index(_handler,audio):
    _handler.send_blob(audio)