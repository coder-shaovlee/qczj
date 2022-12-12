import requests


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
    "x-zse-96": "2.0_bXC+Tt/PQ7xgt7zewidy0zYM=eLOLfD3fDSpDVjmgV23o6tRqS7g5/78MuI0bZ2i",
    "x-zst-81": ""
}
cookies = {
    "d_c0": "APCWCOaOlxWPTrbtbeaa731M6VLwSMsxhB4=|1663728151",
}
url = "https://www.zhihu.com/api/v3/moments/mei-ri-jing-ji-xin-wen/activities"
params = {
    "limit": "5",
    "desktop": "true"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)