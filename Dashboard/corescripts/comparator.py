import requests
from channel import *

def dateload(cookie_dict={}):
    cookies_x = {
    'T': 'TI169891842149300161944937865135939588577615020537527148270186391420',
    '_pxvid': 'c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0',
    'dpr': '1.25',
    '_fbp': 'fb.1.1700471257731.638459595',
    '_ga_B9RGC9GN63': 'GS1.1.1702722512.1.1.1702722682.54.0.0',
    'DID': 'clr1pup252bqp0x0wejpe1ajo',
    'ULSN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw',
    'ud': '7.FKluYsbjMSc0eLZOxg8QnowhzVZwLF7DV8Krb7TrukAYp-sew-t8uSo4wvYhTU_A56AyHK9B91iv9CQ8gsvGss9XYeRVB336vXnyYf2BWu6qOPEhW6PTgknyWlVk6t40zDBZqI_ghooutPdUhuHTQJq2aw5ZW1CfxOStGBkySf34cmST4cOWDvrCJoVFGjNKV4Oeiq4GSw-7yRllRJy868MzI1TQODRX6bwTZ9xx2c2jtSf9lZbO31CbwUyIpc3L_syjKcKQqciGn8TmYT0vi3fApsx3PSyWNBBQ4-mvSCrhtl0Gr9yGY-PbyD4ZAzOKvwrsmemKIhhsRlR-KuIIQ9aDmI3aEVVxXa8XcEmMWVMnc1J9PdzjkATofj4vC2kObv8FGfpyWXqlDVBo0IRoxMkZiPx6XB-7OczT38AWuXjzu6xLD-xm7mpw3AUrVSaqz-fy2hqD_SFl8AMqUCcyacRVODNAeCidDpCkug9Ix1hEMw9HiSFBZH0yWixwMf9M54a4-aRjGfh3_4yqq16khnPa3KGtxPYKjugscH4TazwEDnuqr359GBQmfwDym0btFkGqqPj8Udm-dCQbeM2VosOeLxpW0Ef1F0Cl7Ur8inaN0JcvwfoPDvAJ4p9R82naZmPaz_ndA_2g-qiiR0n7Vs6PMX3tybk7PV4Nj9V2b4ZkIhKrwDQHxkl42_VDAIObvbVV_wrxZ28OsbG0Qx6Aa5HQtV6TSpSfRTl_zsqV7G5yJ2QrCZllRWM7Q9K1GVpJ1IAXtAp8Z2JTA8NIW3eltQ',
    'vh': '730',
    'vw': '1536',
    'K-ACTION': 'null',
    '_ga_0RGM1K38MN': 'GS1.2.1708195526.2.1.1708195657.0.0.0',
    '_ga_C00F4Q43Q7': 'GS1.2.1708196044.1.0.1708196044.0.0.0',
    '_ga_2P94RMW04V': 'GS1.2.1708196121.6.1.1708196143.0.0.0',
    '_gcl_au': '1.1.856723108.1708257205',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19774%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1709028912%7C7%7CMCAAMB-1709028912%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1708431312s%7CNONE%7CMCAID%7CNONE',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MDg1Mzc1MjgsImlhdCI6MTcwODUzNTcyOCwiaXNzIjoia2V2bGFyIiwianRpIjoiNWRjNDU2NmUtOWEzNC00ZTFmLTk3OWUtYWM3MDNlZDVkZWJlIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJWWkJJT1IiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImJlMHVRSWdQSVRwMlpxYW5OTmhobkdIamhSdi1QMVhOTmNURnloQS16QVNBWU40QlZ2NF9Odz09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.ixhU35LmpE--LWxH_Tug5UsoH3uDNKS2NL5j3y6MwTA',
    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MjQyNjA1MjgsImlhdCI6MTcwODUzNTcyOCwiaXNzIjoia2V2bGFyIiwianRpIjoiYjY0ZDhmOTItOTcyMS00MDY3LWI4OGMtNmJiM2MyZDk5NzFhIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJWWkJJT1IiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiTlpTRkYwIn0.g2hkK6c7Q2c7MxB1WlaiYX1bWasSlpOdDC7x_gHDlpM',
    'SN': 'VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1708535785.LI',
    'vd': 'VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-13.1708537051.1708535728.162293777',
    'S': 'd1t12emQ/fh4tF1Y/Pz9RQT8/P80KJmhodn6rNULCBJ5uZan0th6BBL1Yefc0o343q0W9YTGUjyenYJfm7VzPZee0sQ==',
    'CURRENT_TENANT': 'BSS',
    'AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg': '-227196251%7CMCIDTS%7C19777%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1708950352%7C7%7CMCAAMB-1709270075%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1708672475s%7CNONE%7CMCAID%7CNONE',
    '_ga_TVF0VCMCT3': 'GS1.1.1708665258.110.1.1708665578.18.0.0',
    '_ga_0SJLGHBL81': 'GS1.1.1708665259.110.1.1708665578.0.0.0',
    's_nr': '1708665578715-Repeat',
    'mp_9ea3bc9a23c575907407cf80efd56524_mixpanel': '%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D',
    '_ga': 'GA1.1.1819741834.1700633034',
    '_csrf': '14lXxdIYF0JgZiWdgYCARY4l',
    'TENANT': 'BSS',
    'BSS_SID': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA1MGRjYzRjLTE0MGYtNDNkYy1iYTUzLTM2NTY3MTQ3MWVlZSJ9.eyJleHAiOjE3MDg3NTcyMDQsImlhdCI6MTcwODc1NTQwNCwiaXNzIjoia2V2bGFyIiwianRpIjoiN2JhZTBhMTEtYmQzZi00MDA1LWJiNDctZjQyYjU1NmVmYTU2IiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IkZGMU1EMCIsImtldklkIjoiVkk2MzIzRkZFQTZCMzc0QjdDOTY0Mzg5NzUxMTlEM0VDNSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEelFjYkRsbnItWWJIaUhZVUpvT2JpdnNPUHk0bUhuOER6c2xLRkxYeUZsMTB0X3RweVdubmc9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.ZuPwURCBcl9JwNNICNhvsgm6Kc58nhL1Ra7i688Ilbo',
    'BSS_UDT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcwODc1NTQwNCwiZXhwIjoxNzA4NzU2MDA0fQ.rAG0OkDpSTsBnZH865imaDQYed_5tRzzjSj7rVuLKf0',
    '_ga_ZPGRNTNNRT': 'GS1.1.1708751713.65.1.1708755415.0.0.0',
    'nonce': 'ss-2451472327',
    }


    for key in cookie_dict.keys():
        if key in cookies_x:
            cookies_x[key] = cookie_dict[key]


    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'T=TI169891842149300161944937865135939588577615020537527148270186391420; _pxvid=c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0; dpr=1.25; _fbp=fb.1.1700471257731.638459595; _ga_B9RGC9GN63=GS1.1.1702722512.1.1.1702722682.54.0.0; DID=clr1pup252bqp0x0wejpe1ajo; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw; ud=7.FKluYsbjMSc0eLZOxg8QnowhzVZwLF7DV8Krb7TrukAYp-sew-t8uSo4wvYhTU_A56AyHK9B91iv9CQ8gsvGss9XYeRVB336vXnyYf2BWu6qOPEhW6PTgknyWlVk6t40zDBZqI_ghooutPdUhuHTQJq2aw5ZW1CfxOStGBkySf34cmST4cOWDvrCJoVFGjNKV4Oeiq4GSw-7yRllRJy868MzI1TQODRX6bwTZ9xx2c2jtSf9lZbO31CbwUyIpc3L_syjKcKQqciGn8TmYT0vi3fApsx3PSyWNBBQ4-mvSCrhtl0Gr9yGY-PbyD4ZAzOKvwrsmemKIhhsRlR-KuIIQ9aDmI3aEVVxXa8XcEmMWVMnc1J9PdzjkATofj4vC2kObv8FGfpyWXqlDVBo0IRoxMkZiPx6XB-7OczT38AWuXjzu6xLD-xm7mpw3AUrVSaqz-fy2hqD_SFl8AMqUCcyacRVODNAeCidDpCkug9Ix1hEMw9HiSFBZH0yWixwMf9M54a4-aRjGfh3_4yqq16khnPa3KGtxPYKjugscH4TazwEDnuqr359GBQmfwDym0btFkGqqPj8Udm-dCQbeM2VosOeLxpW0Ef1F0Cl7Ur8inaN0JcvwfoPDvAJ4p9R82naZmPaz_ndA_2g-qiiR0n7Vs6PMX3tybk7PV4Nj9V2b4ZkIhKrwDQHxkl42_VDAIObvbVV_wrxZ28OsbG0Qx6Aa5HQtV6TSpSfRTl_zsqV7G5yJ2QrCZllRWM7Q9K1GVpJ1IAXtAp8Z2JTA8NIW3eltQ; vh=730; vw=1536; K-ACTION=null; _ga_0RGM1K38MN=GS1.2.1708195526.2.1.1708195657.0.0.0; _ga_C00F4Q43Q7=GS1.2.1708196044.1.0.1708196044.0.0.0; _ga_2P94RMW04V=GS1.2.1708196121.6.1.1708196143.0.0.0; _gcl_au=1.1.856723108.1708257205; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19774%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1709028912%7C7%7CMCAAMB-1709028912%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1708431312s%7CNONE%7CMCAID%7CNONE; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MDg1Mzc1MjgsImlhdCI6MTcwODUzNTcyOCwiaXNzIjoia2V2bGFyIiwianRpIjoiNWRjNDU2NmUtOWEzNC00ZTFmLTk3OWUtYWM3MDNlZDVkZWJlIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJWWkJJT1IiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImJlMHVRSWdQSVRwMlpxYW5OTmhobkdIamhSdi1QMVhOTmNURnloQS16QVNBWU40QlZ2NF9Odz09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.ixhU35LmpE--LWxH_Tug5UsoH3uDNKS2NL5j3y6MwTA; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MjQyNjA1MjgsImlhdCI6MTcwODUzNTcyOCwiaXNzIjoia2V2bGFyIiwianRpIjoiYjY0ZDhmOTItOTcyMS00MDY3LWI4OGMtNmJiM2MyZDk5NzFhIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJWWkJJT1IiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiTlpTRkYwIn0.g2hkK6c7Q2c7MxB1WlaiYX1bWasSlpOdDC7x_gHDlpM; SN=VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1708535785.LI; vd=VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-13.1708537051.1708535728.162293777; S=d1t12emQ/fh4tF1Y/Pz9RQT8/P80KJmhodn6rNULCBJ5uZan0th6BBL1Yefc0o343q0W9YTGUjyenYJfm7VzPZee0sQ==; CURRENT_TENANT=BSS; AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg=-227196251%7CMCIDTS%7C19777%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1708950352%7C7%7CMCAAMB-1709270075%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1708672475s%7CNONE%7CMCAID%7CNONE; _ga_TVF0VCMCT3=GS1.1.1708665258.110.1.1708665578.18.0.0; _ga_0SJLGHBL81=GS1.1.1708665259.110.1.1708665578.0.0.0; s_nr=1708665578715-Repeat; mp_9ea3bc9a23c575907407cf80efd56524_mixpanel=%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D; _ga=GA1.1.1819741834.1700633034; _csrf=14lXxdIYF0JgZiWdgYCARY4l; TENANT=BSS; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA1MGRjYzRjLTE0MGYtNDNkYy1iYTUzLTM2NTY3MTQ3MWVlZSJ9.eyJleHAiOjE3MDg3NTcyMDQsImlhdCI6MTcwODc1NTQwNCwiaXNzIjoia2V2bGFyIiwianRpIjoiN2JhZTBhMTEtYmQzZi00MDA1LWJiNDctZjQyYjU1NmVmYTU2IiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IkZGMU1EMCIsImtldklkIjoiVkk2MzIzRkZFQTZCMzc0QjdDOTY0Mzg5NzUxMTlEM0VDNSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEelFjYkRsbnItWWJIaUhZVUpvT2JpdnNPUHk0bUhuOER6c2xLRkxYeUZsMTB0X3RweVdubmc9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.ZuPwURCBcl9JwNNICNhvsgm6Kc58nhL1Ra7i688Ilbo; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcwODc1NTQwNCwiZXhwIjoxNzA4NzU2MDA0fQ.rAG0OkDpSTsBnZH865imaDQYed_5tRzzjSj7rVuLKf0; _ga_ZPGRNTNNRT=GS1.1.1708751713.65.1.1708755415.0.0.0; nonce=ss-2451472327',
        'Origin': 'https://advertising.flipkart.com',
        'Pragma': 'no-cache',
        'Referer': 'https://advertising.flipkart.com/ad-account/reports/pca?baccount=PHO4MLL4X6QR&aaccount=IIZEQUC5TFAH&duration=2024-02-09_2024-02-09%2Ccustom',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'accept': '*/*',
        'apollographql-client-name': 'Flipkart-Ads',
        'apollographql-client-version': '1.0.0',
        'content-type': 'application/json',
        'downlink': '3.45',
        'dpr': '1.25',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'viewport-width': '914',
        'x-csrf-token': 'rFkY1ZwN-STnU0i4Khq7Yfe5eOY3NPTpiqb4',
        'x-pageContext': 'report-dashboard#BRAND_PCA#adaccount#scorecard',
        'x-sourceurl': 'https://advertising.flipkart.com/ad-account/reports/pca?baccount=PHO4MLL4X6QR&aaccount=IIZEQUC5TFAH&duration=2024-02-09_2024-02-09%2Ccustom',
        'x-tenant': 'BSS',
    }

    json_data = {
        'operationName': 'getURFTabularData',
        'variables': {
            'dateRange': {
                'endDate': '2024-02-12',
                'startDate': '2024-02-09',
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
                                    'IIZEQUC5TFAH',
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
                        'group_by': [],
                        'metrics': [
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
                                'function': 'SUM',
                                'name': 'click_direct_converted_ppv',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'advertiser_spend',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'click_roi',
                            },
                            {
                                'function': 'VALUE',
                                'name': 'click_total_converted_units',
                            },
                        ],
                        'order_by': {
                            'fields': [],
                            'type': 'ASC',
                        },
                        'page_size': 10,
                        'type': 'TABULAR',
                        'view_id': '603',
                    },
                    'queryId': 'scorecard-0.94jyr7z8vt9',
                },
            ],
            'requestId': 'wi4jgegs5ks',
            'timeGranularity': 'DAY',
        },
        'query': 'query getURFTabularData($dateRange: URFDateRange, $timeGranularity: String, $requestId: String, $pageLevelFilter: [URFFilter], $queries: [URFQuerySet]) {\n  getURFTabularData(dateRange: $dateRange, timeGranularity: $timeGranularity, requestId: $requestId, pageLevelFilter: $pageLevelFilter, queries: $queries) {\n    queryId\n    data {\n      code\n      columns {\n        entityType\n        name\n        type\n        metadata {\n          HAS_MULTISOURCE\n          __typename\n        }\n        __typename\n      }\n      rows {\n        values\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
    }

    response = requests.post('https://advertising.flipkart.com/api', cookies=cookies_x, headers=headers, json=json_data)
    ans = json.loads(response.text)
    print(ans)



if __name__ == '__main__':
    dateload(cookie_generator()[0])


    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"operationName":"getURFTabularData","variables":{"dateRange":{"endDate":"2024-02-09","startDate":"2024-02-09"},"pageLevelFilter":[{"comparator":["BRAND_PCA"],"field":{"entity_type":"DIMENSION","function":"VALUE","name":"campaign_type"},"operator":"IN","view_id":"603"},{"comparator":["FLIPKART"],"field":{"entity_type":"DIMENSION","function":"VALUE","name":"marketplace"},"operator":"IN","view_id":"603"}],"queries":[{"query":{"filters":[{"comparator":["IIZEQUC5TFAH"],"field":{"entity_type":"DIMENSION","function":"VALUE","name":"advertiser_id"},"operator":"IN","view_id":"603"}],"group_by":[],"metrics":[{"function":"SUM","name":"views"},{"function":"SUM","name":"clicks"},{"function":"VALUE","name":"CTR"},{"function":"SUM","name":"click_direct_converted_ppv"},{"function":"VALUE","name":"advertiser_spend"},{"function":"VALUE","name":"click_roi"},{"function":"VALUE","name":"click_total_converted_units"}],"order_by":{"fields":[],"type":"ASC"},"page_size":10,"type":"TABULAR","view_id":"603"},"queryId":"scorecard-0.94jyr7z8vt9"}],"requestId":"wi4jgegs5ks","timeGranularity":"DAY"},"query":"query getURFTabularData($dateRange: URFDateRange, $timeGranularity: String, $requestId: String, $pageLevelFilter: [URFFilter], $queries: [URFQuerySet]) {\\n  getURFTabularData(dateRange: $dateRange, timeGranularity: $timeGranularity, requestId: $requestId, pageLevelFilter: $pageLevelFilter, queries: $queries) {\\n    queryId\\n    data {\\n      code\\n      columns {\\n        entityType\\n        name\\n        type\\n        metadata {\\n          HAS_MULTISOURCE\\n          __typename\\n        }\\n        __typename\\n      }\\n      rows {\\n        values\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'
    #response = requests.post('https://advertising.flipkart.com/api', cookies=cookies, headers=headers, data=data)