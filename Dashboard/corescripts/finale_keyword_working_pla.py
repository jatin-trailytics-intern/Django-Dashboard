import requests
import json
import pymysql
from channel import *


def keywords_data(cookie_dict={}):
    cookies_x = {
        'T': 'TI169891842149300161944937865135939588577615020537527148270186391420',
        '_pxvid': 'c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0',
        'dpr': '1.25',
        '_fbp': 'fb.1.1700471257731.638459595',
        '_ga_B9RGC9GN63': 'GS1.1.1702722512.1.1.1702722682.54.0.0',
        'DID': 'clr1pup252bqp0x0wejpe1ajo',
        'ULSN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw',
        'vh': '730',
        'vw': '1536',
        '_ga_0RGM1K38MN': 'GS1.2.1708195526.2.1.1708195657.0.0.0',
        '_ga_C00F4Q43Q7': 'GS1.2.1708196044.1.0.1708196044.0.0.0',
        '_ga_2P94RMW04V': 'GS1.2.1708196121.6.1.1708196143.0.0.0',
        '_gcl_au': '1.1.856723108.1708257205',
        'K-ACTION': 'null',
        'ud': '3.-hCuLDZfVJf9kwEcWhK4arj09yD35YGA9WD7yo1zRPr-6c1rmX2_xdHegqPpB3V8IXYz3NsAnP3SBWNaEKufBfykm01W9EISet6O__tpbwLut1-EZphHbJ0c9MzW0rczeRXhalfDVODMz8JTNMlQlgc9FtPFTSU9rNePFCXS_okASoEjAhPorkspIuB6dUcZtsYfTSEOj6D6fCfEhHGTX040PuZMdyiyk409VK7VDUArNQCXrRjfusSZdRR_dSa_IYardO48M5GyGz8FGpTkPTBYE_1zDB-5NXEc93lP2wklWoHEa-Dtp_7e6v2PvoLYEnO9q9WRO923E1MzbxEsgQzTal18ocz6m1QhVKcLAkifQY1CVPvSCEDYAhYysg7Cifn25pVGYReJE-wqKz__XeZKWQ6m9S5ylJWi8ZCNic_rQWkW8tl4jP7uwPxupbq0hBk3YeSRAVvcjX09zDY5qn4jmi-pJicw3oOin6BBwh5j4AEuCE1_UBhyu1FzQ6HXVin354_zqMKmt5Ez4awQztwLbxHMqBrzPLNw1nVv-mMH56A0UIV523BaT7wlgFXFKDY9PgZuquXJtkpqqSSPK3sdeoBmL_SsoP5XdHnW3U3lvtJigEiuV1-2In3wufWsqsHYvXC8tj7Vr6X8srs_3ehJ7eFh0ZMdB7QsQTCynabS2sW3gILSeLC2-NwmdaemzanTaScNERb6Z6uBV6aYgxLtiUZZci5cqwxPaCVTIRHxdKh90EtL6MagI-T8KaMNUkYxg3mOLw4UnS1OIQr5vw',
        'S': 'd1t12fhAXNGc/P2M/ED8/Pz8YP5R1C2QLptKLX45nMO0fPoszL18MfCR2oiJUPJpcjVoXbOSe+gCGx2r6cyEFxAneSA==',
        'SN': 'VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710765484.LI',
        'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MTA3NjcyODQsImlhdCI6MTcxMDc2NTQ4NCwiaXNzIjoia2V2bGFyIiwianRpIjoiODFkMDMxZGEtMzk1Yy00NTU0LTllMmMtYThmYTdlYTc4Y2ZlIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJBSEJRRVciLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImJlMHVRSWdQSVRwMlpxYW5OTmhobkdIamhSdi1QMVhOTmNURnloQS16QVNBWU40QlZ2NF9Odz09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.2jYBO6I7KAY5j8GWCj3G9hx7PvI2zH-FYWv2vXh89MM',
        'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjY2NjMwODQsImlhdCI6MTcxMDc2NTQ4NCwiaXNzIjoia2V2bGFyIiwianRpIjoiOGEzNmFjMWMtZjBjYi00ZjExLTkyODctZDUxMzRmNTYxZWMyIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJBSEJRRVciLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiREtRVEMxIn0.PXoD2ZaB5kLjOV3-RFLMrNbeNgWaaobWa5lp-NrPq9I',
        'vd': 'VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-44.1710765484.1710765484.162428945',
        'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19801%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1711370283%7C12%7CMCAAMB-1711370283%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710772683s%7CNONE%7CMCAID%7CNONE',
        '_gid': 'GA1.2.1938733017.1710833007',
        'mp_9ea3bc9a23c575907407cf80efd56524_mixpanel': '%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D',
        'AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg': '-227196251%7CMCIDTS%7C19801%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1710923132%7C12%7CMCAAMB-1711451720%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710854120s%7CNONE%7CMCAID%7CNONE',
        's_nr': '1710846920850-Repeat',
        '_ga_0SJLGHBL81': 'GS1.1.1710850316.23.0.1710850316.0.0.0',
        '_ga_TVF0VCMCT3': 'GS1.1.1710850316.144.0.1710850316.60.0.0',
        '_ga': 'GA1.1.1819741834.1700633034',
        'CURRENT_TENANT': 'BSS',
        '_csrf': 'iirRYaQp7N7J4PssrzUPMaNg',
        'TENANT': 'BSS',
        'BSS_SID': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA1MGRjYzRjLTE0MGYtNDNkYy1iYTUzLTM2NTY3MTQ3MWVlZSJ9.eyJleHAiOjE3MTA5MjI4NzYsImlhdCI6MTcxMDkyMTA3NiwiaXNzIjoia2V2bGFyIiwianRpIjoiOWNhMjhhMWMtNTAwMi00ZjYyLTkzMjktMDY0ZWI5MDBmYmRlIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IkNXR0g5TCIsImtldklkIjoiVklBREFBMDM0RDUyQTA0Q0MwQjc1QUNGNTc3NDE4QUMzMSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEelFjYkRsbnItWWJIaUhZVUpvT2JpdnNPUHk0bUhuOER6c2xLRkxYeUZsMTB0X3RweVdubmc9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.ep4rsjYCEXpRt3PL4PbXI9d9yVrRNizXk0L01xXLDAk',
        'BSS_UDT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMDkyMTgyMiwiZXhwIjoxNzEwOTIyNDIyfQ.es5eVN3_Fn--tvRo4mknnu6WtUq1xdXlZryWsxjhbwE',
        '_ga_ZPGRNTNNRT': 'GS1.1.1710919318.152.1.1710922182.0.0.0',
        'nonce': 'ss-2393985423',
    }

    for key in cookie_dict.keys():
        if key in cookies_x:
            cookies_x[key] = cookie_dict[key]


    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'T=TI169891842149300161944937865135939588577615020537527148270186391420; _pxvid=c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0; dpr=1.25; _fbp=fb.1.1700471257731.638459595; _ga_B9RGC9GN63=GS1.1.1702722512.1.1.1702722682.54.0.0; DID=clr1pup252bqp0x0wejpe1ajo; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw; vh=730; vw=1536; _ga_0RGM1K38MN=GS1.2.1708195526.2.1.1708195657.0.0.0; _ga_C00F4Q43Q7=GS1.2.1708196044.1.0.1708196044.0.0.0; _ga_2P94RMW04V=GS1.2.1708196121.6.1.1708196143.0.0.0; _gcl_au=1.1.856723108.1708257205; K-ACTION=null; ud=3.-hCuLDZfVJf9kwEcWhK4arj09yD35YGA9WD7yo1zRPr-6c1rmX2_xdHegqPpB3V8IXYz3NsAnP3SBWNaEKufBfykm01W9EISet6O__tpbwLut1-EZphHbJ0c9MzW0rczeRXhalfDVODMz8JTNMlQlgc9FtPFTSU9rNePFCXS_okASoEjAhPorkspIuB6dUcZtsYfTSEOj6D6fCfEhHGTX040PuZMdyiyk409VK7VDUArNQCXrRjfusSZdRR_dSa_IYardO48M5GyGz8FGpTkPTBYE_1zDB-5NXEc93lP2wklWoHEa-Dtp_7e6v2PvoLYEnO9q9WRO923E1MzbxEsgQzTal18ocz6m1QhVKcLAkifQY1CVPvSCEDYAhYysg7Cifn25pVGYReJE-wqKz__XeZKWQ6m9S5ylJWi8ZCNic_rQWkW8tl4jP7uwPxupbq0hBk3YeSRAVvcjX09zDY5qn4jmi-pJicw3oOin6BBwh5j4AEuCE1_UBhyu1FzQ6HXVin354_zqMKmt5Ez4awQztwLbxHMqBrzPLNw1nVv-mMH56A0UIV523BaT7wlgFXFKDY9PgZuquXJtkpqqSSPK3sdeoBmL_SsoP5XdHnW3U3lvtJigEiuV1-2In3wufWsqsHYvXC8tj7Vr6X8srs_3ehJ7eFh0ZMdB7QsQTCynabS2sW3gILSeLC2-NwmdaemzanTaScNERb6Z6uBV6aYgxLtiUZZci5cqwxPaCVTIRHxdKh90EtL6MagI-T8KaMNUkYxg3mOLw4UnS1OIQr5vw; S=d1t12fhAXNGc/P2M/ED8/Pz8YP5R1C2QLptKLX45nMO0fPoszL18MfCR2oiJUPJpcjVoXbOSe+gCGx2r6cyEFxAneSA==; SN=VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710765484.LI; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MTA3NjcyODQsImlhdCI6MTcxMDc2NTQ4NCwiaXNzIjoia2V2bGFyIiwianRpIjoiODFkMDMxZGEtMzk1Yy00NTU0LTllMmMtYThmYTdlYTc4Y2ZlIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJBSEJRRVciLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImJlMHVRSWdQSVRwMlpxYW5OTmhobkdIamhSdi1QMVhOTmNURnloQS16QVNBWU40QlZ2NF9Odz09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.2jYBO6I7KAY5j8GWCj3G9hx7PvI2zH-FYWv2vXh89MM; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjY2NjMwODQsImlhdCI6MTcxMDc2NTQ4NCwiaXNzIjoia2V2bGFyIiwianRpIjoiOGEzNmFjMWMtZjBjYi00ZjExLTkyODctZDUxMzRmNTYxZWMyIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJBSEJRRVciLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiREtRVEMxIn0.PXoD2ZaB5kLjOV3-RFLMrNbeNgWaaobWa5lp-NrPq9I; vd=VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-44.1710765484.1710765484.162428945; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19801%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1711370283%7C12%7CMCAAMB-1711370283%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710772683s%7CNONE%7CMCAID%7CNONE; _gid=GA1.2.1938733017.1710833007; mp_9ea3bc9a23c575907407cf80efd56524_mixpanel=%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D; AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg=-227196251%7CMCIDTS%7C19801%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1710923132%7C12%7CMCAAMB-1711451720%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710854120s%7CNONE%7CMCAID%7CNONE; s_nr=1710846920850-Repeat; _ga_0SJLGHBL81=GS1.1.1710850316.23.0.1710850316.0.0.0; _ga_TVF0VCMCT3=GS1.1.1710850316.144.0.1710850316.60.0.0; _ga=GA1.1.1819741834.1700633034; CURRENT_TENANT=BSS; _csrf=iirRYaQp7N7J4PssrzUPMaNg; TENANT=BSS; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA1MGRjYzRjLTE0MGYtNDNkYy1iYTUzLTM2NTY3MTQ3MWVlZSJ9.eyJleHAiOjE3MTA5MjI4NzYsImlhdCI6MTcxMDkyMTA3NiwiaXNzIjoia2V2bGFyIiwianRpIjoiOWNhMjhhMWMtNTAwMi00ZjYyLTkzMjktMDY0ZWI5MDBmYmRlIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IkNXR0g5TCIsImtldklkIjoiVklBREFBMDM0RDUyQTA0Q0MwQjc1QUNGNTc3NDE4QUMzMSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEelFjYkRsbnItWWJIaUhZVUpvT2JpdnNPUHk0bUhuOER6c2xLRkxYeUZsMTB0X3RweVdubmc9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.ep4rsjYCEXpRt3PL4PbXI9d9yVrRNizXk0L01xXLDAk; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMDkyMTgyMiwiZXhwIjoxNzEwOTIyNDIyfQ.es5eVN3_Fn--tvRo4mknnu6WtUq1xdXlZryWsxjhbwE; _ga_ZPGRNTNNRT=GS1.1.1710919318.152.1.1710922182.0.0.0; nonce=ss-2393985423',
        'Origin': 'https://advertising.flipkart.com',
        'Pragma': 'no-cache',
        'Referer': 'https://advertising.flipkart.com/ad-account/campaigns/pla/OWL1UYKSNRYR/edit?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
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
        'viewport-width': '795',
        'x-aaccount': 'IZJL4R3KCMHR',
        'x-baccount': 'N5J3WN87DKC4',
        'x-csrf-token': 'CSDOad48-7SCyzJuCn8UlG_SSDhEn0_sOWUI',
        'x-sourceurl': 'https://advertising.flipkart.com/ad-account/campaigns/pla/OWL1UYKSNRYR/edit?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
        'x-tenant': 'BSS',
    }
    finale_output =[]
    i=2
    id=["OWL1UYKSNRYR","8VN5DXLKJN8A"]
    while i>0:
        json_data = {
        'operationName': 'GetCampaign',
        'variables': {
            'seller': False,
            'id': id[i-1],
            'adProduct': 'BRAND_PLA',
        },
        'query': 'query GetCampaign($id: String!, $adProduct: String!, $seller: Boolean! = false) {\n  getCampaignForId(id: $id, adProduct: $adProduct) {\n    ... on CampaignPLAResponse {\n      campaignInfo {\n        id\n        type\n        name\n        status\n        uiStatus\n        currency\n        paymentType\n        budget\n        budgetType\n        fsnIds\n        startDate\n        endDate\n        costModel\n        marketplace\n        pacing\n        withPreferredSellers\n        preferredSellerIds\n        preferredSellerNames\n        businessZones\n        tillBudgetEnds\n        fsnMeta {\n          id\n          title\n          image\n          minListingPrice\n          maxListingPrice\n          listingCurrency\n          brand\n          storeList\n          __typename\n        }\n        __typename\n      }\n      adGroups {\n        id\n        name\n        status\n        productCount\n        commodityId\n        cost\n        budget\n        targeting {\n          type\n          pages\n          excludeKeywords {\n            q\n            r\n            __typename\n          }\n          includeKeywords {\n            q\n            r\n            matchType\n            __typename\n          }\n          __typename\n        }\n        storePaths\n        fsnBanners {\n          id\n          fsnId\n          __typename\n        }\n        costVariation {\n          ...PlacementsFragment\n          __typename\n        }\n        __typename\n      }\n      brandIds\n      preferredSellers {\n        alias\n        sellerId\n        __typename\n      }\n      placementsMetaInfo {\n        ...PlacementsMetaInfoFragement\n        __typename\n      }\n      __typename\n    }\n    ... on CampaignPCAResponse {\n      campaignInfo {\n        id\n        type\n        name\n        status\n        uiStatus\n        currency\n        paymentType\n        budget\n        budgetType\n        startDate\n        endDate\n        costModel\n        marketplace\n        __typename\n      }\n      adGroups {\n        id\n        name\n        status\n        uiStatus\n        startDate\n        endDate\n        cost\n        budget\n        excludeKeywords\n        marketplace\n        showAdInBroadMatchStores\n        costVariation {\n          ...PlacementsFragment\n          __typename\n        }\n        allowedActions\n        pacing\n        targeting {\n          type\n          pages\n          excludeKeywords {\n            q\n            r\n            __typename\n          }\n          includeKeywords {\n            q\n            r\n            matchType\n            __typename\n          }\n          __typename\n        }\n        contents {\n          contentId\n          creativeBanners {\n            creativeId\n            creativeName\n            creativeTemplateId\n            uiStatus\n            status\n            allowedActions\n            referenceId\n            mediaId\n            creativeType\n            assets {\n              macro\n              value\n              type\n              origin\n              assetId\n              subAssets {\n                macro\n                value\n                type\n                __typename\n              }\n              __typename\n            }\n            isSelected\n            id\n            language\n            __typename\n          }\n          collectionUrl\n          landingPageUrl\n          collectionId\n          collectionType\n          brands\n          stores {\n            storeId\n            storeName\n            __typename\n          }\n          rejectedCount\n          isPreferredSeller\n          creativeTemplateId\n          __typename\n        }\n        __typename\n      }\n      brandIds\n      placementsMetaInfo {\n        ...PlacementsMetaInfoFragement\n        __typename\n      }\n      __typename\n    }\n    ... on CampaignDisplayAdsResponse {\n      campaignInfo {\n        id\n        type\n        name\n        status\n        uiStatus\n        currency\n        paymentType\n        budget\n        startDate\n        endDate\n        costModel\n        marketplace\n        pacing\n        budgetType\n        adFormat\n        publisher\n        __typename\n      }\n      adGroups {\n        id\n        name\n        status\n        uiStatus\n        startDate\n        endDate\n        cost\n        budget\n        allowedActions\n        marketplace\n        pacing\n        contents {\n          contentId\n          creativeBanners {\n            creativeId\n            creativeName\n            uiStatus\n            status\n            allowedActions\n            referenceId\n            mediaId\n            videoMediaStatus\n            creativeType\n            assets {\n              macro\n              value\n              type\n              origin\n              subAssets {\n                macro\n                value\n                type\n                __typename\n              }\n              isSystemAsset\n              __typename\n            }\n            isSelected\n            id\n            __typename\n          }\n          collectionUrl\n          collectionId\n          collectionType\n          brands\n          stores {\n            storeId\n            storeName\n            __typename\n          }\n          rejectedCount\n          isUrlSystemCreated\n          landingPageUrl\n          status\n          isPreferredSeller\n          __typename\n        }\n        frequencyCapping {\n          interval\n          value\n          numberOfIntervals\n          __typename\n        }\n        customScheduling\n        channels\n        userTargetingExpression {\n          groupId\n          type\n          values\n          publisherSpecific\n          __typename\n        }\n        contextTargetingExpression {\n          groupId\n          type\n          values\n          publisherSpecific\n          __typename\n        }\n        __typename\n      }\n      brandIds\n      __typename\n    }\n    __typename\n  }\n  getAdAccountDetails @skip(if: $seller) {\n    marketplaceConfigurationResponse {\n      marketplaceList\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PlacementsFragment on CostVariationType {\n  placements {\n    absoluteCost\n    percentage\n    type\n    pageType\n    __typename\n  }\n  __typename\n}\n\nfragment PlacementsMetaInfoFragement on PlacementsMeta {\n  type\n  title\n  detail\n  pageType\n  __typename\n}\n',
    }
        y = json_data['variables']['id']
        response = requests.post('https://advertising.flipkart.com/api', cookies=cookies_x, headers=headers, json=json_data)
    

        x = json.loads(response.text)
        names = (x["data"]["getCampaignForId"]["adGroups"][0]["name"])
        fsn_ids = (x["data"]["getCampaignForId"]["campaignInfo"]["fsnIds"])
        pla_pca = (x["data"]["getCampaignForId"]["campaignInfo"]["type"])
        name = (x["data"]["getCampaignForId"]["campaignInfo"]["name"])
        budget = (x["data"]["getCampaignForId"]["campaignInfo"]["budget"])
        start_date =  (x["data"]["getCampaignForId"]["campaignInfo"]["startDate"][:10])
        end_date = (x["data"]["getCampaignForId"]["campaignInfo"]["endDate"])
        cost_model = (x["data"]["getCampaignForId"]["campaignInfo"]["costModel"])
        ads_grps =  (x["data"]["getCampaignForId"]["adGroups"][0]["id"])
        cost =  (x["data"]["getCampaignForId"]["adGroups"][0]["cost"])
        store_path =  (x["data"]["getCampaignForId"]["adGroups"][0]["storePaths"])
        data  =  (x["data"]["getCampaignForId"]["adGroups"][0]["costVariation"]["placements"])
        status = x["data"]["getCampaignForId"]["adGroups"][0]["status"]
        # print(name)
        


        placements = []


        for item in data:
            placement = {
                'absoluteCost': item['absoluteCost'],
                'type': item['type'],
                'percentage': item['percentage'],
                'campaignId': y
            }
            placements.append(placement)
        #print(placements)

        def needed():
            return placements
    

        DB_HOST = "tr-wp-database.cfqdq6ohjn0p.us-east-1.rds.amazonaws.com"
        DB_USER = "shivam"
        DB_PASSWORD = "Trailytics@789"
        DB_DATABASE =  "amazon_ads_api"
        DB_PORT = 3306

        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_DATABASE,
            port=DB_PORT,
            connect_timeout=1000,
            autocommit=True
        )

        cursor = connection.cursor()

        start_date = '2024-03-10'
        end_date = '2024-03-10'
        campaign_data=id[i-1]
        print(campaign_data)

        sql = "SELECT * FROM fk_kw_pla WHERE DATE(date) BETWEEN %s AND %s AND `campaign_ID` = %s"
        cursor.execute(sql, (start_date, end_date, campaign_data))  # Execute the SQL query
        #print(placements)
        results = cursor.fetchall()
        # print("-------------------------------------------------------------------------------------------------------------------------")
        result_list = []

        for row in results:
            row_found = False
            for placement in placements:
                if placement["campaignId"] == row[0] and placement["type"] == row[4]:
                    row_dict = {
                        "campaign_id": row[0],  
                        "campaign_name": row[1],
                        "adgroup_id": row[2],
                        "adgroup_name": row[3],
                        "placement_type": row[4],
                        "views": row[5],
                        "clicks": float(row[6]),
                        "ctr": float(row[7]),
                        "cpc": float(row[8]),
                        "cvr": row[9],
                        "adspend": float(row[10]),
                        "usdir": row[11],
                        "usind": row[12],
                        "revenue": row[13],
                        "Inrevenue": row[14],
                        "roid": float(row[15]),
                        "roii": float(row[16]),
                        "roas": row[17],
                        "troas": row[18],
                        "service":status
                    }
                    row_dict["required"] = placement['absoluteCost']
                    result_list.append(row_dict)
                    row_found = True
                    break 

            if not row_found:
            
                row_dict = {
                    "campaign_id": row[0],  
                    "Campaign Name": row[1],
                    "adgroup_id": row[2],
                    "adgroup_name": row[3],
                    "placement_type": placement["type"],
                    "views": 0,
                    "clicks": 0,
                    "ctr": 0,
                    "cpc": 0,
                    "cvr": 0,
                    "adspend": 0,
                    "usdir": 0,
                    "usind": 0,
                    "revenue": 0,
                    "Inrevenue": 0,
                    "roid": 0,
                    "roii": 0,
                    "roas": 0,
                    "troas": 0,
                     "service":status,
                }
                result_list.append(row_dict)
        finale_output += result_list
        i-=1
        # print(finale_output)
    return finale_output[0]




print(keywords_data(cookie_generator()[0]))