# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from gaecookie.decorator import no_csrf
from gaepermission import facade
from gaepermission.decorator import login_not_required
from tekton import router
from config.template_middleware import TemplateResponse

#
# @login_not_required
# @no_csrf
# def index(_resp, ret_path='/'):
#     return RedirectResponse(ret_path)

#! /usr/bin/env python
# coding:utf-8

import twitter_oauth

# write your oauth token and oauth token secret
consumer_key = 'uCqvQmq0Q9jC4ZKBO8x3VWpqX'
consumer_secret = ' ms0YpsYyt8hqyOPXlUEVpYeCOSCAqn9fpHYtrqGAa7dHUGO1bV'

# create GetOauth instance
get_oauth_obj = twitter_oauth.GetOauth(consumer_key, consumer_secret)

# get oauth_token and oauth token secret
key_dict = get_oauth_obj.get_oauth()

# create Api instance
api = twitter_oauth.Api(consumer_key, consumer_secret, key_dict['oauth_token'], key_dict['oauth_token_secret'])

# get friends timeline
print [status.text for status in api.get_friends_timeline()]

# get user timeline
print [status.text for status in api.get_user_timeline()]

# get replies
print [status.text for status in api.get_replies()]

# post update
api.post_update(u'こんにちは, Twitter')