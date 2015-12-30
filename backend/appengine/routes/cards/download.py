# -*- coding: utf-8 -*-
from gaecookie.decorator import no_csrf

__author__ = 'bea'


@no_csrf
def index(_handler,audio):
    _handler.send_blob(audio)