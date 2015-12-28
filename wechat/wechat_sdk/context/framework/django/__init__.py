# -*- coding: utf-8 -*-

default_app_config = 'wechat_sdk.context.framework.django.apps.ContextConfig'

try:
    from wechat.wechat_sdk.context.framework.django.models import Context as DatabaseContext
    from wechat.wechat_sdk.context.framework.django.backends import ContextStore as DatabaseContextStore
except ImportError:
    pass