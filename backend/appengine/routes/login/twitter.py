# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from gaecookie.decorator import no_csrf
from gaepermission import facade
from gaepermission.decorator import login_not_required
from tekton import router
from config.template_middleware import TemplateResponse
from tekton.gae.middleware.redirect import RedirectResponse
import tweepy

@login_not_required
@no_csrf
def index(_resp, ret_path='/'):
    auth = tweepy.OAuthHandler('uCqvQmq0Q9jC4ZKBO8x3VWpqX', 'ms0YpsYyt8hqyOPXlUEVpYeCOSCAqn9fpHYtrqGAa7dHUGO1bV')
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print 'Error! Failed to get request token.'
    return RedirectResponse(ret_path)
