import urllib.request
import urllib.parse
import json

while True:
    content = input("请输入需要翻译的内容：")
    if content == 'q!':
        break
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link"
    '''
    head={}
    head ['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
    '''
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = "1.8"
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typeResult'] = 'true'

    data = urllib.parse.urlencode(data).encode('utf-8')
    print("data is: %s"%data)
    req = urllib.request.Request(url,data)
    print("req is: %s"%req)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    print("html is: %s"%html)
    target = json.loads(html)
    transresult = target['translateResult'][0][0]['tgt']
    print(transresult)