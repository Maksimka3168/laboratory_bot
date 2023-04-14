import json

import requests


def get_joke():
    cookies = {
        '_ym_uid': '168042844890340461',
        '_ym_d': '1680428448',
        '_ym_isad': '1',
        'PHPSESSID': 'b2ebbeaedf582a812151f951afba75dc',
    }

    headers = {
        'authority': 'generatom.com',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ym_uid=168042844890340461; _ym_d=1680428448; _ym_isad=1; PHPSESSID=b2ebbeaedf582a812151f951afba75dc',
        'origin': 'https://generatom.com',
        'referer': 'https://generatom.com/joke',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.0.2246 Yowser/2.5 Safari/537.36',
    }

    data = {
        'type': 'joke',
        'count': '1',
    }

    response = requests.post('https://generatom.com/ajax/main', cookies=cookies, headers=headers, data=data)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

