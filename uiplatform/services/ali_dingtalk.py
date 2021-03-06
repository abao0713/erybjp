# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         ali_dingtalk
# Description:  
# Author:       yuanbaojun
# Date:         2020/11/10
#----------------------------

import time
import hmac
import hashlib
import base64
import urllib.parse
import json
import requests
import logging

try:
    JSONDecodeError = json.decoder.JSONDecodeError
except AttributeError:
    JSONDecodeError = ValueError

URL = "https://oapi.dingtalk.com/robot/send?access_token=94365d973019b26147e61de5e1ef23ad86d5ce8a4f36e6c56a03b72c681c8705"
SIGN = "SEC4cf8edcdeb0cd0066b4f42e005585c833ec119c642b0c5bf2881d39a221d4940"
def is_not_null_and_blank_str(content):
    if content and content.strip():
        return True
    else:
        return False


class DingtalkRobot(object):
    def __init__(self, webhook=URL, sign=SIGN):
        super(DingtalkRobot, self).__init__()
        self.webhook = webhook
        self.sign = sign
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.times = 0
        self.start_time = time.time()

    # 加密签名
    def __spliceUrl(self) -> str:
        timestamp = round(time.time() * 1000)
        secret = self.sign
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = f"{self.webhook}&timestamp={timestamp}&sign={sign}"
        return url

    def send_text(self, msg, at_mobiles, is_at_all=False):
        data = {"msgtype": "text", "at": {}}
        if is_not_null_and_blank_str(msg):
            data["text"] = {"content": msg}
        else:
            logging.error("text类型，消息内容不能为空！")
            raise ValueError("text类型，消息内容不能为空！")

        if is_at_all:
            data["at"]["isAtAll"] = is_at_all

        if at_mobiles:
            at_mobiles = list(map(str, at_mobiles))
            data["at"]["atMobiles"] = at_mobiles

        logging.debug('text类型：%s' % data)
        return self.__post(data)

    def send_markdown(self, msg, mark_text, at_mobiles, is_at_all=False):
        data = {"msgtype": "markdown", "at": {}}
        if is_not_null_and_blank_str(msg):
            data["markdown"] = {"title": msg, "text": mark_text}
        else:
            logging.error("markdown类型，消息内容不能为空！")
            raise ValueError("markdown类型，消息内容不能为空！")

        if is_at_all:
            data["at"]["isAtAll"] = is_at_all

        if at_mobiles:
            at_mobiles = list(map(str, at_mobiles))
            data["at"]["atMobiles"] = at_mobiles

        logging.debug('markdown类型：%s' % data)
        return self.__post(data)

    def __post(self, data):
        """
        发送消息（内容UTF-8编码）
        :param data: 消息数据（字典）
        :return: 返回发送结果
        """
        self.times += 1
        if self.times > 20:
            if time.time() - self.start_time < 60:
                logging.debug('钉钉官方限制每个机器人每分钟最多发送20条，当前消息发送频率已达到限制条件，休眠一分钟')
                time.sleep(60)
            self.start_time = time.time()

        post_data = json.dumps(data)
        try:
            response = requests.post(self.__spliceUrl(), headers=self.headers, data=post_data)
        except requests.exceptions.HTTPError as exc:
            logging.error("消息发送失败， HTTP error: %d, reason: %s" % (exc.response.status_code, exc.response.reason))
            raise
        except requests.exceptions.ConnectionError:
            logging.error("消息发送失败，HTTP connection error!")
            raise
        except requests.exceptions.Timeout:
            logging.error("消息发送失败，Timeout error!")
            raise
        except requests.exceptions.RequestException:
            logging.error("消息发送失败, Request Exception!")
            raise
        else:
            try:
                result = response.json()
            except JSONDecodeError:
                logging.error("服务器响应异常，状态码：%s，响应内容：%s" % (response.status_code, response.text))
                return {'errcode': 500, 'errmsg': '服务器响应异常'}
            else:
                logging.debug('发送结果：%s' % result)
                if result['errcode']:
                    error_data = {"msgtype": "text", "text": {"content": "钉钉机器人消息发送失败，原因：%s" % result['errmsg']},
                                  "at": {"isAtAll": True}}
                    logging.error("消息发送失败，自动通知：%s" % error_data)
                    requests.post(self.webhook, headers=self.headers, data=json.dumps(error_data))
                return result


def alidingcheck(filename, cur_time, test_name, title="巡检异常预警"):
    url = "http://172.16.26.119:6851/data/picture/162461447116295.png"
    text = "本次在运行测试用例test_morderpage时探针检测失败判定页面打开失败,截图如下![screenshot](http://qwugfk1sd.hn-bkt.clouddn.com/162729218850966.png)"
    DingtalkRobot().send_markdown(title, text, [])




if __name__ == '__main__':
    URL = "162193303881437.png"
    cur_time = ''
    alidingcheck(URL, cur_time=cur_time,test_name="不告诉你")
