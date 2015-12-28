# -*- coding: utf-8 -*-

__all__ = ['WechatBasic', 'WechatExt']

try:
    from wechat.wechat_sdk import WechatBasic
    from wechat.wechat_sdk import WechatExt
except ImportError:
    pass