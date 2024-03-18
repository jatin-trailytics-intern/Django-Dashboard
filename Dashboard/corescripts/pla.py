import requests
import pandas as pd
import json
# from channel import *


def payloadpla(cookie_dict={}, start_date='2024-03-03', end_date='2024-03-09'):
    cookies_x = {
        'K-ACTION': 'null',
        'T': 'clsdgcjg102e71tblx48b935i-BR1707410870641',
        'vh': '730',
        'vw': '1536',
        'dpr': '1.25',
        '_pxvid': 'ce5590ea-c6a1-11ee-a41f-4a9ea3aa8784',
        'rt': 'null',
        'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MTE0NDE4NjgsImlhdCI6MTcwOTcxMzg2OCwiaXNzIjoia2V2bGFyIiwianRpIjoiOThmZjRkNDItZTRkOC00MGZhLTgwMzYtNjU3ZDJmYmE3YTY5IiwidHlwZSI6IkFUIiwiZElkIjoiY2xzZGdjamcxMDJlNzF0Ymx4NDhiOTM1aS1CUjE3MDc0MTA4NzA2NDEiLCJrZXZJZCI6IlZJMjU4M0ZCNTI5MjMzNDIwRTkxQUNDNzZGMjlGN0MyNjUiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.Wc8fXpEJNqwmc_Xktga9JONuZlRUJbfq2_I-KVxNooQ',
        'ud': '8.icdr18KS5w96Lsef0YQs0y5hjbQU2IMrj8lquWttKVwzoxfl8H42sVAB4Vs4VthM_udyzZsGQjjzYww8is3I-_fApniJPIPfz-jkxwhV5ZcAY4fzvEYBhoHOM5v1ZVtzqqDV5QDNre4wggVzyfcYHI3z4FA33cfkK6t__x5IOtWYb1dC6s8LVQH1vXDE5307zF_8VEL-yReCqZWnqdF6hQ',
        'DID': 'cltgvjc8p49ki0x2z0drtpwzl',
        '_ga': 'GA1.1.601601622.1709794569',
        'CURRENT_TENANT': 'BSS',
        'vd': 'VI2583FB529233420E91ACC76F29F7C265-1707410876561-10.1709882471.1709882471.155547531',
        'Network-Type': '4g',
        's_cc': 'true',
        'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
        'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19791%7CMCMID%7C25200924767558710411459620755726899807%7CMCAID%7CNONE%7CMCOPTOUT-1709889673s%7CNONE%7CMCAAMLH-1710318670%7C12%7CMCAAMB-1710487273%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y',
        'pxcts': '7923805c-dd1c-11ee-846e-f9ca1fffeeb5',
        'S': 'd1t18PwM/bj9YPz8/MD8/Pz8/Yeg1a+1i1Su5U7svSOiyHL4eLnGli7PlmFCU126PSb7cPSHilkNGbfR7fxwRp01oDA==',
        'SN': 'VI2583FB529233420E91ACC76F29F7C265.TOK283DC0EBD85648CFA4DD642A96D9D81B.1709882472.LO',
        '_csrf': 'PjkYvvnoPuPIZSpOlrbnxtMl',
        'TENANT': 'BSS',
        'BSS_SID': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA1MGRjYzRjLTE0MGYtNDNkYy1iYTUzLTM2NTY3MTQ3MWVlZSJ9.eyJleHAiOjE3MDk4OTMyNzcsImlhdCI6MTcwOTg5MTQ3NywiaXNzIjoia2V2bGFyIiwianRpIjoiMjMwN2IzYTgtNmJkYy00NTk1LWFhMTYtZjM3ZjcyYjY1M2JiIiwidHlwZSI6IkFUIiwiZElkIjoiY2x0Z3ZqYzhwNDlraTB4MnowZHJ0cHd6bCIsImJJZCI6IlhGNzROWiIsImtldklkIjoiVklBMEU1REMzNDYxNTI0NEQ1OEQ4RTEzNUI3ODY5OEE2NyIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEelFjYkRsbnItWWJIaUhZVUpvT2JpdnNPUHk0bUhuOER6c2xLRkxYeUZsMTB0X3RweVdubmc9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.XgltnTv0HBiVOicGs9vseA-WdfsCXyEVc8XjUpqkWLs',
        'BSS_UDT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcwOTg5MTQ3NywiZXhwIjoxNzA5ODkyMDc3fQ.0mBqKfYc8qU-mWp9RdELjWG_mZGYmZjkVSuLbqBOxiI',
        '_ga_ZPGRNTNNRT': 'GS1.1.1709888651.7.1.1709891477.0.0.0',
        'nonce': 'ss-1691208520',
    }


    for key in cookie_dict.keys():
        if key in cookies_x:
            cookies_x[key] = cookie_dict[key]

    headers = {
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Connection': 'keep-alive',
        # 'Cookie': 'K-ACTION=null; T=clsdgcjg102e71tblx48b935i-BR1707410870641; vh=730; vw=1536; dpr=1.25; _pxvid=ce5590ea-c6a1-11ee-a41f-4a9ea3aa8784; rt=null; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MTE0NDE4NjgsImlhdCI6MTcwOTcxMzg2OCwiaXNzIjoia2V2bGFyIiwianRpIjoiOThmZjRkNDItZTRkOC00MGZhLTgwMzYtNjU3ZDJmYmE3YTY5IiwidHlwZSI6IkFUIiwiZElkIjoiY2xzZGdjamcxMDJlNzF0Ymx4NDhiOTM1aS1CUjE3MDc0MTA4NzA2NDEiLCJrZXZJZCI6IlZJMjU4M0ZCNTI5MjMzNDIwRTkxQUNDNzZGMjlGN0MyNjUiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.Wc8fXpEJNqwmc_Xktga9JONuZlRUJbfq2_I-KVxNooQ; ud=8.icdr18KS5w96Lsef0YQs0y5hjbQU2IMrj8lquWttKVwzoxfl8H42sVAB4Vs4VthM_udyzZsGQjjzYww8is3I-_fApniJPIPfz-jkxwhV5ZcAY4fzvEYBhoHOM5v1ZVtzqqDV5QDNre4wggVzyfcYHI3z4FA33cfkK6t__x5IOtWYb1dC6s8LVQH1vXDE5307zF_8VEL-yReCqZWnqdF6hQ; DID=cltgvjc8p49ki0x2z0drtpwzl; _ga=GA1.1.601601622.1709794569; CURRENT_TENANT=BSS; vd=VI2583FB529233420E91ACC76F29F7C265-1707410876561-10.1709882471.1709882471.155547531; Network-Type=4g; s_cc=true; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19791%7CMCMID%7C25200924767558710411459620755726899807%7CMCAID%7CNONE%7CMCOPTOUT-1709889673s%7CNONE%7CMCAAMLH-1710318670%7C12%7CMCAAMB-1710487273%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y; pxcts=7923805c-dd1c-11ee-846e-f9ca1fffeeb5; S=d1t18PwM/bj9YPz8/MD8/Pz8/Yeg1a+1i1Su5U7svSOiyHL4eLnGli7PlmFCU126PSb7cPSHilkNGbfR7fxwRp01oDA==; SN=VI2583FB529233420E91ACC76F29F7C265.TOK283DC0EBD85648CFA4DD642A96D9D81B.1709882472.LO; _csrf=PjkYvvnoPuPIZSpOlrbnxtMl; TENANT=BSS; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA1MGRjYzRjLTE0MGYtNDNkYy1iYTUzLTM2NTY3MTQ3MWVlZSJ9.eyJleHAiOjE3MDk4OTMyNzcsImlhdCI6MTcwOTg5MTQ3NywiaXNzIjoia2V2bGFyIiwianRpIjoiMjMwN2IzYTgtNmJkYy00NTk1LWFhMTYtZjM3ZjcyYjY1M2JiIiwidHlwZSI6IkFUIiwiZElkIjoiY2x0Z3ZqYzhwNDlraTB4MnowZHJ0cHd6bCIsImJJZCI6IlhGNzROWiIsImtldklkIjoiVklBMEU1REMzNDYxNTI0NEQ1OEQ4RTEzNUI3ODY5OEE2NyIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEelFjYkRsbnItWWJIaUhZVUpvT2JpdnNPUHk0bUhuOER6c2xLRkxYeUZsMTB0X3RweVdubmc9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.XgltnTv0HBiVOicGs9vseA-WdfsCXyEVc8XjUpqkWLs; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcwOTg5MTQ3NywiZXhwIjoxNzA5ODkyMDc3fQ.0mBqKfYc8qU-mWp9RdELjWG_mZGYmZjkVSuLbqBOxiI; _ga_ZPGRNTNNRT=GS1.1.1709888651.7.1.1709891477.0.0.0; nonce=ss-1691208520',
        'Origin': 'https://advertising.flipkart.com',
        'Referer': 'https://advertising.flipkart.com/ad-account/reports/pla?baccount=N5J3WN87DKC&aaccount=IZJL4R3KCMHR&tab=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'accept': '*/*',
        'apollographql-client-name': 'Flipkart-Ads',
        'apollographql-client-version': '1.0.0',
        'content-type': 'application/json',
        'downlink': '10',
        'dpr': '1.25',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'viewport-width': '852',
        'x-csrf-token': 'U6qi5pbF-7sJBi0Ein44rP3nLrOlEQ2JuLLU',
        'x-pageContext': 'report-dashboard#BRAND_PLA#daily-view#table',
        'x-sourceurl': 'https://advertising.flipkart.com/ad-account/reports/pla?baccount=N5J3WN87DKC&aaccount=IZJL4R3KCMHR&tab=1',
        'x-tenant': 'BSS',
    }

    json_data = {
        'operationName': 'getURFTabularData',
        'variables': {
            'dateRange': {
                'endDate': end_date,
                'startDate': start_date,
            },
            'pageLevelFilter': [
                {
                    'comparator': [
                        'FLIPKART',
                    ],
                    'field': {
                        'entity_type': 'DIMENSION',
                        'function': 'VALUE',
                        'name': 'marketplace',
                    },
                    'operator': 'IN',
                    'view_id': '600',
                },
            ],
            'queries': [
                {
                    'query': {
                        'filters': [
                            {
                                'comparator': [
                                    'IZJL4R3KCMHR',
                                ],
                                'field': {
                                    'entity_type': 'DIMENSION',
                                    'function': 'VALUE',
                                    'name': 'team_id',
                                },
                                'operator': 'IN',
                                'view_id': '600',
                            },
                        ],
                        'group_by': [
                            {
                                'function': 'VALUE',
                                'name': 'date',
                            },
                        ],
                        'metrics': [
                            {
                                'function': 'SUM',
                                'name': 'views',
                            },
                            {
                                'function': 'SUM',
                                'name': 'engagements',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'ctr',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'cvr',
                            },
                            {
                                'function': 'SUM',
                                'name': 'cost',
                            },
                            {
                                'function': 'SUM',
                                'name': 'direct_converted_units',
                            },
                            {
                                'function': 'SUM',
                                'name': 'indirectly_converted_units',
                            },
                            {
                                'function': 'SUM',
                                'name': 'direct_revenue',
                            },
                            {
                                'function': 'SUM',
                                'name': 'indirect_revenue',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'direct_roi',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'indirect_roi',
                            },
                        ],
                        'order_by': {
                            'fields': [
                                {
                                    'entity_type': 'METRIC',
                                    'function': 'SUM',
                                    'name': 'views',
                                },
                            ],
                            'type': 'DESC',
                        },
                        'page_size': 50,
                        'type': 'TABULAR',
                        'view_id': '600',
                    },
                    'queryId': 'tabular-pfTableCampaignDailyViewV2e0sm7yj5e2w',
                },
            ],
            'requestId': 'pla-tabular-123',
            'timeGranularity': 'DAY',
        },
        'query': 'query getURFTabularData($dateRange: URFDateRange, $timeGranularity: String, $requestId: String, $pageLevelFilter: [URFFilter], $queries: [URFQuerySet]) {\n  getURFTabularData(dateRange: $dateRange, timeGranularity: $timeGranularity, requestId: $requestId, pageLevelFilter: $pageLevelFilter, queries: $queries) {\n    queryId\n    data {\n      code\n      columns {\n        entityType\n        name\n        type\n        metadata {\n          HAS_MULTISOURCE\n          __typename\n        }\n        __typename\n      }\n      rows {\n        values\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
    }

    response = requests.post('https://advertising.flipkart.com/api', cookies=cookies_x, headers=headers, json=json_data)
    if response.status_code == 200:
        x = json.loads(response.text)
        rows = x.get("data", {}).get("getURFTabularData")[0].get('data').get("rows")
        columns = x.get("data", {}).get("getURFTabularData")[0].get("data").get("columns")

        column = []
        for i in columns:
            column.append(i["name"])
        df = pd.DataFrame(columns=column)
        for i in rows:
            new_row = i["values"]
            df.loc[len(df)] = new_row    
        # print(df)
        # print(df.to_dict())
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date')
        df['date'] = df['date'].dt.strftime('%Y-%m-%d')
        data = {}
        data['date'] = df['date'].values.tolist()
        data['ads_pend'] = df['SUM(cost)'].values.tolist()
        data['impressions'] = df['SUM(views)'].values.tolist()
        data['clicks'] = df['SUM(engagements)'].values.tolist()
        data['ctr'] = df['ctr'].values.tolist()
        data['cdcu'] = df['SUM(direct_converted_units)'].values.tolist()
        data['cicu'] = df['SUM(indirectly_converted_units)'].values.tolist()
        data['cvr'] = df['cvr'].values.tolist()
        data['cdcr'] = df['SUM(direct_revenue)'].values.tolist()
        data['cicr'] = df['SUM(indirect_revenue)'].values.tolist()
        data['roi'] = df['indirect_roi'].values.tolist()
        b = df['direct_roi'].values.tolist()
        # data['roi'] = [1/float(i)+float(j) if (i!=0 and j!=0) else 0 for i, j in zip(a,b)]

        # print(data)
        return data
    
    else:
        print("some error occure")
        return None




# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"operationName":"getURFTabularData","variables":{"dateRange":{"endDate":"2024-03-02","startDate":"2024-02-25"},"pageLevelFilter":[{"comparator":["FLIPKART"],"field":{"entity_type":"DIMENSION","function":"VALUE","name":"marketplace"},"operator":"IN","view_id":"600"}],"queries":[{"query":{"filters":[{"comparator":["IZJL4R3KCMHR"],"field":{"entity_type":"DIMENSION","function":"VALUE","name":"team_id"},"operator":"IN","view_id":"600"}],"group_by":[{"function":"VALUE","name":"date"}],"metrics":[{"function":"SUM","name":"views"},{"function":"SUM","name":"engagements"},{"function":"VALUE","name":"ctr"},{"function":"VALUE","name":"cvr"},{"function":"SUM","name":"cost"},{"function":"SUM","name":"direct_converted_units"},{"function":"SUM","name":"indirectly_converted_units"},{"function":"SUM","name":"direct_revenue"},{"function":"SUM","name":"indirect_revenue"},{"function":"VALUE","name":"direct_roi"},{"function":"VALUE","name":"indirect_roi"}],"order_by":{"fields":[{"entity_type":"METRIC","function":"SUM","name":"views"}],"type":"DESC"},"page_size":50,"type":"TABULAR","view_id":"600"},"queryId":"tabular-pfTableCampaignDailyViewV2e0sm7yj5e2w"}],"requestId":"pla-tabular-123","timeGranularity":"DAY"},"query":"query getURFTabularData($dateRange: URFDateRange, $timeGranularity: String, $requestId: String, $pageLevelFilter: [URFFilter], $queries: [URFQuerySet]) {\\n  getURFTabularData(dateRange: $dateRange, timeGranularity: $timeGranularity, requestId: $requestId, pageLevelFilter: $pageLevelFilter, queries: $queries) {\\n    queryId\\n    data {\\n      code\\n      columns {\\n        entityType\\n        name\\n        type\\n        metadata {\\n          HAS_MULTISOURCE\\n          __typename\\n        }\\n        __typename\\n      }\\n      rows {\\n        values\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'
#response = requests.post('https://advertising.flipkart.com/api', cookies=cookies, headers=headers, data=data)


# payloadpla(cookie_generator()[0])


