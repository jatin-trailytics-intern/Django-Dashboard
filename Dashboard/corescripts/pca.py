import json
import pandas as pd
import requests
import datetime as DT




def payloadpca(cookie_dict={}, start_date="2023-03-01", end_date="2023-03-12"):
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
        'BSS_SID': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MDk4OTA5NTUsImlhdCI6MTcwOTg4OTE1NSwiaXNzIjoia2V2bGFyIiwianRpIjoiNzY1MzI5ZGItNDRjZS00MDYyLWI1Y2MtMjkyNTI2OGNkOTE0IiwidHlwZSI6IkFUIiwiZElkIjoiY2x0Z3ZqYzhwNDlraTB4MnowZHJ0cHd6bCIsImJJZCI6IkFaQ0NaTiIsImtldklkIjoiVklBMEU1REMzNDYxNTI0NEQ1OEQ4RTEzNUI3ODY5OEE2NyIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.E3bk6a12texAJD_ClHFMQ0lD1iqI1hLDQAd7kI1GhxM',
        'BSS_UDT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcwOTg4OTUwMiwiZXhwIjoxNzA5ODkwMTAyfQ.9UprXNk2fcb8QCddUNJySng3TZbScCcKJntZg1k214c',
        '_ga_ZPGRNTNNRT': 'GS1.1.1709888651.7.1.1709889944.0.0.0',
        'nonce': 'ss-2336983472',
    }


    for key in cookie_dict.keys():
        if key in cookies_x:
            cookies_x[key] = cookie_dict[key]


    headers = {
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Connection': 'keep-alive',
        # 'Cookie': 'K-ACTION=null; T=clsdgcjg102e71tblx48b935i-BR1707410870641; vh=730; vw=1536; dpr=1.25; _pxvid=ce5590ea-c6a1-11ee-a41f-4a9ea3aa8784; rt=null; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MTE0NDE4NjgsImlhdCI6MTcwOTcxMzg2OCwiaXNzIjoia2V2bGFyIiwianRpIjoiOThmZjRkNDItZTRkOC00MGZhLTgwMzYtNjU3ZDJmYmE3YTY5IiwidHlwZSI6IkFUIiwiZElkIjoiY2xzZGdjamcxMDJlNzF0Ymx4NDhiOTM1aS1CUjE3MDc0MTA4NzA2NDEiLCJrZXZJZCI6IlZJMjU4M0ZCNTI5MjMzNDIwRTkxQUNDNzZGMjlGN0MyNjUiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.Wc8fXpEJNqwmc_Xktga9JONuZlRUJbfq2_I-KVxNooQ; ud=8.icdr18KS5w96Lsef0YQs0y5hjbQU2IMrj8lquWttKVwzoxfl8H42sVAB4Vs4VthM_udyzZsGQjjzYww8is3I-_fApniJPIPfz-jkxwhV5ZcAY4fzvEYBhoHOM5v1ZVtzqqDV5QDNre4wggVzyfcYHI3z4FA33cfkK6t__x5IOtWYb1dC6s8LVQH1vXDE5307zF_8VEL-yReCqZWnqdF6hQ; DID=cltgvjc8p49ki0x2z0drtpwzl; _ga=GA1.1.601601622.1709794569; CURRENT_TENANT=BSS; vd=VI2583FB529233420E91ACC76F29F7C265-1707410876561-10.1709882471.1709882471.155547531; Network-Type=4g; s_cc=true; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19791%7CMCMID%7C25200924767558710411459620755726899807%7CMCAID%7CNONE%7CMCOPTOUT-1709889673s%7CNONE%7CMCAAMLH-1710318670%7C12%7CMCAAMB-1710487273%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y; pxcts=7923805c-dd1c-11ee-846e-f9ca1fffeeb5; S=d1t18PwM/bj9YPz8/MD8/Pz8/Yeg1a+1i1Su5U7svSOiyHL4eLnGli7PlmFCU126PSb7cPSHilkNGbfR7fxwRp01oDA==; SN=VI2583FB529233420E91ACC76F29F7C265.TOK283DC0EBD85648CFA4DD642A96D9D81B.1709882472.LO; _csrf=PjkYvvnoPuPIZSpOlrbnxtMl; TENANT=BSS; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MDk4OTA5NTUsImlhdCI6MTcwOTg4OTE1NSwiaXNzIjoia2V2bGFyIiwianRpIjoiNzY1MzI5ZGItNDRjZS00MDYyLWI1Y2MtMjkyNTI2OGNkOTE0IiwidHlwZSI6IkFUIiwiZElkIjoiY2x0Z3ZqYzhwNDlraTB4MnowZHJ0cHd6bCIsImJJZCI6IkFaQ0NaTiIsImtldklkIjoiVklBMEU1REMzNDYxNTI0NEQ1OEQ4RTEzNUI3ODY5OEE2NyIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.E3bk6a12texAJD_ClHFMQ0lD1iqI1hLDQAd7kI1GhxM; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcwOTg4OTUwMiwiZXhwIjoxNzA5ODkwMTAyfQ.9UprXNk2fcb8QCddUNJySng3TZbScCcKJntZg1k214c; _ga_ZPGRNTNNRT=GS1.1.1709888651.7.1.1709889944.0.0.0; nonce=ss-2336983472',
        'Origin': 'https://advertising.flipkart.com',
        'Referer': 'https://advertising.flipkart.com/ad-account/reports/pca?baccount=N5J3WN87DKC&aaccount=IZJL4R3KCMHR&tab=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'accept': '*/*',
        'apollographql-client-name': 'Flipkart-Ads',
        'apollographql-client-version': '1.0.0',
        'content-type': 'application/json',
        'downlink': '7.7',
        'dpr': '1.25',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'viewport-width': '852',
        'x-csrf-token': 'jARk8fQi-BBhdtA7-eiPL1Nr_RR-fl1OjNFk',
        'x-pageContext': 'report-dashboard#BRAND_PCA#daily-view#table',
        'x-sourceurl': 'https://advertising.flipkart.com/ad-account/reports/pca?baccount=N5J3WN87DKC&aaccount=IZJL4R3KCMHR&tab=1',
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
                        'BRAND_PCA',
                    ],
                    'field': {
                        'entity_type': 'DIMENSION',
                        'function': 'VALUE',
                        'name': 'campaign_type',
                    },
                    'operator': 'IN',
                    'view_id': '603',
                },
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
                    'view_id': '603',
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
                                    'name': 'advertiser_id',
                                },
                                'operator': 'IN',
                                'view_id': '603',
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
                                'function': 'VALUE',
                                'name': 'advertiser_spend',
                            },
                            {
                                'function': 'SUM',
                                'name': 'views',
                            },
                            {
                                'function': 'SUM',
                                'name': 'clicks',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'CTR',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'average_cpc',
                            },
                            {
                                'function': 'SUM',
                                'name': 'click_direct_converted_ppv',
                            },
                            {
                                'function': 'SUM',
                                'name': 'click_direct_converted_units',
                            },
                            {
                                'function': 'SUM',
                                'name': 'click_indirect_converted_units',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'CVR',
                            },
                            {
                                'function': 'SUM',
                                'name': 'click_direct_converted_revenue',
                            },
                            {
                                'function': 'SUM',
                                'name': 'click_indirect_converted_revenue',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'click_direct_roi',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'click_indirect_roi',
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
                        'view_id': '603',
                    },
                    'queryId': 'tabular-pfTableCampaignDailyVieww7jbolp99mb',
                },
            ],
            'requestId': 'pca-tabular-123',
            'timeGranularity': 'DAY',
        },
        'query': 'query getURFTabularData($dateRange: URFDateRange, $timeGranularity: String, $requestId: String, $pageLevelFilter: [URFFilter], $queries: [URFQuerySet]) {\n  getURFTabularData(dateRange: $dateRange, timeGranularity: $timeGranularity, requestId: $requestId, pageLevelFilter: $pageLevelFilter, queries: $queries) {\n    queryId\n    data {\n      code\n      columns {\n        entityType\n        name\n        type\n        metadata {\n          HAS_MULTISOURCE\n          __typename\n        }\n        __typename\n      }\n      rows {\n        values\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
    }

    response = requests.post('https://advertising.flipkart.com/api', cookies=cookies_x, headers=headers, json=json_data)
    if response.status_code ==200:
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
        

        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date')
        df['date'] = df['date'].dt.strftime('%Y-%m-%d')
        data = {}
        data['date'] = df['date'].values.tolist()
        data['ads_spend'] = df['advertiser_spend'].values.tolist()
        data['impressions'] = df['SUM(views)'].values.tolist()
        data['clicks'] = df['SUM(clicks)'].values.tolist()
        data['ctr'] = df['CTR'].values.tolist()
        data['cdcu'] = df['SUM(click_direct_converted_units)'].values.tolist()
        data['cicu'] = df['SUM(click_indirect_converted_units)'].values.tolist()
        data['cvr'] = df['CVR'].values.tolist()
        data['cdcr'] = df['SUM(click_direct_converted_revenue)'].values.tolist()
        data['cicr'] = df['SUM(click_indirect_converted_revenue)'].values.tolist()
        a = df['click_direct_roi'].values.tolist()
        b = df['click_indirect_roi'].values.tolist()
        data['roi'] = [1/float(i)+float(j) for i, j in zip(a,b)]
        return data
    

    else:
        print("some error occure")
        return None


# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"operationName":"getURFTabularData","variables":{"dateRange":{"endDate":"2024-03-02","startDate":"2024-02-25"},"pageLevelFilter":[{"comparator":["BRAND_PCA"],"field":{"entity_type":"DIMENSION","function":"VALUE","name":"campaign_type"},"operator":"IN","view_id":"603"},{"comparator":["FLIPKART"],"field":{"entity_type":"DIMENSION","function":"VALUE","name":"marketplace"},"operator":"IN","view_id":"603"}],"queries":[{"query":{"filters":[{"comparator":["IZJL4R3KCMHR"],"field":{"entity_type":"DIMENSION","function":"VALUE","name":"advertiser_id"},"operator":"IN","view_id":"603"}],"group_by":[{"function":"VALUE","name":"date"}],"metrics":[{"function":"VALUE","name":"advertiser_spend"},{"function":"SUM","name":"views"},{"function":"SUM","name":"clicks"},{"function":"VALUE","name":"CTR"},{"function":"VALUE","name":"average_cpc"},{"function":"SUM","name":"click_direct_converted_ppv"},{"function":"SUM","name":"click_direct_converted_units"},{"function":"SUM","name":"click_indirect_converted_units"},{"function":"VALUE","name":"CVR"},{"function":"SUM","name":"click_direct_converted_revenue"},{"function":"SUM","name":"click_indirect_converted_revenue"},{"function":"VALUE","name":"click_direct_roi"},{"function":"VALUE","name":"click_indirect_roi"}],"order_by":{"fields":[{"entity_type":"METRIC","function":"SUM","name":"views"}],"type":"DESC"},"page_size":50,"type":"TABULAR","view_id":"603"},"queryId":"tabular-pfTableCampaignDailyVieww7jbolp99mb"}],"requestId":"pca-tabular-123","timeGranularity":"DAY"},"query":"query getURFTabularData($dateRange: URFDateRange, $timeGranularity: String, $requestId: String, $pageLevelFilter: [URFFilter], $queries: [URFQuerySet]) {\\n  getURFTabularData(dateRange: $dateRange, timeGranularity: $timeGranularity, requestId: $requestId, pageLevelFilter: $pageLevelFilter, queries: $queries) {\\n    queryId\\n    data {\\n      code\\n      columns {\\n        entityType\\n        name\\n        type\\n        metadata {\\n          HAS_MULTISOURCE\\n          __typename\\n        }\\n        __typename\\n      }\\n      rows {\\n        values\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'
#response = requests.post('https://advertising.flipkart.com/api', cookies=cookies, headers=headers, data=data)


# print(payloadpca(cookie_generator()[0]))