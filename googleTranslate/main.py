#!/usr/bin/python3
import requests
import execjs
import argparse
from tk import tk
from urllib.parse import urlencode
class ExecJs:
    def __init__(self):
        self.tk = execjs.compile(tk)
    def get_tk(self,str):
        return self.tk.call('ru', str)


class GoogleTranslate(ExecJs):

    def __init__(self):
        """
        text: word we will to translate
        to_language: which language we want to translate
        native: which language we use
        """
        super(GoogleTranslate, self).__init__()
        self.text = "hello"
        self.foreign = "zh-CN"
        self.native = "auto"
        self.tkv = ""
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
            'referer': 'https://translate.google.cn/'
        }
        self.__params = {
            'client': 'webapp',
            'sl': self.native,
            'hl': 'zh-CN',
            'dt': 'at',
            'dt': 'bd',
            'dt': 'ex',
            'dt': 'ld',
            'dt': 'md',
            'dt': 'qca',
            'dt': 'rw',
            'dt': 'rm',
            'dt': 'sos',
            'dt': 'ss',
            'dt': 't',
            'otf': '2',
            'ssel': '0',
            'tsel': '0',
            'kc': '1'
        }

    def get_url(self,url):
        """
        :param url: request url
        :return:
        """
        data = requests.get(url=url, headers=self.__headers)
        # print(data.text)
        return data
    def build_url(self):
        """
        build our request url
        :return:
        """
        base_url = self.__headers.get('referer')+'translate_a/single?'
        object_url = base_url+urlencode(self.__params)
        return object_url
    def translate(self, text, foreign='zh-CN', native='auto'):
        """
        text: word we will to translate
        to_language: which language we want to translate
        native: which language we use
        """

        self.__params['tl'] = foreign
        self.tkv = self.get_tk(text)
        self.__params['tk'] = self.tkv.split('=')[-1]
        self.__params['q'] = text

        url = self.build_url()
        _result = self.get_url(url)
        data = _result.content.decode('utf-8')
        end = data.find("\",")
        if end > 4:
            return data[4:end]
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--text", help="要翻译的语句")
    parser.add_argument("-l", "--language", help="翻译目标语言")
    args = parser.parse_args()
    text = args.text
    lan = args.language
    ts = GoogleTranslate()

    print(ts.translate(text, foreign=lan))
