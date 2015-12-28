# coding=utf-8
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk.basic import WechatBasic
import requests


def wechat_kernel(wechat_context, request):
    # 获得解析结果, message 为 WechatMessage 对象 (wechat_sdk.messages中定义)
    print request.body
    message = wechat_context.get_message()
    if message.type == 'text':
        response = parse_text(wechat_context)
    elif message.type == 'image':
        response = wechat_context.response_text(u'图片')
    elif message.type == 'voice':
        response = parse_voice(wechat_context)
        # response = parse_tuling_msg(wechat, tuling(message.source, message.recognition))
    elif message.type == 'subscribe':
        response = wechat_context.response_text(u'人，生得靓仔，就特别多人关注~~~来，用语音同我讲野吧~~~')
    elif message.type == 'scan':
        response = wechat_context.response_text(message.key)
    else:
        response = wechat_context.response_text("未知")
    # 现在直接将 response 变量内容直接作为 HTTP Response 响应微信服务器即可，此处为了演示返回内容，直接将响应进行输出
    return response
    pass


@csrf_exempt
def wechat_auth(request):
    try:
        wechat = WechatBasic(appid="wx85ddc4617e4400b0", appsecret="237dc3cc551b6bac043f660cbab093ca", token="feynman")
        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']
        if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            if request.method == 'GET':
                return HttpResponse(request.GET.get('echostr', ''), content_type="text/plain")
            else:
                wechat.parse_data(request.body)
                return HttpResponse(wechat_kernel(wechat, request), content_type="application/xml")
        else:
            return HttpResponse("Valid Auth")

    except Exception, e:
        print e.message
        return HttpResponse(e.message)
        # finally:
        #     return HttpResponse("Hello World")


def parse_text(wechat_context):
    message = wechat_context.get_message()
    if "2222" in message.content:
        d = {"expire_seconds": 604800, "action_name": "QR_SCENE", "action_info": {"scene": {"scene_id": 123}}}
        return wechat_context.response_text(wechat_context.create_qrcode(dict(d)))
    if 'kq' in message.content:
        print "hello"
        from attendance.models import Attendance, AttendanceParam
        import datetime
        now = datetime.datetime.now()
        a = Attendance(checking_date_sys=now, type="morning", remark_text="test")
        a.save()
        print "world"
        return wechat_context.response_text(Attendance.objects.all())
        pass
    # if "QA" or "qa" in message.content:
    #     articles = []
    #     q = message.content.replace('qa', '').replace('QA', '')
    #     for item in QA.objects.filter(q__contains=q):
    #         articles.append({
    #             'title': item.q,
    #             'description': item.a,
    #         })
    #         if len(articles) == 10:
    #             break
    #     if articles:
    #         return wechat.response_news(articles)
    #     else:
    #         return parse_tuling_msg(wechat, tuling(message.source, q))
    # else:
    return parse_tuling_msg(wechat_context, tuling(message.source, message.content))


def parse_voice(wechat_context):
    message = wechat_context.get_message()
    if '考勤' in message.recognition:
        from attendance.models import Attendance, AttendanceParam
        import datetime
        now = datetime.datetime
        a = Attendance(checking_date_sys=now, type="morning", remark_text="test")
        a.save()
        pass
    else:
        response = parse_tuling_msg(wechat_context, tuling(message.source, message.recognition))
    return response
    pass


def parse_tuling_msg(wechat_context, json_data):
    try:
        print json_data['code']
        if json_data['code'] == 100000:
            return wechat_context.response_text(json_data['text'])
        elif json_data['code'] == 200000:
            return wechat_context.response_text(json_data['url'])
        elif json_data['code'] == 302000 or json_data['code'] == 308000:
            articles = []
            for data in json_data['list']:
                articles.append({'title': data['article'] if json_data['code'] == 302000 else data['name'],
                                 'description': data['source'] if json_data['code'] == 302000 else data['info'],
                                 'picurl': data['icon'], 'url': data['detailurl']})
                if len(articles) == 10:
                    break
            return wechat_context.response_news(articles)
        else:
            return wechat_context.response_text(json_data['text'])
    except Exception, e:
        print e.message
        print json_data['code']


def tuling(userid, info):
    # print info
    key = u'ebc23dad527e36a33299db7a192edeb5'
    url = u'http://www.tuling123.com/openapi/api'
    return requests.get(url, params={'key': key, 'info': info, 'userid': userid}).json()
