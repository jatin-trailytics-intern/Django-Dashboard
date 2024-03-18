import requests
import json

def cookie_generator():
    cookies = {
        '_csrf': '-QlSRpfa7b8_G_tIr-rAzIWR',
    }
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'apollographql-client-name': 'Flipkart-Ads',
        'x-csrf-token': 'w1qiG7Nm--Tbq5z42RXqHDbzCPd4YQ3P2l-E',
        'x-sourceurl': 'https://advertising.flipkart.com/login?tenant=BSS',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'viewport-width': '1536',
        'content-type': 'application/json',
        'accept': '*/*',
        'apollographql-client-version': '1.0.0',
        'dpr': '1.25',
        'downlink': '10',
        'x-tenant': 'BSS',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://advertising.flipkart.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://advertising.flipkart.com/login?tenant=BSS',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    json_data = {
        'operationName': 'LoginUser',
        'variables': {
            'password': 'blessings@guruji123',
            'userLoginId': 'Marketplaces@bellavitaorganic.com',
        },
        'query': 'mutation LoginUser($userLoginId: String!, $password: String!) {\n  loginUser(userLoginId: $userLoginId, password: $password) {\n    email\n    state\n    mobile\n    firstName\n    success\n    __typename\n  }\n}\n',
    }



    response = requests.post('https://advertising.flipkart.com/api', cookies=cookies, headers=headers, json=json_data)
    cookies = response.cookies
    cookie_dict = {}
    for cookie in cookies:
        cookie_dict[cookie.name] = cookie.value

# # for key, value in cookie_dict.items():
#     # print(f"'{key}': '{value}'")
    print(response.status_code)
    return (cookie_dict, response.status_code)



# print(cookie_generator()[0])













