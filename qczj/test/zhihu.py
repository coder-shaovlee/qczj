import hashlib
import execjs
import requests


if __name__ == '__main__':
    url = 'https://www.zhihu.com/api/v4/search_v3?gk_version=gz-gaokao&t=general&q=%E5%8C%97%E4%BA%AC&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal'
    path = url.replace('https://www.zhihu.com', '')
    m = hashlib.md5()
    s = f"101_3_3.0+{path}+AWCYZmrv-hWPTnJlJaXYb_qaemAtmqcp7zc=|1670397230"
    m.update(s.encode())
    md5s = m.hexdigest()
    print(md5s)
    with open('zhihu.js', encoding='utf-8') as p:
        js_code = p.read()
    ctx = execjs.compile(js_code)
    xzse96 = '2.0_'+ctx.call('D', md5s)
    print(xzse96)
    print(url)
    headers = {
        "authority": "www.zhihu.com",
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "x-api-version": "3.0.40",
        "x-zse-93": "101_3_3.0",
        "x-zse-96": xzse96,
        "referer": "https://www.zhihu.com/search?type=content&q=%E5%8C%97%E4%BA%AC",
        "cookie": "AWCYZmrv-hWPTnJlJaXYb_qaemAtmqcp7zc=|1670397230"
    }
    res = requests.get(url=url, headers=headers)
    print(res.json())